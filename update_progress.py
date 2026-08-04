"""
🔄 Automated Course Progress Sync Script
=========================================
Scans the repository structure, counts completed lessons & assignments,
and updates README.md & dashboard/index.html automatically.

Usage:
    python update_progress.py
"""

import os
import re
import sys

# ===== UTF-8 Terminal Support =====
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
LESSONS_DIR = os.path.join(REPO_ROOT, "Lessons")
ASSIGNMENTS_DIR = os.path.join(REPO_ROOT, "Assignments")
README_PATH = os.path.join(REPO_ROOT, "README.md")
DASHBOARD_PATH = os.path.join(REPO_ROOT, "dashboard", "index.html")

TOTAL_VIDEOS = 152
TOTAL_WEEKS = 19
TOTAL_ASSIGNMENTS = 113


def scan_lessons():
    """Scan the Lessons directory for completed scripts."""
    total_found = 0
    weeks_count = 0
    if os.path.exists(LESSONS_DIR):
        for item in sorted(os.listdir(LESSONS_DIR)):
            item_path = os.path.join(LESSONS_DIR, item)
            if os.path.isdir(item_path) and item.startswith("Week"):
                weeks_count += 1
                files = [f for f in os.listdir(item_path) if f.endswith(".py")]
                total_found += len(files)
    return total_found, weeks_count


def scan_assignments():
    """Scan the Assignments directory for solved assignment files."""
    solved_count = 0
    if os.path.exists(ASSIGNMENTS_DIR):
        for item in os.listdir(ASSIGNMENTS_DIR):
            item_path = os.path.join(ASSIGNMENTS_DIR, item)
            if os.path.isdir(item_path):
                files = [f for f in os.listdir(item_path) if f.endswith(".py")]
                solved_count += len(files)
    return solved_count


def run_sync():
    """Execute the progress sync across README and dashboard."""
    print("=" * 55)
    print(" 🔄 SCANNING COURSE PROGRESS")
    print("=" * 55)

    lessons_found, weeks_found = scan_lessons()
    assignments_solved = scan_assignments()

    # Note: user is currently at video 15, week 02 in progress
    # Adjust watched count to user's actual progress
    watched_videos = 15
    completed_weeks = 2

    video_pct = round((watched_videos / TOTAL_VIDEOS) * 100)
    week_pct = round((completed_weeks / TOTAL_WEEKS) * 100)
    assignment_pct = round((assignments_solved / TOTAL_ASSIGNMENTS) * 100)

    print(f"  • Videos Watched   : {watched_videos} / {TOTAL_VIDEOS} ({video_pct}%)")
    print(f"  • Lessons Available : {lessons_found} scripts in repository")
    print(f"  • Study Plan       : {completed_weeks} / {TOTAL_WEEKS} Weeks ({week_pct}%)")
    print(f"  • Solved Exercises : {assignments_solved} / {TOTAL_ASSIGNMENTS} ({assignment_pct}%)")
    print("=" * 55)

    # ===== Update README.md =====
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        # Update assignment badge
        content = re.sub(
            r'Assignments-\d+%2F113%20Solved-[A-Z0-9]+',
            f'Assignments-{assignments_solved}%2F113%20Solved-{"00C853" if assignments_solved > 0 else "FF9800"}',
            content
        )

        # Update progress bars in table
        content = re.sub(
            r'title=Completed&width=200\)\s*\|\s*\d+\s*/\s*19',
            f'title=Completed&width=200) | {completed_weeks} / 19',
            content
        )
        content = re.sub(
            r'title=Watched&width=200\)\s*\|\s*\d+\s*/\s*152',
            f'title=Watched&width=200) | {watched_videos} / 152',
            content
        )
        content = re.sub(
            r'title=Solved&width=200\)\s*\|\s*\d+\s*/\s*113',
            f'title=Solved&width=200) | {assignments_solved} / 113',
            content
        )

        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(content)

        print("  ✅ README.md updated successfully.")

    # ===== Update dashboard/index.html =====
    if os.path.exists(DASHBOARD_PATH):
        with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
            dash = f.read()

        dash = re.sub(r'data-percent="\d+"', f'data-percent="{video_pct}"', dash, count=1)
        dash = re.sub(r'data-target="\d+"', f'data-target="{video_pct}"', dash, count=1)
        dash = re.sub(r'\d+ / 152 Videos', f'{watched_videos} / 152 Videos', dash)
        dash = re.sub(r'\d+ / 113 Solved', f'{assignments_solved} / 113 Solved', dash)

        with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
            f.write(dash)

        print("  ✅ dashboard/index.html updated successfully.")

    print("\n🎉 Course progress sync complete!")


if __name__ == "__main__":
    run_sync()
