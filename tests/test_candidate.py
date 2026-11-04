"""Observable candidate-identity checks in disposable Git repositories."""

import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills/rdd/scripts/candidate.py"
spec = importlib.util.spec_from_file_location("candidate", HELPER)
candidate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(candidate)


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="gentle-stack-candidate-")
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "core.autocrlf", "false")
        (self.repo / "module.py").write_text("value = 1\n", encoding="utf-8")
        (self.repo / ".gitignore").write_text("cache/\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "baseline")
        self.base = self.git("rev-parse", "HEAD").strip().decode()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE)

    def identity(self):
        return candidate.fingerprint(self.repo, self.base)["fingerprint"]

    def test_stable_and_read_only(self):
        status = self.git("status", "--porcelain=v1")
        index = (self.repo / ".git/index").read_bytes()
        before = self.identity()
        self.assertEqual(before, self.identity())
        self.assertEqual(status, self.git("status", "--porcelain=v1"))
        self.assertEqual(index, (self.repo / ".git/index").read_bytes())

    def test_tracked_untracked_and_deleted_content(self):
        original = self.identity()
        (self.repo / "module.py").write_text("value = 2\n", encoding="utf-8")
        changed = self.identity()
        self.assertNotEqual(original, changed)
        extra = self.repo / "new module ñ.txt"
        extra.write_bytes(b"first")
        added = self.identity()
        self.assertNotEqual(changed, added)
        extra.write_bytes(b"second")
        self.assertNotEqual(added, self.identity())
        extra.unlink()
        self.assertEqual(changed, self.identity())
        (self.repo / "module.py").unlink()
        self.assertNotEqual(changed, self.identity())

    def test_staging_and_commit_invalidate_identity(self):
        (self.repo / "module.py").write_text("value = 2\n", encoding="utf-8")
        dirty = self.identity()
        self.git("add", "module.py")
        staged = self.identity()
        self.assertNotEqual(dirty, staged)
        self.git("commit", "-qm", "change")
        self.assertNotEqual(staged, self.identity())

    def test_ignored_inputs_are_explicitly_out_of_scope(self):
        before = self.identity()
        (self.repo / "cache").mkdir()
        (self.repo / "cache/data").write_bytes(b"not captured")
        self.assertEqual(before, self.identity())

    def test_invalid_base_and_submodules_fail(self):
        with self.assertRaises(ValueError):
            candidate.fingerprint(self.repo, "missing-base")
        self.git("update-index", "--add", "--cacheinfo", "160000," + self.base + ",nested")
        with self.assertRaisesRegex(ValueError, "Submodules"):
            self.identity()

    def test_skill_copies_match(self):
        self.assertEqual(HELPER.read_bytes(), (ROOT / "skills/verify/scripts/candidate.py").read_bytes())
        self.assertEqual(
            (ROOT / "skills/rdd/references/candidate.md").read_bytes(),
            (ROOT / "skills/verify/references/candidate.md").read_bytes(),
        )


if __name__ == "__main__":
    unittest.main()
