"""Pure package-metadata identity checks, independent of Docker availability."""
import hashlib
from pathlib import Path
import tempfile
import unittest

from tools.release.package_image_identity import package_identity, require_identity


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
