"""
🔄 Smart Course Progress Sync Script
=========================================
Scans README.md for ✅ checkboxes, calculates progress metrics,
and updates README.md headers & dashboard files automatically.
"""

import os
import re
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(REPO_ROOT, "README.md")
DASHBOARD_PATH = os.path.join(REPO_ROOT, "dashboard", "index.html")
DOCS_DASHBOARD_PATH = os.path.join(REPO_ROOT, "docs", "dashboard", "index.html")

TOTAL_VIDEOS = 152
TOTAL_WEEKS = 19
TOTAL_TOPICS = 24

def run_sync():
    print("=" * 55)
    print(" 🔄 SMART UPDATING COURSE PROGRESS FROM README CHECKBOXES")
    print("=" * 55)

    if not os.path.exists(README_PATH):
        print("❌ README.md not found.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into sections
    parts = re.split(r'## 📝 Assignments', content)
    lessons_section = parts[0]
    assignments_section = parts[1] if len(parts) > 1 else ""

    # Parse completed lessons
    completed_lessons = []
    total_found_lessons = 0
    lesson_matches = re.finditer(r'\|\s*(\d+)\s*\|\s*(✅|⬜)\s*\|', lessons_section)
    for match in lesson_matches:
        num = match.group(1)
        status = match.group(2)
        total_found_lessons += 1
        if status == '✅':
            completed_lessons.append(num)
            
    watched_videos = len(completed_lessons)

    # Analyze Weeks
    weeks_count = 0
    completed_weeks = 0
    
    # We will modify the lessons section string to update week summaries
    new_lessons_section = lessons_section
    week_blocks = list(re.finditer(r'(<summary><strong>Week (\d+)</strong>.*?)</details>', lessons_section, re.DOTALL))
    
    for block in week_blocks:
        weeks_count += 1
        block_content = block.group(0)
        
        # Count checkboxes in this week
        week_lessons = re.findall(r'\|\s*\d+\s*\|\s*(✅|⬜)\s*\|', block_content)
        total_week = len(week_lessons)
        done_week = week_lessons.count('✅')
        
        # Determine status
        if done_week == 0:
            status_text = "⬜ Not Started"
        elif done_week == total_week and total_week > 0:
            status_text = "✅ Completed"
            completed_weeks += 1
        else:
            status_text = "🔄 In Progress"
            
        # Replace the summary line
        # Match something like: <summary><strong>Week 01</strong> — Intro (10 lessons) ✅ Completed</summary>
        summary_pattern = r'(<summary><strong>Week \d+</strong>[^\(]+\(\d+ lessons\))[^<]*(</summary>)'
        new_block = re.sub(summary_pattern, rf'\g<1> {status_text}\g<2>', block_content)
        
        new_lessons_section = new_lessons_section.replace(block_content, new_block)

    # Parse Assignments
    completed_topics = 0
    if assignments_section:
        topic_matches = re.findall(r'\|\s*(✅|⬜)\s*\|.*?\|.*?\|.*?\|', assignments_section)
        completed_topics = topic_matches.count('✅')

    # Calculate percentages
    video_pct = round((watched_videos / TOTAL_VIDEOS) * 100) if TOTAL_VIDEOS else 0
    week_pct = round((completed_weeks / TOTAL_WEEKS) * 100) if TOTAL_WEEKS else 0
    assignment_pct = round((completed_topics / TOTAL_TOPICS) * 100) if TOTAL_TOPICS else 0

    print(f"  • Videos Watched   : {watched_videos} / {TOTAL_VIDEOS} ({video_pct}%)")
    print(f"  • Study Plan       : {completed_weeks} / {TOTAL_WEEKS} Weeks ({week_pct}%)")
    print(f"  • Solved Topics    : {completed_topics} / {TOTAL_TOPICS} ({assignment_pct}%)")
    print("=" * 55)

    # Reconstruct content
    content = new_lessons_section
    if len(parts) > 1:
        content += "## 📝 Assignments" + assignments_section

    # Update assignment badge
    content = re.sub(
        r'Assignments-\d+%2F(?:113|24)%20(?:Solved|Topics)-[A-Z0-9]+',
        f'Assignments-{completed_topics}%2F24%20Topics-{"00C853" if completed_topics > 0 else "FF9800"}',
        content
    )

    # Update text below Assignments heading
    content = re.sub(
        r'\*\*\d+ / (?:113|24)\*\*(?:\s*assignments\s*solved|\s*topics\s*completed)',
        f'**{completed_topics} / 24** topics completed',
        content, flags=re.IGNORECASE
    )

    # Update progress bars in table with accurate percentages
    # Weeks
    content = re.sub(
        r'!\[\d+%\]\(https://progress-bar\.dev/\d+/\?title=Completed&width=200\)\s*\|\s*\d+\s*/\s*19',
        f'![{week_pct}%](https://progress-bar.dev/{week_pct}/?title=Completed&width=200) | {completed_weeks} / 19',
        content
    )
    # Videos
    content = re.sub(
        r'!\[\d+%\]\(https://progress-bar\.dev/\d+/\?title=Watched&width=200\)\s*\|\s*\d+\s*/\s*152',
        f'![{video_pct}%](https://progress-bar.dev/{video_pct}/?title=Watched&width=200) | {watched_videos} / 152',
        content
    )
    # Assignments (Topics)
    content = re.sub(
        r'!\[\d+%\]\(https://progress-bar\.dev/\d+/\?title=Solved&width=200\)\s*\|\s*\d+\s*/\s*(?:113|24)',
        f'![{assignment_pct}%](https://progress-bar.dev/{assignment_pct}/?title=Solved&width=200) | {completed_topics} / 24',
        content
    )
    
    # Text replacements to handle 113 to 24 in table rows if they haven't been changed yet
    content = re.sub(r'\|\s*\d+\s*/\s*113\s*(Exercises|Solved)\s*\|', f'| {completed_topics} / 24 Topics |', content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("  ✅ README.md updated successfully.")

    # ===== Update dashboard/index.html =====
    if os.path.exists(DASHBOARD_PATH):
        with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
            dash = f.read()

        # --- Update stat card ring percentages ---
        # Videos ring (first data-percent and data-target)
        rings = list(re.finditer(r'data-percent="\d+"', dash))
        targets = list(re.finditer(r'data-target="\d+"', dash))
        pcts = [video_pct, week_pct, assignment_pct]
        for i, pct in enumerate(pcts):
            if i < len(rings):
                dash = dash[:rings[i].start()] + f'data-percent="{pct}"' + dash[rings[i].end():]
                # Recalculate positions after replacement
                rings = list(re.finditer(r'data-percent="\d+"', dash))
            if i < len(targets):
                targets = list(re.finditer(r'data-target="\d+"', dash))
                if i < len(targets):
                    dash = dash[:targets[i].start()] + f'data-target="{pct}"' + dash[targets[i].end():]

        # --- Update text details ---
        dash = re.sub(r'\d+ / 152 Videos', f'{watched_videos} / 152 Videos', dash)
        dash = re.sub(r'\d+ / 19 Weeks', f'{completed_weeks} / 19 Weeks', dash)
        dash = re.sub(r'\d+ / 24 Topics', f'{completed_topics} / 24 Topics', dash)
        dash = re.sub(r'\d+ / 113 Solved', f'{completed_topics} / 24 Topics', dash)

        # --- Update mini bar widths ---
        dash = re.sub(
            r'(stat-card__mini-fill--blue[^>]*style=")width:\s*\d+%',
            f'\\1width: {video_pct}%', dash
        )
        dash = re.sub(
            r'(stat-card__mini-fill--green[^>]*style=")width:\s*\d+%',
            f'\\1width: {week_pct}%', dash
        )
        dash = re.sub(
            r'(stat-card__mini-fill--orange[^>]*style=")width:\s*\d+%',
            f'\\1width: {assignment_pct}%', dash
        )

        # --- Update lesson completed status in JS array ---
        dash = re.sub(r'done:\s*true', 'done: false', dash)
        for num_str in completed_lessons:
            dash = re.sub(
                rf'\{{\s*num:\s*"{num_str}",\s*name:\s*"([^"]+)",\s*done:\s*false\s*\}}',
                f'{{ num: "{num_str}", name: "\\1", done: true }}',
                dash
            )

        # --- Update week statuses in dashboard JS array ---
        for block in week_blocks:
            week_match = re.search(r'<summary><strong>Week (\d+)</strong>', block.group(0))
            if week_match:
                week_num = week_match.group(1)
                week_lessons = re.findall(r'\|\s*\d+\s*\|\s*(✅|⬜)\s*\|', block.group(0))
                done = week_lessons.count('✅')
                tot = len(week_lessons)
                if done == 0: dash_status = 'pending'
                elif done == tot and tot > 0: dash_status = 'done'
                else: dash_status = 'progress'

                dash = re.sub(
                    rf'\{{\s*num:\s*"{week_num}",\s*title:\s*"([^"]+)",\s*status:\s*"[^"]+"',
                    f'{{ num: "{week_num}", title: "\\1", status: "{dash_status}"',
                    dash
                )

        with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
            f.write(dash)

        os.makedirs(os.path.dirname(DOCS_DASHBOARD_PATH), exist_ok=True)
        with open(DOCS_DASHBOARD_PATH, "w", encoding="utf-8") as f:
            f.write(dash)

        print("  ✅ dashboard/index.html & docs/dashboard/index.html updated successfully.")

    print("\n🎉 Course progress sync complete!")

if __name__ == "__main__":
    run_sync()
