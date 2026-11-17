#!/usr/bin/env python3
"""Verify release source, every packaged byte, supplemental assets and OCI blobs."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import tarfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = {'.git', '__pycache__', '.venv', 'venv', '.pytest_cache',
             '.ruff_cache', '.DS_Store', '.AppleDouble', 'node_modules'}


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def safe_path(name):
    rel = PurePosixPath(name)
    if rel.is_absolute() or '..' in rel.parts or str(rel) != name:
        raise ValueError('Unsafe manifest path: ' + name)
    path = ROOT / name
    if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
        raise ValueError('Unsafe manifest path: ' + name)
    return path


def verify(manifest):
    entries = {}
    for line in manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        if len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
            raise ValueError('Invalid SHA-256: ' + name)
        if name in entries:
            raise ValueError('Duplicate manifest entry: ' + name)
        path = safe_path(name)
        if not path.is_file() or digest(path) != expected:
            raise ValueError('Missing or changed file: ' + name)
        entries[name] = expected
    if not entries:
        raise ValueError('Empty manifest: ' + str(manifest))
    print(str(manifest.relative_to(ROOT)) + ': PASS (' + str(len(entries)) + ' files)')
    return entries


def verify_image(release):
    image = safe_path(release['image_archive'])
    inventory = json.loads((ROOT / 'docker/image-inventory.json').read_text())
    if inventory['image'] != release['image'] or digest(image) != inventory['archive_sha256']:
        raise ValueError('Image name or export checksum differs')
    if image.stat().st_size != inventory['archive_bytes']:
        raise ValueError('Image export length differs')
    sys.path.insert(0, str(ROOT / 'src'))
    from mlirbench.ae import source_fingerprint
    identity = source_fingerprint(ROOT)
    with tarfile.open(image, 'r:') as archive:
        members = {m.name: m for m in archive.getmembers() if m.isfile()}
        if len(members) != sum(m.isfile() for m in archive.getmembers()):
            raise ValueError('Duplicate image archive members')
        verified = 0
        for name, member in members.items():
            if name.startswith('blobs/sha256/'):
                h = hashlib.sha256()
                with archive.extractfile(member) as stream:
                    for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
                        h.update(block)
                if h.hexdigest() != name.rsplit('/', 1)[-1]:
                    raise ValueError('Image blob checksum differs: ' + name)
                verified += 1
        def read_blob(descriptor):
            name = 'blobs/sha256/' + descriptor['digest'].split(':', 1)[1]
            if name not in members or members[name].size != descriptor['size']:
                raise ValueError('Missing or truncated image descriptor: ' + name)
            return json.load(archive.extractfile(members[name]))
        found = []
        def walk(index):
            for descriptor in index['manifests']:
                value = read_blob(descriptor)
                if 'manifests' in value:
                    walk(value)
                else:
                    config = read_blob(value['config'])
                    for layer in value['layers']:
                        name = 'blobs/sha256/' + layer['digest'].split(':', 1)[1]
                        if name not in members or members[name].size != layer['size']:
                            raise ValueError('Missing image layer: ' + name)
                    labels = config['config']['Labels']
                    if labels.get('org.mlirbench.source-fingerprint') != identity:
                        raise ValueError('Image/source fingerprint differs')
                    if labels.get('org.opencontainers.image.version') != release['version']:
                        raise ValueError('Image version differs')
                    found.append((config['os'], config['architecture']))
        walk(json.load(archive.extractfile(members['index.json'])))
        if sorted(found) != [('linux', 'amd64'), ('linux', 'arm64')]:
            raise ValueError('Exactly AMD64 and ARM64 image variants are required')
    if inventory['source_fingerprint'] != identity:
        raise ValueError('Inventory/source fingerprint differs')
    print('Image export: PASS (' + str(verified) + ' verified blobs; AMD64/ARM64 metadata; matching source)')
    return identity


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-only', action='store_true')
    args = parser.parse_args()
    verify(ROOT / 'release/scientific-files.sha256')
    verify(ROOT / 'release/scientific-reference.sha256')
    if args.source_only:
        print('Source-only verification: PASS; complete distribution not assessed.')
        return
    release = json.loads((ROOT / 'release/release.json').read_text())
    entries = verify(ROOT / 'MANIFEST.sha256')
    files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    if files != set(entries) | {'MANIFEST.sha256'}:
        raise ValueError('Complete manifest coverage differs: ' + repr(sorted(files ^ (set(entries) | {'MANIFEST.sha256'}))))
    for p in ROOT.rglob('*'):
        parts = p.relative_to(ROOT).parts
        if p.is_symlink() or any(x in FORBIDDEN or x.startswith('._') or x == '.env' or x.startswith('.env.') for x in parts):
            raise ValueError('Unintended development file: ' + str(p.relative_to(ROOT)))
    assets = json.loads((ROOT / 'assets/nova/ASSET_MANIFEST.json').read_text())
    for name, spec in assets['files'].items():
        path = safe_path('assets/nova/' + name)
        if not path.is_file() or path.stat().st_size != spec['bytes'] or digest(path) != spec['sha256']:
            raise ValueError('Supplemental asset differs: ' + name)
    if len(assets['files']) != 914:
        raise ValueError('Original 914-entry supplemental inventory is required')
    for name in ('evidence/label-review', 'evidence/native-ci'):
        if not any(p.is_file() for p in safe_path(name).rglob('*')):
            raise ValueError('Required historical evidence missing: ' + name)
    print('Supplemental assets: PASS (914 original entries; historical evidence present)')
    identity = verify_image(release)
    print('Complete distribution: PASS; source fingerprint ' + identity)
    print('Metadata integrity is not native runtime validation. Run quickstart as documented.')


if __name__ == '__main__':
    main()
