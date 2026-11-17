"""Independent packaging guard tests; scientific test suite is unchanged in count."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('verify_distribution', Path(__file__).with_name('verify_distribution.py'))
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ManifestGuards(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.previous = MODULE.ROOT
        MODULE.ROOT = self.root
        self.addCleanup(setattr, MODULE, 'ROOT', self.previous)
        (self.root/'input').write_bytes(b'frozen bytes')
        self.line = MODULE.digest(self.root/'input') + '  input\n'
        self.manifest = self.root/'manifest'

    def test_changed_bytes_are_rejected(self):
        self.manifest.write_text(self.line)
        (self.root/'input').write_bytes(b'altered bytes')
        with self.assertRaisesRegex(ValueError, 'Missing or changed'):
            MODULE.verify(self.manifest)

    def test_duplicate_paths_are_rejected(self):
        self.manifest.write_text(self.line * 2)
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            MODULE.verify(self.manifest)

    def test_absolute_and_traversing_paths_are_rejected(self):
        for name in ('../input', '/tmp/input', './input'):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'Unsafe'):
                MODULE.safe_path(name)

    def test_symlink_is_rejected_even_for_correct_content(self):
        (self.root/'link').symlink_to(self.root/'input')
        self.manifest.write_text(self.line.replace('  input', '  link'))
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            MODULE.verify(self.manifest)

    def test_valid_manifest_verifies_actual_bytes(self):
        self.manifest.write_text(self.line)
        self.assertEqual(MODULE.verify(self.manifest), {'input': self.line.split()[0]})


if __name__ == '__main__':
    unittest.main()
