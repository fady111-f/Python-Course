#!/usr/bin/env python3
"""
Python Course Mastery - Interactive CLI & Course Runner
--------------------------------------------------------
An interactive terminal dashboard and automated tool for exploring lessons,
running exercises, taking topic quizzes, and verifying solution progress.
"""

import sys
import os
import glob
import subprocess
import argparse
from pathlib import Path

# Ensure UTF-8 output encoding on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


BASE_DIR = Path(__file__).parent.resolve()
LESSONS_DIR = BASE_DIR / "Lessons"
ASSIGNMENTS_DIR = BASE_DIR / "Assignments"

QUIZZES = {
    "week01": [
        {
            "question": "Which operator or symbol is used for comments in Python?",
            "options": ["//", "/* */", "#", "--"],
            "answer": 2
        },
        {
            "question": "What is the output of print(type(10))?",
            "options": ["<class 'float'>", "<class 'int'>", "<class 'str'>", "<class 'number'>"],
            "answer": 1
        }
    ],
    "week02": [
        {
            "question": "Which string method converts the first character to uppercase and rest to lowercase?",
            "options": ["upper()", "capitalize()", "title()", "swapcase()"],
            "answer": 1
        },
        {
            "question": "What does 'Python'[1:4] return?",
            "options": ["Pyt", "ytho", "yth", "Pyt"],
            "answer": 2
        }
    ],
    "week03": [
        {
            "question": "Are Python lists mutable?",
            "options": ["Yes", "No"],
            "answer": 0
        },
        {
            "question": "Which collection type is immutable?",
            "options": ["List", "Dictionary", "Set", "Tuple"],
            "answer": 3
        }
    ],
    "week04": [
        {
            "question": "Which of the following creates an empty set in Python?",
            "options": ["{}", "set()", "[]", "()"],
            "answer": 1
        },
        {
            "question": "How do you access a dictionary value safely without raising a KeyError?",
            "options": ["dict.fetch(key)", "dict.get(key)", "dict.read(key)", "dict[key]"],
            "answer": 1
        }
    ],
    "week08": [
        {
            "question": "What does *args pack function arguments into?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": 1
        },
        {
            "question": "What does **kwargs pack function arguments into?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": 2
        }
    ],
    "week14": [
        {
            "question": "Which method is the constructor in a Python class?",
            "options": ["__construct__", "__init__", "__new__", "self()"],
            "answer": 1
        },
        {
            "question": "How do you create an abstract base class in Python?",
            "options": ["from abc import ABC", "class Abstract", "import interface", "using @abstract"],
            "answer": 0
        }
    ]
}


def print_banner():
    print("=" * 65)
    print(" 🚀 PYTHON COURSE MASTERY PLATFORM - ELZERO STUDY SUITE")
    print("=" * 65)


def list_weeks():
    print_banner()
    print("\n📚 COURSE LESSONS MAP:\n")
    if not LESSONS_DIR.exists():
        print("❌ Lessons directory not found!")
        return

    weeks = sorted([d for d in LESSONS_DIR.iterdir() if d.is_dir()])
    for week in weeks:
        lessons = sorted(list(week.glob("*.py")))
        print(f" 📂 {week.name} ({len(lessons)} lessons)")
        for lesson in lessons[:3]:
            print(f"    ├─ 📄 {lesson.name}")
        if len(lessons) > 3:
            print(f"    └─ ... and {len(lessons) - 3} more lessons")
        print()


def show_status():
    print_banner()
    print("\n📊 PROGRESS METRICS DASHBOARD:\n")

    # Run progress sync first to update metrics
    try:
        from update_progress import run_sync, README_PATH
        run_sync()
    except Exception:
        pass

    # Read synced README
    readme = Path(__file__).parent / "README.md"
    watched_videos = 0
    completed_weeks = 0
    completed_topics = 0
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        import re
        parts = re.split(r'## 📝 Assignments', text)
        lessons_sec = parts[0]
        assign_sec = parts[1] if len(parts) > 1 else ""
        
        completed_videos = len(re.findall(r'\|\s*\d+\s*\|\s*✅\s*\|', lessons_sec))
        completed_weeks = len(re.findall(r'<summary><strong>Week \d+</strong>[^\(]+\(\d+ lessons\) ✅ Completed</summary>', lessons_sec))
        completed_topics = re.findall(r'\|\s*(✅|⬜)\s*\|.*?\|.*?\|.*?\|', assign_sec).count('✅')
    else:
        completed_videos = 0

    total_videos = 152
    total_weeks = 19
    total_topics = 24
    total_lessons = len(list(LESSONS_DIR.glob("Week */*.py"))) if LESSONS_DIR.exists() else 0

    video_pct = round((completed_videos / total_videos) * 100)
    week_pct = round((completed_weeks / total_weeks) * 100)
    topic_pct = round((completed_topics / total_topics) * 100)

    print(f"  • Videos Watched     : {completed_videos} / {total_videos} Videos ({video_pct}%)")
    print(f"  • Study Plan         : {completed_weeks} / {total_weeks} Weeks ({week_pct}%)")
    print(f"  • Video Lesson Files : {total_lessons} Python Scripts in Repo")
    print(f"  • Quiz Modules       : {len(QUIZZES)} Topic Quizzes Ready")
    print(f"  • Solved Topics      : {completed_topics} / {total_topics} Topics ({topic_pct}%)")

    bar_filled = int(video_pct / 5)
    bar_empty = 20 - bar_filled
    print(f"\n  Progress: [{'=' * bar_filled}{'.' * bar_empty}] {video_pct}% Videos Watched")
    print("=" * 65)


