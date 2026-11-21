"""Standalone wheel entrypoint must not silently use site-packages as data."""
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from mlirbench import __version__
from mlirbench import wheel_cli
from mlirbench import cli


class WheelEntrypoint(unittest.TestCase):
    def fixture(self, root: Path, *, version: str = __version__) -> None:
        for name, text in (
            ("data/bundle/manifest.json", "{}"),
            ("experiments/claims.json", "{}"),
            ("release/release.json", json.dumps({"version": version})),
        ):
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)

    def test_rejects_missing_artifact_with_actionable_message(self):
        with TemporaryDirectory() as directory:
            with patch.dict(os.environ, {wheel_cli.ARTIFACT_ENV: directory}):
                with self.assertRaisesRegex(SystemExit, "Missing:"):
                    wheel_cli.locate_artifact_root()

    def test_rejects_relative_artifact_path(self):
        with patch.dict(os.environ, {wheel_cli.ARTIFACT_ENV: "relative/artifact"}):
            with self.assertRaisesRegex(SystemExit, "absolute path"):
                wheel_cli.locate_artifact_root()

    def test_rejects_incompatible_artifact_version(self):
        with TemporaryDirectory() as directory:
            self.fixture(Path(directory), version="999.0.0")
            with patch.dict(os.environ, {wheel_cli.ARTIFACT_ENV: directory}):
                with self.assertRaisesRegex(SystemExit, "does not match"):
                    wheel_cli.locate_artifact_root()

    def test_help_does_not_require_artifact(self):
        with patch.dict(os.environ, {wheel_cli.ARTIFACT_ENV: "/does/not/exist"}):
            with patch.object(cli, "main", return_value=0) as original:
                self.assertEqual(wheel_cli.main(["--help"]), 0)
                original.assert_called_once_with(["--help"])

    def test_valid_artifact_is_used_and_original_globals_restored(self):
        before = (cli.ROOT, cli.DATASET, cli.HISTORICAL)
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            with patch.dict(os.environ, {wheel_cli.ARTIFACT_ENV: directory}):
                def observe(args):
                    self.assertEqual(args, ["dataset-info"])
                    self.assertEqual(cli.ROOT, root)
                    self.assertEqual(cli.DATASET, root / "data/processed/MLIRBench/master/master.jsonl")
                    self.assertEqual(cli.HISTORICAL, root / "data/historical/historical_execution.jsonl")
                    return 0
                with patch.object(cli, "main", side_effect=observe):
                    self.assertEqual(wheel_cli.main(["dataset-info"]), 0)
        self.assertEqual((cli.ROOT, cli.DATASET, cli.HISTORICAL), before)

    def test_source_checkout_default_remains_supported(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            env = os.environ.copy()
            env.pop(wheel_cli.ARTIFACT_ENV, None)
            with patch.dict(os.environ, env, clear=True):
                self.assertEqual(wheel_cli.locate_artifact_root(root), root)


if __name__ == "__main__":
    unittest.main()
