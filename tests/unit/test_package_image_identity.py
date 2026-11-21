"""Pure package-metadata identity checks, independent of Docker availability."""
import hashlib
import json
from pathlib import Path
from unittest.mock import patch
import tempfile
import unittest

from tools.release.package_image_identity import (
    LABEL, package_identity, require_identity, verify_image,
)


class PackageImageIdentity(unittest.TestCase):
    def test_exact_pyproject_bytes_define_package_identity(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = b'[project]\nversion="0.3.0rc6"\n'
            (root / 'pyproject.toml').write_bytes(source)
            self.assertEqual(package_identity(root), (hashlib.sha256(source).hexdigest(), '0.3.0rc6'))
            (root / 'pyproject.toml').write_bytes(source + b'\n')
            self.assertNotEqual(package_identity(root)[0], hashlib.sha256(source).hexdigest())

    def test_matching_image_passes(self):
        require_identity('a' * 64, '0.3.0rc6', 'a' * 64, 'a' * 64, '0.3.0rc6')

    def test_stale_or_missing_label_fails(self):
        for label in ('<no value>', '', 'b' * 64):
            with self.subTest(label=label), self.assertRaisesRegex(ValueError, 'label'):
                require_identity('a' * 64, '0.3.0rc6', label, 'a' * 64, '0.3.0rc6')

    def test_changed_embedded_package_file_fails(self):
        with self.assertRaisesRegex(ValueError, 'bytes'):
            require_identity('a' * 64, '0.3.0rc6', 'a' * 64, 'b' * 64, '0.3.0rc6')

    def test_wrong_installed_distribution_fails(self):
        with self.assertRaisesRegex(ValueError, 'version'):
            require_identity('a' * 64, '0.3.0rc6', 'a' * 64, 'a' * 64, '0.3.0rc5')

    def _simulate_docker(self, root, *, inspect_help, reported_arch='arm64'):
        from tools.release.package_image_identity import package_identity
        sha, version = package_identity(root)
        calls = []

        def command(args, *, text):
            self.assertTrue(text)
            calls.append(args)
            if args == ['docker', 'image', 'inspect', '--help']:
                return inspect_help
            if args[:3] == ['docker', 'image', 'inspect']:
                return json.dumps({
                    'Os': 'linux', 'Architecture': reported_arch,
                    'Config': {'Labels': {LABEL: sha}},
                })
            if args[:2] == ['docker', 'run']:
                return json.dumps({'sha': sha, 'version': version})
            raise AssertionError('Unexpected Docker command: ' + repr(args))

        return calls, command

    def test_older_docker_omits_unsupported_flag_and_checks_arch(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'pyproject.toml').write_text('[project]\nversion="0.3.0rc6"\n')
            calls, command = self._simulate_docker(root, inspect_help='Usage: docker image inspect')
            with patch('tools.release.package_image_identity.subprocess.check_output', side_effect=command):
                verify_image('test:latest', 'linux/arm64', root)
            inspect = next(c for c in calls if c[:3] == ['docker', 'image', 'inspect'] and '--format' in c)
            self.assertNotIn('--platform', inspect)
            self.assertTrue(any(c[:2] == ['docker', 'run'] for c in calls))

    def test_newer_docker_selects_requested_platform(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'pyproject.toml').write_text('[project]\nversion="0.3.0rc6"\n')
            calls, command = self._simulate_docker(root, inspect_help='--platform string')
            with patch('tools.release.package_image_identity.subprocess.check_output', side_effect=command):
                verify_image('test:latest', 'linux/arm64', root)
            inspect = next(c for c in calls if c[:3] == ['docker', 'image', 'inspect'] and '--format' in c)
            self.assertEqual(inspect[inspect.index('--platform') + 1], 'linux/arm64')

    def test_older_docker_rejects_wrong_arch_before_container_run(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'pyproject.toml').write_text('[project]\nversion="0.3.0rc6"\n')
            calls, command = self._simulate_docker(root, inspect_help='Usage:', reported_arch='amd64')
            with patch('tools.release.package_image_identity.subprocess.check_output', side_effect=command):
                with self.assertRaisesRegex(ValueError, 'platform mismatch'):
                    verify_image('test:latest', 'linux/arm64', root)
            self.assertFalse(any(c[:2] == ['docker', 'run'] for c in calls))