def run_lesson(lesson_query: str):
    print_banner()
    files = list(LESSONS_DIR.glob(f"**/*{lesson_query}*.py"))
    if not files:
        print(f"❌ No lesson matching '{lesson_query}' found!")
        return

    target = files[0]
    print(f"\n▶ Executing: {target.relative_to(BASE_DIR)}\n" + "-" * 50)
    try:
        res = subprocess.run([sys.executable, str(target)], capture_output=True, text=True, timeout=10)
        if res.stdout:
            print("STDOUT:")
            print(res.stdout)
        if res.stderr:
            print("STDERR:")
            print(res.stderr)
        print("-" * 50)
        print(f"✅ Execution finished with exit code {res.returncode}")
    except Exception as e:
        print(f"❌ Execution error: {e}")


def run_quiz(week_name: str = None):
    print_banner()
    if not week_name or week_name not in QUIZZES:
        available = ", ".join(QUIZZES.keys())
        print(f"\n💡 Available Quizzes: {available}")
        week_name = input("Enter quiz module (e.g. week01): ").strip().lower()

    if week_name not in QUIZZES:
        print(f"❌ Quiz '{week_name}' not found!")
        return

    questions = QUIZZES[week_name]
    score = 0
    print(f"\n🧠 KNOWLEDGE QUIZ: {week_name.upper()}\n" + "-" * 50)

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"   {idx + 1}) {opt}")
        
        try:
            user_choice = int(input("\nYour choice (number): ")) - 1
            if user_choice == q['answer']:
                print("✨ Correct!")
                score += 1
            else:
                correct_str = q['options'][q['answer']]
                print(f"❌ Incorrect. Correct answer: {correct_str}")
        except ValueError:
            print("❌ Invalid input!")

    print("\n" + "=" * 50)
    print(f"🏆 Quiz Finished! Score: {score}/{len(questions)}")
    print("=" * 50)


def run_tests():
    print_banner()
    print("\n🧪 RUNNING AUTOMATED TEST SUITE...\n")
    
    # Try pytest first if installed, else fallback to unittest
    try:
        import pytest
        cmd = [sys.executable, "-m", "pytest", "tests/", "-v"]
    except ImportError:
        cmd = [sys.executable, "-m", "unittest", "discover", "tests"]
        
    try:
        res = subprocess.run(cmd, cwd=str(BASE_DIR))
        sys.exit(res.returncode)
    except Exception as e:
        print(f"❌ Error running tests: {e}")



def interactive_menu():
    while True:
        print_banner()
        print("\nSelect an action:")
        print("  1) 📚 List All Weeks & Lessons")
        print("  2) 📊 View Learning Dashboard")
        print("  3) ▶ Run a Lesson Script")
        print("  4) 🧠 Take a Knowledge Quiz")
        print("  5) 🧪 Run Automated Pytest Suite")
        print("  0) ❌ Exit")

        choice = input("\nEnter option (0-5): ").strip()
        if choice == "1":
            list_weeks()
        elif choice == "2":
            show_status()
        elif choice == "3":
            query = input("Enter lesson number/name (e.g., 004 or OOP): ").strip()
            run_lesson(query)
        elif choice == "4":
            run_quiz()
        elif choice == "5":
            run_tests()
        elif choice == "0":
            print("\nGoodbye & Happy Coding! 🐍✨\n")
            break
        else:
            print("❌ Invalid option, try again.")
        
        input("\nPress Enter to return to menu...")


def main():
    parser = argparse.ArgumentParser(description="Python Course Mastery CLI Dashboard")
    parser.add_argument("--list-weeks", action="store_true", help="List all study weeks and lessons")
    parser.add_argument("--status", action="store_true", help="Show learning progress dashboard")
    parser.add_argument("--run-lesson", type=str, help="Run a specific lesson by number or name")
    parser.add_argument("--quiz", type=str, help="Run quiz for a given week (e.g. week01, week14)")
    parser.add_argument("--test-all", action="store_true", help="Run automated test suite")

    args = parser.parse_args()

    if args.list_weeks:
        list_weeks()
    elif args.status:
        show_status()
    elif args.run_lesson:
        run_lesson(args.run_lesson)
    elif args.quiz:
        run_quiz(args.quiz)
    elif args.test_all:
        run_tests()
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
