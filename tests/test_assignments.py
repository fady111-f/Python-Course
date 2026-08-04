"""
Tests for Assignments across all weeks
"""
import unittest
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
ASSIGNMENTS_DIR = BASE_DIR / "Assignments"


class TestAssignments(unittest.TestCase):

    def test_assignments_exist(self):
        self.assertTrue(ASSIGNMENTS_DIR.exists())
        assignment_folders = list(ASSIGNMENTS_DIR.glob("Assignments From *"))
        self.assertGreaterEqual(len(assignment_folders), 20, f"Expected 20+ assignment folders, found {len(assignment_folders)}")

    def test_assignment_files_valid_syntax(self):
        assignment_files = list(ASSIGNMENTS_DIR.glob("**/*.py"))
        self.assertGreater(len(assignment_files), 100, f"Expected 100+ assignment files, found {len(assignment_files)}")

        for py_file in assignment_files:
            res = subprocess.run([sys.executable, "-m", "py_compile", str(py_file)], capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, f"Syntax error in assignment {py_file.name}: {res.stderr}")


if __name__ == "__main__":
    unittest.main()
