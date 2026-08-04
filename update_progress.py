"""
🔄 Automated Course Progress Sync Script
=========================================
Scans the repository structure, counts completed lessons & assignments,
and updates README.md & dashboard files automatically.

Usage:
    python update_progress.py
    python update_progress.py --videos 20 --weeks 3 --assignments 5
"""

import os
import re
import sys
import argparse

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


def run_sync(watched_videos=15, completed_weeks=2, assignments_solved=0):
    """Execute the progress sync across README and dashboard."""
    print("=" * 55)
    print(" 🔄 UPDATING COURSE PROGRESS")
    print("=" * 55)

    lessons_found, weeks_found = scan_lessons()

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

        # Update lesson completed status in JS array for videos watched
        for v in range(1, watched_videos + 1):
            num_str = f"{v:03d}"
            dash = re.sub(
                rf'\{{ num: "{num_str}", name: "([^"]+)", done: false \}}',
                f'{{ num: "{num_str}", name: "\\1", done: true }}',
                dash
            )

        with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
            f.write(dash)

        # Sync to docs/dashboard/index.html for static site build
        docs_dash = os.path.join(REPO_ROOT, "docs", "dashboard", "index.html")
        os.makedirs(os.path.dirname(docs_dash), exist_ok=True)
        with open(docs_dash, "w", encoding="utf-8") as f:
            f.write(dash)

        print("  ✅ dashboard/index.html & docs/dashboard/index.html updated successfully.")

    print("\n🎉 Course progress sync complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update course progress metrics.")
    parser.add_argument("--videos", type=int, default=15, help="Number of videos watched (out of 152)")
    parser.add_argument("--weeks", type=int, default=2, help="Number of weeks completed (out of 19)")
    parser.add_argument("--assignments", type=int, default=0, help="Number of assignments solved (out of 113)")

    args = parser.parse_args()
    run_sync(watched_videos=args.videos, completed_weeks=args.weeks, assignments_solved=args.assignments)
