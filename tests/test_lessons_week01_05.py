"""
Tests for Weeks 01 to 05 Lessons (Fundamentals, Data Types, Strings, Collections, Operators)
"""
import unittest
import py_compile
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
LESSONS_DIR = BASE_DIR / "Lessons"


class TestWeek01To05(unittest.TestCase):

    def test_week_lessons_syntax(self):
        for week in ["Week 01", "Week 02", "Week 03", "Week 04", "Week 05"]:
            target_dir = LESSONS_DIR / week
            self.assertTrue(target_dir.exists(), f"{week} directory missing!")
            python_files = list(target_dir.glob("*.py"))
            self.assertGreater(len(python_files), 0, f"No python files in {week}")

            for py_file in python_files:
                try:
                    py_compile.compile(str(py_file), doraise=True)
                except py_compile.PyCompileError as e:
                    self.fail(f"Syntax error in lesson file {py_file.name}: {e}")

    def test_string_manipulation_concepts(self):
        text = "Elzero Web School"
        self.assertEqual(text[0:6], "Elzero")
        self.assertEqual(text.upper(), "ELZERO WEB SCHOOL")
        self.assertEqual(text.lower(), "elzero web school")
        self.assertIn("Web", text)

    def test_collections_concepts(self):
        my_list = [1, 2, 3]
        my_list.append(4)
        self.assertEqual(len(my_list), 4)

        my_tuple = (10, 20, 30)
        self.assertEqual(my_tuple[0], 10)

        my_set = {1, 2, 2, 3}
        self.assertEqual(len(my_set), 3)

        my_dict = {"name": "Python", "version": 3}
        self.assertEqual(my_dict.get("name"), "Python")
        self.assertEqual(my_dict.get("missing", "default"), "default")


if __name__ == "__main__":
    unittest.main()
