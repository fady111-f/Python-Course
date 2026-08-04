# 📊 Web Dashboard

A beautiful, interactive progress dashboard for tracking your Python course journey.

---

## How to Open

Simply open the file in your browser:

```bash
# From the repository root
start dashboard/index.html     # Windows
open dashboard/index.html      # macOS
xdg-open dashboard/index.html  # Linux
```

Or double-click `dashboard/index.html` in your file explorer.

## Features

- 🎯 **Animated progress rings** for videos, study plan, and assignments
- 📚 **Collapsible week cards** showing all 15 weeks and their lessons
- ✅ **Per-lesson status** tracking (done / pending)
- ⚡ **Quick access links** to cheatsheets, projects, flashcards, and CLI
- 🌙 **Dark theme** with glassmorphism design
- 📱 **Fully responsive** — works on mobile and desktop
- ⚡ **Zero dependencies** — pure HTML/CSS/JS, no build step

## Updating Progress

To update your progress, edit the `weeks` array in `dashboard/index.html` and change `done: false` to `done: true` for completed lessons.
