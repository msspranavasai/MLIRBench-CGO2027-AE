#!/usr/bin/env python3
"""Verify package-metadata SHA-256 is bound to the exact built Docker image.

This independent check complements the frozen scientific source fingerprint.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[2]
LABEL = 'org.mlirbench.package-metadata-sha256'


def package_identity(root: Path) -> tuple[str, str]:
    content = (root / 'pyproject.toml').read_bytes()
    return hashlib.sha256(content).hexdigest(), tomllib.loads(content.decode())['project']['version']


def require_identity(expected_sha: str, expected_version: str,
                     image_label: str, actual_sha: str, installed_version: str) -> None:
    if image_label != expected_sha:
        raise ValueError('Docker image package metadata label is missing or stale')
    if actual_sha != expected_sha:
        raise ValueError('Docker image /app/pyproject.toml bytes differ from checkout')
    if installed_version != expected_version:
        raise ValueError('Installed MLIRBench distribution version differs from checkout')


def verify_image(image: str, platform: str, root: Path) -> None:
    expected_sha, version = package_identity(root)
    template = '{{index .Config.Labels "' + LABEL + '"}}'
    label = subprocess.check_output(
        ['docker', 'image', 'inspect', '--platform', platform,
         '--format', template, image], text=True).strip()
    code = (
        'import hashlib,importlib.metadata,json,pathlib;'
        'p=pathlib.Path("/app/pyproject.toml");'
        'print(json.dumps({"sha":hashlib.sha256(p.read_bytes()).hexdigest(),'
        '"version":importlib.metadata.version("mlirbench")}))'
    )
    raw = subprocess.check_output(
        ['docker', 'run', '--rm', '--network', 'none', '--platform', platform,
         '--entrypoint', 'python', image, '-I', '-c', code], text=True)
    data = json.loads(raw)
    require_identity(expected_sha, version, label, data['sha'], data['version'])
    print(f'PASS: package metadata label, image bytes, and installed MLIRBench {version} agree ({platform})')


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=ROOT)
    ap.add_argument('--image')
    ap.add_argument('--platform', choices=('linux/arm64', 'linux/amd64'))
    args = ap.parse_args()
    if args.image and not args.platform:
        ap.error('--platform required with --image')
    if args.platform and not args.image:
        ap.error('--image required with --platform')
    if args.image:
        verify_image(args.image, args.platform, args.root.resolve())
    else:
        print(package_identity(args.root.resolve())[0])


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
