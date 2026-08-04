"""
Tests for Weeks 06 to 10 Lessons (Control Flow, Loops, Functions, File I/O, Built-In Functions)
"""
import unittest
import py_compile
from functools import reduce
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
LESSONS_DIR = BASE_DIR / "Lessons"


class TestWeek06To10(unittest.TestCase):

    def test_week_lessons_syntax(self):
        for week in ["Week 06", "Week 07", "Week 08", "Week 09", "Week 10"]:
            target_dir = LESSONS_DIR / week
            self.assertTrue(target_dir.exists(), f"{week} directory missing!")
            python_files = list(target_dir.glob("*.py"))
            self.assertGreater(len(python_files), 0, f"No python files in {week}")

            for py_file in python_files:
                try:
                    py_compile.compile(str(py_file), doraise=True)
                except py_compile.PyCompileError as e:
                    self.fail(f"Syntax error in lesson file {py_file.name}: {e}")

    def test_functions_args_kwargs(self):
        def show_skills(name, *skills, **details):
            return {
                "name": name,
                "skills": list(skills),
                "details": details
            }

        res = show_skills("Developer", "Python", "SQL", age=25, country="Egypt")
        self.assertEqual(res["name"], "Developer")
        self.assertEqual(res["skills"], ["Python", "SQL"])
        self.assertEqual(res["details"]["country"], "Egypt")

    def test_map_filter_reduce(self):
        nums = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x * x, nums))
        self.assertEqual(squared, [1, 4, 9, 16, 25])

        evens = list(filter(lambda x: x % 2 == 0, nums))
        self.assertEqual(evens, [2, 4])

        total = reduce(lambda x, y: x + y, nums)
        self.assertEqual(total, 15)


if __name__ == "__main__":
    unittest.main()
