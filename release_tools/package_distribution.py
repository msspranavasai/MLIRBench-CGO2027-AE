#!/usr/bin/env python3
"""Package a verified, complete rc6 distribution with deterministic tar metadata."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile

sys.dont_write_bytecode = True
FORBIDDEN = {'.git', '__pycache__', '.venv', 'venv', '.pytest_cache',
             '.ruff_cache', '.DS_Store', '.AppleDouble', 'node_modules'}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--timestamp', type=int, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    release = json.loads((root / 'release/release.json').read_text())
    if root.name != release['root_directory'] or output.name != release['archive']:
        parser.error('Archive name and top-level directory must match release/release.json')
    if output.is_relative_to(root) or output.exists():
        parser.error('Use a new output archive outside the distribution root')
    for path in root.rglob('*'):
        if path.is_symlink() or any(x in FORBIDDEN or x.startswith('._') or x == '.env' or x.startswith('.env.') for x in path.relative_to(root).parts):
            parser.error('Unintended file: ' + str(path.relative_to(root)))
    manifest = root / 'MANIFEST.sha256'
    files = sorted(p for p in root.rglob('*') if p.is_file() and p != manifest)
    manifest.write_text(''.join(sha(p) + '  ' + p.relative_to(root).as_posix() + '\n' for p in files))
    subprocess.run([sys.executable, '-B', str(root / 'release_tools/verify_distribution.py')], check=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('xb') as raw, gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=6) as gz:
        with tarfile.open(fileobj=gz, mode='w|', format=tarfile.PAX_FORMAT, dereference=True) as archive:
            for path in sorted(p for p in root.rglob('*') if p.is_file()):
                info = archive.gettarinfo(str(path), arcname=root.name + '/' + path.relative_to(root).as_posix())
                info.uid = info.gid = 0
                info.uname = info.gname = ''
                info.mtime = args.timestamp
                info.mode = 0o755 if path.stat().st_mode & 0o111 else 0o644
                info.pax_headers = {}
                with path.open('rb') as stream:
                    archive.addfile(info, stream)
    digest = sha(output)
    output.with_name(output.name + '.sha256').write_text(digest + '  ' + output.name + '\n')
    print(str(output) + ' ' + str(output.stat().st_size) + ' bytes SHA256 ' + digest)


if __name__ == '__main__':
    main()
