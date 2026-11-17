#!/usr/bin/env python3
"""Verify preserved source and complete distribution hashes using only stdlib."""
import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def verify(manifest):
    count = 0
    for line in manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        path = ROOT / name
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError('Unsafe manifest path: ' + name)
        if not path.is_file() or digest(path) != expected:
            raise ValueError('Missing or changed file: ' + name)
        count += 1
    print(str(manifest.relative_to(ROOT)) + ': PASS (' + str(count) + ' files)')
    return count

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-only', action='store_true', help='Verify Git source without large distribution assets')
    args = ap.parse_args()
    verify(ROOT / 'release/scientific-files.sha256')
    if args.source_only:
        print('Source-only verification; complete distribution not assessed.')
    else:
        if not (ROOT / 'MANIFEST.sha256').is_file():
            ap.error('Complete archive manifest is absent; use --source-only for a Git checkout.')
        verify(ROOT / 'MANIFEST.sha256')
        image = ROOT / 'docker/mlirbench-ae-v0.3.0rc5-image.tar'
        if not image.is_file():
            raise ValueError('The actual Docker export is absent')
        print('Complete archive file integrity: PASS. Run docker load and quickstart as documented.')

if __name__ == '__main__':
    main()
