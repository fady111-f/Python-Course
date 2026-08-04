"""
Tests for Weeks 11 to 15 Lessons (Decorators, Regex, OOP, SQLite Database)
"""
import unittest
import py_compile
import sqlite3
import re
import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
LESSONS_DIR = BASE_DIR / "Lessons"


class TestWeek11To15(unittest.TestCase):

    def test_week_lessons_syntax(self):
        for week in ["Week 11", "Week 12", "Week 13", "Week 14", "Week 15"]:
            target_dir = LESSONS_DIR / week
            self.assertTrue(target_dir.exists(), f"{week} directory missing!")
            python_files = list(target_dir.glob("*.py"))
            self.assertGreater(len(python_files), 0, f"No python files in {week}")

            for py_file in python_files:
                try:
                    py_compile.compile(str(py_file), doraise=True)
                except py_compile.PyCompileError as e:
                    self.fail(f"Syntax error in lesson file {py_file.name}: {e}")

    def test_decorators_and_generators(self):
        def my_gen():
            yield 1
            yield 2
            yield 3

        gen = my_gen()
        self.assertEqual(next(gen), 1)
        self.assertEqual(list(gen), [2, 3])

        def my_decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs).upper()
            return wrapper

        @my_decorator
        def greet(name):
            return f"hello {name}"

        self.assertEqual(greet("world"), "HELLO WORLD")

    def test_regular_expressions(self):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        self.assertIsNotNone(re.match(email_pattern, "user@example.com"))
        self.assertIsNone(re.match(email_pattern, "invalid-email"))

    def test_oop_principles(self):
        class Member:
            def __init__(self, name, age):
                self.name = name
                self._age = age

            @property
            def age(self):
                return self._age

            def get_role(self):
                return "Member"

        class Admin(Member):
            def get_role(self):
                return "Admin"

        m = Member("Alice", 25)
        a = Admin("Bob", 30)

        self.assertEqual(m.name, "Alice")
        self.assertEqual(m.age, 25)
        self.assertEqual(m.get_role(), "Member")
        self.assertEqual(a.get_role(), "Admin")

    def test_sqlite_database_operations(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_file = Path(tmp_dir) / "test_app.db"
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, skill TEXT)")
            cursor.execute("INSERT INTO users (name, skill) VALUES (?, ?)", ("Alice", "Python"))
            cursor.execute("INSERT INTO users (name, skill) VALUES (?, ?)", ("Bob", "SQLite"))
            conn.commit()

            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0][1], "Alice")

            cursor.execute("UPDATE users SET skill = ? WHERE name = ?", ("Python & Data", "Alice"))
            conn.commit()

            cursor.execute("SELECT skill FROM users WHERE name = ?", ("Alice",))
            self.assertEqual(cursor.fetchone()[0], "Python & Data")

            conn.close()


if __name__ == "__main__":
    unittest.main()
