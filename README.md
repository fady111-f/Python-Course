<p align="center">
  <img src="https://i.ibb.co/ggSVcwm/python.png" alt="Python Course" width="200" />
</p>

<h1 align="center">🐍 Python Mastery Platform</h1>

<p align="center">
  <strong>A comprehensive, interactive Python learning suite — from zero to hero.</strong>
  <br />
  Based on the <a href="https://elzero.org/study/mastering-python-study-plan/">Mastering Python</a> course by <a href="https://www.youtube.com/user/OsamaElzero">Osama Elzero</a>
</p>

<p align="center">
  <a href="https://fady111-f.github.io/Python-Course/">
    <img src="https://img.shields.io/badge/🌐%20Live%20Website-Open%20Docs%20Hub-7C3AED?style=for-the-badge&logo=github&logoColor=white" alt="Live Website" />
  </a>
  <a href="https://fady111-f.github.io/Python-Course/dashboard/">
    <img src="https://img.shields.io/badge/📊%20Live%20Dashboard-Open%20Progress%20Tracker-059669?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Live Dashboard" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/fady111-f/Python-Course/actions/workflows/python-ci.yml">
    <img src="https://github.com/fady111-f/Python-Course/actions/workflows/python-ci.yml/badge.svg" alt="CI Status" />
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?logo=python&logoColor=white" alt="Python Version" />
  </a>
  <a href="#-assignments">
    <img src="https://img.shields.io/badge/Assignments-0%2F113%20Solved-FF9800?logo=checkmarx&logoColor=white" alt="Assignments Solved" />
  </a>
  <a href="https://www.youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs">
    <img src="https://img.shields.io/badge/YouTube-152%20Videos-FF0000?logo=youtube&logoColor=white" alt="YouTube Playlist" />
  </a>
</p>

---

> ### 🌐 Live Hosted Links (No Terminal Required!)
> - 📚 **[Open Live Documentation Hub](https://fady111-f.github.io/Python-Course/)** — Full MkDocs Material course website with search & cheat sheets
> - 📊 **[Open Live Progress Dashboard](https://fady111-f.github.io/Python-Course/dashboard/)** — Interactive web dashboard with progress rings & lesson tracker

---

## 📋 Table of Contents

- [About](#-about)
- [Progress Dashboard](#-progress-dashboard)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Topics Covered](#-topics-covered)
- [Lessons](#-lessons)
- [Assignments](#-assignments)
- [Testing & CI](#-testing--ci)
- [Credits](#-credits)

---

## 🎯 About

This repository is more than just course notes — it's a **fully interactive Python learning platform** featuring:

- 🎥 **127 lesson scripts** with hands-on code examples across 15 study weeks
- 📝 **113 assignments** spanning 24 topic categories (solving in progress)
- 📋 **[Cheat Sheets](cheatsheets/01_fundamentals.md)** for quick syntax and method references
- 🚀 **[Mini Projects](projects/)** (1 project for every 5 videos watched)
- 🧠 **[Flashcard CLI](flashcards/flashcards.py)** for spaced-repetition studying
- 📊 **[Web Dashboard](dashboard/index.html)** with interactive progress rings
- 🧪 **Automated test suite** validating every script and concept
- 🖥️ **Interactive CLI dashboard** to explore lessons, take quizzes, and track progress
- ⚙️ **CI/CD pipeline** with multi-version Python testing & MkDocs site deployment via GitHub Actions

---

## 📊 Progress Dashboard

| Metric | Progress | Details |
| :--- | :--- | :--- |
| 📅 Study Plan | ![10%](https://progress-bar.dev/10/?title=Completed&width=200) | 2 / 19 Weeks |
| 🎥 Videos Watched | ![10%](https://progress-bar.dev/10/?title=Watched&width=200) | 15 / 152 Videos |
| 📝 Assignments | ![0%](https://progress-bar.dev/0/?title=Solved&width=200) | 0 / 113 Exercises |

> **Course**: [Mastering Python Study Plan](https://elzero.org/study/mastering-python-study-plan/) &nbsp;|&nbsp; **Playlist**: [YouTube (20h 25m)](https://www.youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs) &nbsp;|&nbsp; **Assignments**: [Elzero Assignments](https://elzero.org/category/assignments/python-assignments/)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/fady111-f/Python-Course.git
cd Python-Course

# 🌐 Launch Live Web App & Dashboard (http://localhost:8000)
python server.py

# 🖥️ Launch Interactive Terminal CLI
python course_runner.py

# 🧠 Launch Flashcard System
python flashcards/flashcards.py
```

### Quick Commands

| Command | Description |
| :--- | :--- |
| `python server.py` | 🌐 Launch local web server (Web Dashboard + Docs Site) |
| `python course_runner.py` | 🖥️ Open terminal CLI menu (Lessons, Quizzes, Progress) |
| `python flashcards/flashcards.py` | 🧠 Launch interactive flashcard spaced-repetition tool |
| `python update_progress.py` | 🔄 Auto-sync progress metrics across README & Dashboard |
| `python -m unittest discover tests` | 🧪 Run full automated test suite |

### Example Terminal Output

```
=================================================================
 🚀 PYTHON COURSE MASTERY PLATFORM - ELZERO STUDY SUITE
=================================================================

📊 PROGRESS METRICS DASHBOARD:

  • Total Study Weeks  : 15 / 15 Weeks Completed
  • Video Lesson Files : 128 Python Scripts
  • Solved Assignments : 109 Exercise Files
  • Quiz Modules       : 6 Topic Quizzes Ready

  [========================================] 100% Solved Assignments!
=================================================================
```

---

## 📁 Project Structure

```
Python-Course/
├── 📄 README.md                 # This file
├── 📄 course_runner.py          # Interactive CLI & course dashboard
├── 📄 pyproject.toml            # Python project configuration
├── 📄 .gitignore                # Git ignore rules
│
├── 📂 Lessons/                  # 127 lesson scripts organized by week
│   ├── Week 01/                 #   Introduction, Variables, Data Types
│   ├── Week 02/                 #   Strings & String Methods
│   ├── Week 03/                 #   Numbers, Lists, Tuples
│   ├── Week 04/                 #   Sets & Dictionaries
│   ├── Week 05/                 #   Operators, Type Conversion, User Input
│   ├── Week 06/                 #   Control Flow (if/elif/else)
│   ├── Week 07/                 #   Loops (while, for, nested, break/continue)
│   ├── Week 08/                 #   Functions, *args, **kwargs, Recursion, Lambda
│   ├── Week 09/                 #   File Handling (Read, Write, Append)
│   ├── Week 10/                 #   Built-in Functions (map, filter, reduce)
│   ├── Week 11/                 #   Modules, Date/Time, Iterators, Generators, Decorators
│   ├── Week 12/                 #   Zip, Pillow, Docstrings, Error Handling, Debugging
│   ├── Week 13/                 #   Regular Expressions (re module)
│   ├── Week 14/                 #   OOP (Classes, Inheritance, Polymorphism, ABCs)
│   └── Week 15/                 #   SQLite Database (CRUD, Skills App Project)
│
├── 📂 Assignments/              # 113 assignment exercises (in progress)
│   ├── Assignments From [ 001 ] To [ 010 ]/
│   ├── ...                      #   24 topic folders total
│   └── Assignments From [ 117 ] To [ 127 ]/
│
├── 📂 tests/                    # Automated test suite
│   ├── conftest.py              #   Pytest configuration
│   ├── test_lessons_week01_05.py
│   ├── test_lessons_week06_10.py
│   ├── test_lessons_week11_15.py
│   └── test_assignments.py
│
└── 📂 .github/workflows/       # CI/CD pipeline
    └── python-ci.yml            #   Multi-version automated testing
```

---

## 📚 Topics Covered

<table>
  <thead>
    <tr>
      <th>Week</th>
      <th>Topics</th>
      <th>Key Concepts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>01</strong></td>
      <td>🟢 Fundamentals</td>
      <td>Syntax, Comments, Data Types, Variables, Escape Sequences, Concatenation</td>
    </tr>
    <tr>
      <td><strong>02</strong></td>
      <td>🟢 Strings</td>
      <td>Indexing, Slicing, String Methods, Old & New Formatting</td>
    </tr>
    <tr>
      <td><strong>03</strong></td>
      <td>🟡 Collections I</td>
      <td>Numbers, Arithmetic Operators, Lists, Tuples & Their Methods</td>
    </tr>
    <tr>
      <td><strong>04</strong></td>
      <td>🟡 Collections II</td>
      <td>Sets, Dictionaries & Their Methods</td>
    </tr>
    <tr>
      <td><strong>05</strong></td>
      <td>🟡 Operators & Input</td>
      <td>Boolean, Assignment, Comparison Operators, Type Conversion, User Input</td>
    </tr>
    <tr>
      <td><strong>06</strong></td>
      <td>🔵 Control Flow</td>
      <td>if / elif / else, Nested Conditions, Ternary Operator, Membership</td>
    </tr>
    <tr>
      <td><strong>07</strong></td>
      <td>🔵 Loops</td>
      <td>while, for, Nested Loops, break / continue / pass, Dictionary Looping</td>
    </tr>
    <tr>
      <td><strong>08</strong></td>
      <td>🟣 Functions</td>
      <td>Return, Parameters, *args, **kwargs, Scope, Recursion, Lambda</td>
    </tr>
    <tr>
      <td><strong>09</strong></td>
      <td>🟣 File Handling</td>
      <td>Open, Read, Write, Append, Context Managers</td>
    </tr>
    <tr>
      <td><strong>10</strong></td>
      <td>🟣 Built-in Functions</td>
      <td>map(), filter(), reduce(), enumerate(), zip()</td>
    </tr>
    <tr>
      <td><strong>11</strong></td>
      <td>🟠 Advanced Python</td>
      <td>Modules, Packages, Date & Time, Iterators, Generators, Decorators</td>
    </tr>
    <tr>
      <td><strong>12</strong></td>
      <td>🟠 Code Quality</td>
      <td>Zip Practical, Pillow, Docstrings, Pylint, Error Handling, Type Hinting</td>
    </tr>
    <tr>
      <td><strong>13</strong></td>
      <td>🔴 Regex</td>
      <td>Patterns, Quantifiers, Character Classes, Assertions, re Module</td>
    </tr>
    <tr>
      <td><strong>14</strong></td>
      <td>🔴 OOP</td>
      <td>Classes, Attributes, Methods, Inheritance, Polymorphism, Encapsulation, ABCs</td>
    </tr>
    <tr>
      <td><strong>15</strong></td>
      <td>🔴 Database</td>
      <td>SQLite, CRUD Operations, Building a Full Skills App</td>
    </tr>
  </tbody>
</table>

---

## 📖 Lessons

<details>
<summary><strong>Week 01</strong> — Introduction & Variables (10 lessons) ✅ Completed</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 001 | ✅ | [Introduction & What Is Python ?](Lessons/Week%2001/001%20-%20Introduction%20%26%20What%20Is%20Python.py) |
| 002 | ✅ | [What I Need ?](Lessons/Week%2001/002%20-%20What%20I%20Need.py) |
| 003 | ✅ | [Syntax & Your First App](Lessons/Week%2001/003%20-%20Syntax%20And%20Your%20First%20App.py) |
| 004 | ✅ | [Comments](Lessons/Week%2001/004%20-%20Comments.py) |
| 005 | ✅ | [Dealing With Data In Python](Lessons/Week%2001/005%20-%20Dealing%20With%20Data%20In%20Python.py) |
| 006 | ✅ | [Some Data Types Overview](Lessons/Week%2001/006%20-%20Some%20Data%20Types%20Overview.py) |
| 007 | ✅ | [Variables - Part 01](Lessons/Week%2001/007%20-%20Variables%20-%20Part%2001.py) |
| 008 | ✅ | [Variables - Part 02](Lessons/Week%2001/008%20-%20Variables%20-%20Part%2002.py) |
| 009 | ✅ | [Escape Sequences Characters](Lessons/Week%2001/009%20-%20Escape%20Sequences%20Characters.py) |
| 010 | ✅ | [Concatenation & Training](Lessons/Week%2001/010%20-%20Concatenation%20%26%20Training.py) |

</details>

<details>
<summary><strong>Week 02</strong> — Strings & Methods (8 lessons) 🔄 In Progress</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 011 | ✅ | [String](Lessons/Week%2002/011%20-%20String.py) |
| 012 | ✅ | [String - Indexing & Slicing](Lessons/Week%2002/012%20-%20String%20-%20Indexing%20%26%20Slicing.py) |
| 013 | ✅ | [String - Methods - Part 01](Lessons/Week%2002/013%20-%20String%20-%20Methods%20-%20Part%2001.py) |
| 014 | ✅ | [String - Methods - Part 02](Lessons/Week%2002/014%20-%20String%20-%20Methods%20-%20Part%2002.py) |
| 015 | ✅ | [String - Methods - Part 03](Lessons/Week%2002/015%20-%20String%20-%20Methods%20-%20Part%2003.py) |
| 016 | ✅ | [String - Methods - Part 04](Lessons/Week%2002/016%20-%20String%20-%20Methods%20-%20Part%2004.py) |
| 017 | ⬜ | [String - Formatting - Old Way](Lessons/Week%2002/017%20-%20String%20-%20Formatting%20-%20Old%20Way.py) |
| 018 | ⬜ | [String - Formatting - New Way](Lessons/Week%2002/018%20-%20String%20-%20Formatting%20-%20New%20Way.py) |

</details>

<details>
<summary><strong>Week 03</strong> — Numbers, Lists & Tuples (7 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 019 | ⬜ | [Numbers](Lessons/Week%2003/019%20-%20Numbers.py) |
| 020 | ⬜ | [Arithmetic Operators](Lessons/Week%2003/020%20-%20Arithmetic%20Operators.py) |
| 021 | ⬜ | [List](Lessons/Week%2003/021%20-%20List.py) |
| 022 | ⬜ | [List - Methods - Part 01](Lessons/Week%2003/022%20-%20List%20-%20Methods%20-%20Part%2001.py) |
| 023 | ⬜ | [List - Methods - Part 02](Lessons/Week%2003/023%20-%20List%20-%20Methods%20-%20Part%2002.py) |
| 024 | ⬜ | [Tuple - Methods - Part 01](Lessons/Week%2003/024%20-%20Tuple%20-%20Methods%20-%20Part%2001.py) |
| 025 | ⬜ | [Tuple - Methods - Part 02](Lessons/Week%2003/025%20-%20Tuple%20-%20Methods%20-%20Part%2002.py) |

</details>

<details>
<summary><strong>Week 04</strong> — Sets & Dictionaries (7 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 026 | ⬜ | [Set](Lessons/Week%2004/026%20-%20Set.py) |
| 027 | ⬜ | [Set - Methods - Part 01](Lessons/Week%2004/027%20-%20Set%20-%20Methods%20-%20Part%2001.py) |
| 028 | ⬜ | [Set - Methods - Part 02](Lessons/Week%2004/028%20-%20Set%20-%20Methods%20-%20Part%2002.py) |
| 029 | ⬜ | [Set - Methods - Part 03](Lessons/Week%2004/029%20-%20Set%20-%20Methods%20-%20Part%2003.py) |
| 030 | ⬜ | [Dictionary](Lessons/Week%2004/030%20-%20Dictionary.py) |
| 031 | ⬜ | [Dictionary - Methods - Part 01](Lessons/Week%2004/031%20-%20Dictionary%20-%20Methods%20-%20Part%2001.py) |
| 032 | ⬜ | [Dictionary - Methods - Part 02](Lessons/Week%2004/032%20-%20Dictionary%20-%20Methods%20-%20Part%2002.py) |

</details>

<details>
<summary><strong>Week 05</strong> — Operators, Input & Practice (8 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 033 | ⬜ | [Boolean](Lessons/Week%2005/033%20-%20Boolean.py) |
| 034 | ⬜ | [Boolean Operators](Lessons/Week%2005/034%20-%20Boolean%20Operators.py) |
| 035 | ⬜ | [Assignment Operators](Lessons/Week%2005/035%20-%20Assignment%20Operators.py) |
| 036 | ⬜ | [Comparison Operators](Lessons/Week%2005/036%20-%20Comparison%20Operators.py) |
| 037 | ⬜ | [Type Conversion](Lessons/Week%2005/037%20-%20Type%20Conversion.py) |
| 038 | ⬜ | [User Input](Lessons/Week%2005/038%20-%20User%20Input.py) |
| 039 | ⬜ | [Email Slice - Practical](Lessons/Week%2005/039%20-%20Email%20Slice%20-%20Practical.py) |
| 040 | ⬜ | [Your Age In Full Details - Practical](Lessons/Week%2005/040%20-%20Your%20Age%20In%20Full%20Details%20-%20Practical.py) |

</details>

<details>
<summary><strong>Week 06</strong> — Control Flow (6 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 041 | ⬜ | [Control Flow - If & Elif & Else](Lessons/Week%2006/041%20-%20Control%20Flow%20-%20Part%2001%20-%20If%20%26%20Elif%20%26%20Else.py) |
| 042 | ⬜ | [Nested If & Training](Lessons/Week%2006/042%20-%20Control%20Flow%20-%20Part%2002%20-%20Nested%20If%20%26%20Training.py) |
| 043 | ⬜ | [Ternary Conditional Operator](Lessons/Week%2006/043%20-%20Control%20Flow%20-%20Part%2003%20-%20Ternary%20Conditional%20Operator.py) |
| 044 | ⬜ | [Calculate Age Advanced Version & Training](Lessons/Week%2006/044%20-%20Calculate%20Age%20Advanced%20Version%20%26%20Training.py) |
| 045 | ⬜ | [Membership Operators](Lessons/Week%2006/045%20-%20Membership%20Operators.py) |
| 046 | ⬜ | [Membership Control - Practical](Lessons/Week%2006/046%20-%20Membership%20Control%20-%20Practical.py) |

</details>

<details>
<summary><strong>Week 07</strong> — Loops (9 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 047 | ⬜ | [While - Else](Lessons/Week%2007/047%20-%20Loop%20-%20Part%2001%20-%20While%20-%20Else.py) |
| 048 | ⬜ | [While - Printing Friends](Lessons/Week%2007/048%20-%20Loop%20-%20Part%2002%20-%20While%20-%20Training%20-%20Printing%20Friends.py) |
| 049 | ⬜ | [While - Bookmarks Manager](Lessons/Week%2007/049%20-%20Loop%20-%20Part%2003%20-%20While%20-%20Training%20-%20Bookmarks%20Manager.py) |
| 050 | ⬜ | [While - Password Checker](Lessons/Week%2007/050%20-%20Loop%20-%20Part%2004%20-%20While%20-%20Training%20-%20Password%20Checker.py) |
| 051 | ⬜ | [For - Else](Lessons/Week%2007/051%20-%20Loop%20-%20Part%2005%20-%20For%20-%20Else.py) |
| 052 | ⬜ | [For - Training](Lessons/Week%2007/052%20-%20Loop%20-%20Part%2006%20-%20For%20-%20Training.py) |
| 053 | ⬜ | [For - Nested Loop](Lessons/Week%2007/053%20-%20Loop%20-%20Part%2007%20-%20For%20-%20Nested%20Loop.py) |
| 054 | ⬜ | [Break & Continue & Pass](Lessons/Week%2007/054%20-%20Loop%20-%20Part%2008%20-%20Break%20%26%20Continue%20%26%20Pass.py) |
| 055 | ⬜ | [Advanced Dictionary](Lessons/Week%2007/055%20-%20Loop%20-%20Part%2009%20-%20Advanced%20Dictionary.py) |

</details>

<details>
<summary><strong>Week 08</strong> — Functions (9 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 056 | ⬜ | [Function - Return](Lessons/Week%2008/056%20-%20Function%20-%20Part%2001%20-%20Return.py) |
| 057 | ⬜ | [Parameters & Arguments](Lessons/Week%2008/057%20-%20Function%20-%20Part%2002%20-%20Parameters%20%26%20Arguments.py) |
| 058 | ⬜ | [Packing & Unpacking Arguments](Lessons/Week%2008/058%20-%20Function%20-%20Part%2003%20-%20Packing%20%26%20Unpacking%20Arguments.py) |
| 059 | ⬜ | [Default Parameters](Lessons/Week%2008/059%20-%20Function%20-%20Part%2004%20-%20Default%20Parameters.py) |
| 060 | ⬜ | [Packing & Unpacking Keyword Arguments](Lessons/Week%2008/060%20-%20Function%20-%20Part%2005%20-%20Packing%20%26%20Unpacking%20Keyword%20Arguments.py) |
| 061 | ⬜ | [Packing & Unpacking Training](Lessons/Week%2008/061%20-%20Function%20-%20Part%2006%20-%20Packing%20%26%20Unpacking%20Arguments%20Training.py) |
| 062 | ⬜ | [Scope](Lessons/Week%2008/062%20-%20Function%20-%20Part%2007%20-%20Scope.py) |
| 063 | ⬜ | [Recursion](Lessons/Week%2008/063%20-%20Function%20-%20Part%2008%20-%20Recursion.py) |
| 064 | ⬜ | [Lambda](Lessons/Week%2008/064%20-%20Function%20-%20Part%2009%20-%20Lambda.py) |

</details>

<details>
<summary><strong>Week 09</strong> — File Handling (4 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 065 | ⬜ | [File Handling - Introduction](Lessons/Week%2009/065%20-%20File%20Handling%20-%20Part%2001%20-%20Introduction.py) |
| 066 | ⬜ | [Read File](Lessons/Week%2009/066%20-%20File%20Handling%20-%20Part%2002%20-%20Read%20File.py) |
| 067 | ⬜ | [Write & Append In File](Lessons/Week%2009/067%20-%20File%20Handling%20-%20Part%2003%20-%20Write%20%26%20Append%20in%20File.py) |
| 068 | ⬜ | [Important Information](Lessons/Week%2009/068%20-%20File%20Handling%20-%20Part%2004%20-%20Important%20Information.py) |

</details>

<details>
<summary><strong>Week 10</strong> — Built-in Functions (7 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 069 | ⬜ | [Built-In Functions - Part 01](Lessons/Week%2010/069%20-%20Built-In%20Functions%20-%20Part%2001.py) |
| 070 | ⬜ | [Built-In Functions - Part 02](Lessons/Week%2010/070%20-%20Built-In%20Functions%20-%20Part%2002.py) |
| 071 | ⬜ | [Built-In Functions - Part 03](Lessons/Week%2010/071%20-%20Built-In%20Functions%20-%20Part%2003.py) |
| 072 | ⬜ | [Map](Lessons/Week%2010/072%20-%20Built-In%20Functions%20-%20Part%2004%20-%20Map.py) |
| 073 | ⬜ | [Filter](Lessons/Week%2010/073%20-%20Built-In%20Functions%20-%20Part%2005%20-%20Filter.py) |
| 074 | ⬜ | [Reduce](Lessons/Week%2010/074%20-%20Built-In%20Functions%20-%20Part%2006%20-%20Reduce.py) |
| 075 | ⬜ | [Built-In Functions - Part 07](Lessons/Week%2010/075%20-%20Built-In%20Functions%20-%20Part%2007.py) |

</details>

<details>
<summary><strong>Week 11</strong> — Modules, DateTime, Generators & Decorators (10 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 076 | ⬜ | [Modules - Introduction & Built-In](Lessons/Week%2011/076%20-%20Modules%20-%20Part%2001%20-%20Introduction%20%26%20Built-In%20Modules.py) |
| 077 | ⬜ | [Create Your Module](Lessons/Week%2011/077%20-%20Modules%20-%20Part%2002%20-%20Create%20Your%20Module.py) |
| 078 | ⬜ | [Install External Packages](Lessons/Week%2011/078%20-%20Modules%20-%20Part%2003%20-%20Install%20External%20Packages.py) |
| 079 | ⬜ | [Date & Time - Introduction](Lessons/Week%2011/079%20-%20Date%20%26%20Time%20-%20Part%2001%20-%20Introduction.py) |
| 080 | ⬜ | [Date & Time - Formatting](Lessons/Week%2011/080%20-%20Date%20%26%20Time%20-%20Part%2002%20-%20Formatting%20Date.py) |
| 081 | ⬜ | [Iterable vs Iterator](Lessons/Week%2011/081%20-%20Iterable%20vs%20Iterator.py) |
| 082 | ⬜ | [Generators](Lessons/Week%2011/082%20-%20Generators.py) |
| 083 | ⬜ | [Decorators - Introduction](Lessons/Week%2011/083%20-%20Decorators%20-%20Part%2001%20-%20Introduction.py) |
| 084 | ⬜ | [Decorators - Function With Parameters](Lessons/Week%2011/084%20-%20Decorators%20-%20Part%2002%20-%20Function%20with%20Parameters.py) |
| 085 | ⬜ | [Decorators - Speed Test Practical](Lessons/Week%2011/085%20-%20Decorators%20-%20Part%2003%20-%20Speed%20Test%20-%20Practical.py) |

</details>

<details>
<summary><strong>Week 12</strong> — Code Quality & Error Handling (9 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 086 | ⬜ | [Loop With Zip - Practical](Lessons/Week%2012/086%20-%20Loop%20On%20Many%20Iterators%20With%20Zip%20-%20Practical.py) |
| 087 | ⬜ | [Image Manipulation With Pillow](Lessons/Week%2012/087%20-%20Image%20Manipulation%20With%20Pillow%20-%20Practical.py) |
| 088 | ⬜ | [Doc String & Commenting vs Documenting](Lessons/Week%2012/088%20-%20Doc%20String%20%26%20Commenting%20vs%20Documenting.py) |
| 089 | ⬜ | [Pylint For Better Code](Lessons/Week%2012/089%20-%20Installing%20%26%20Using%20Pylint%20For%20Better%20Code.py) |
| 090 | ⬜ | [Errors & Exceptions Raising](Lessons/Week%2012/090%20-%20Errors%20%26%20Exceptions%20Raising.py) |
| 091 | ⬜ | [Try & Except & Else & Finally](Lessons/Week%2012/091%20-%20Exceptions%20Handling%20-%20Part%2001%20-%20Try%20%26%20Except%20%26%20Else%20%26%20Finally.py) |
| 092 | ⬜ | [Exceptions - Advanced Example](Lessons/Week%2012/092%20-%20Exceptions%20Handling%20-%20Part%2002%20-%20Advanced%20Example.py) |
| 093 | ⬜ | [Debugging Code](Lessons/Week%2012/093%20-%20Debugging%20Code.py) |
| 094 | ⬜ | [Type Hinting](Lessons/Week%2012/094%20-%20Type%20Hinting.py) |

</details>

<details>
<summary><strong>Week 13</strong> — Regular Expressions (8 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 095 | ⬜ | [Regex - Introduction](Lessons/Week%2013/095%20-%20Regular%20Expressions%20-%20Part%2001%20-%20Introduction.py) |
| 096 | ⬜ | [Regex - Quantifiers](Lessons/Week%2013/096%20-%20Regular%20Expressions%20-%20Part%2002%20-%20Quantifiers.py) |
| 097 | ⬜ | [Regex - Characters Classes Training](Lessons/Week%2013/097%20-%20Regular%20Expressions%20-%20Part%2003%20-%20Characters%20Classes%20Training.py) |
| 098 | ⬜ | [Regex - Assertions & Email Pattern](Lessons/Week%2013/098%20-%20Regular%20Expressions%20-%20Part%2004%20-%20Assertions%20%26%20Email%20Pattern.py) |
| 099 | ⬜ | [Regex - Logical Or & Escaping](Lessons/Week%2013/099%20-%20Regular%20Expressions%20-%20Part%2005%20-%20Logical%20Or%20%26%20Escaping.py) |
| 100 | ⬜ | [re Module - Search & FindAll](Lessons/Week%2013/100%20-%20Regular%20Expressions%20-%20Part%2006%20-%20re%20Module%20Search%20%26%20FindAll.py) |
| 101 | ⬜ | [re Module - Split & Sub](Lessons/Week%2013/101%20-%20Regular%20Expressions%20-%20Part%2007%20-%20re%20Module%20Split%20%26%20Sub.py) |
| 102 | ⬜ | [Group Training & Flags](Lessons/Week%2013/102%20-%20Regular%20Expressions%20-%20Part%2008%20-%20Group%20Training%20%26%20Flags.py) |

</details>

<details>
<summary><strong>Week 14</strong> — Object-Oriented Programming (14 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 103 | ⬜ | [OOP - Introduction](Lessons/Week%2014/103%20-%20OOP%20-%20Part%2001%20-%20Introduction.py) |
| 104 | ⬜ | [Class Syntax & Information](Lessons/Week%2014/104%20-%20OOP%20-%20Part%2002%20-%20Class%20Syntax%20%26%20Information.py) |
| 105 | ⬜ | [Instance Attributes & Methods - Part 01](Lessons/Week%2014/105%20-%20OOP%20-%20Part%2003%20-%20Instance%20Attributes%20%26%20Methods%20-%20Part%2001.py) |
| 106 | ⬜ | [Instance Attributes & Methods - Part 02](Lessons/Week%2014/106%20-%20OOP%20-%20Part%2004%20-%20Instance%20Attributes%20%26%20Methods%20-%20Part%2002.py) |
| 107 | ⬜ | [Class Attributes](Lessons/Week%2014/107%20-%20OOP%20-%20Part%2005%20-%20Class%20Attributes.py) |
| 108 | ⬜ | [Class Methods & Static Methods](Lessons/Week%2014/108%20-%20OOP%20-%20Part%2006%20-%20Class%20Methods%20%26%20Static%20Methods.py) |
| 109 | ⬜ | [Magic Methods](Lessons/Week%2014/109%20-%20OOP%20-%20Part%2007%20-%20Magic%20Methods.py) |
| 110 | ⬜ | [Inheritance](Lessons/Week%2014/110%20-%20OOP%20-%20Part%2008%20-%20Inheritance.py) |
| 111 | ⬜ | [Multiple Inheritance & Method Overriding](Lessons/Week%2014/111%20-%20OOP%20-%20Part%2009%20-%20Multiple%20Inheritance%20%20%26%20Method%20Overriding.py) |
| 112 | ⬜ | [Polymorphism](Lessons/Week%2014/112%20-%20OOP%20-%20Part%2010%20-%20Polymorphism.py) |
| 113 | ⬜ | [Encapsulation](Lessons/Week%2014/113%20-%20OOP%20-%20Part%2011%20-%20Encapsulation.py) |
| 114 | ⬜ | [Getters & Setters](Lessons/Week%2014/114%20-%20OOP%20-%20Part%2012%20-%20Getters%20%26%20Setters.py) |
| 115 | ⬜ | [@Property Decorator](Lessons/Week%2014/115%20-%20OOP%20-%20Part%2013%20-%20@Property%20Decorator.py) |
| 116 | ⬜ | [ABCs Abstract Base Class](Lessons/Week%2014/116%20-%20OOP%20-%20Part%2014%20-%20ABCs%20Abstract%20Base%20Class.py) |

</details>

<details>
<summary><strong>Week 15</strong> — SQLite Database (11 lessons) ⬜ Not Started</summary>

| # | Status | Lesson |
| :---: | :---: | :--- |
| 117 | ⬜ | [Database - Introduction](Lessons/Week%2015/117%20-%20Database%20-%20Part%2001%20-%20Introduction.py) |
| 118 | ⬜ | [SQLite - Create Database & Connect](Lessons/Week%2015/118%20-%20Database%20-%20Part%2002%20-%20SQLite%20-%20Create%20Database%20%26%20Connect.py) |
| 119 | ⬜ | [SQLite - Insert Data](Lessons/Week%2015/119%20-%20Database%20-%20Part%2003%20-%20SQLite%20-%20Insert%20Data%20Into%20Database.py) |
| 120 | ⬜ | [SQLite - Retrieve Data](Lessons/Week%2015/120%20-%20Database%20-%20Part%2004%20-%20SQLite%20-%20Retrieve%20Data%20From%20Database.py) |
| 121 | ⬜ | [SQLite - Training On Everything](Lessons/Week%2015/121%20-%20Database%20-%20Part%2005%20-%20SQLite%20-%20Training%20On%20Everything.py) |
| 122 | ⬜ | [SQLite - Update & Delete](Lessons/Week%2015/122%20-%20Database%20-%20Part%2006%20-%20SQLite%20-%20Update%20%26%20Delete%20From%20Database.py) |
| 123 | ⬜ | [Skills App - Part 01](Lessons/Week%2015/123%20-%20Database%20-%20Part%2007%20-%20SQLite%20-%20Create%20Skills%20App%20-%20Part%2001.py) |
| 124 | ⬜ | [Skills App - Part 02](Lessons/Week%2015/124%20-%20Database%20-%20Part%2008%20-%20SQLite%20-%20Create%20Skills%20App%20-%20Part%2002.py) |
| 125 | ⬜ | [Skills App - Part 03](Lessons/Week%2015/125%20-%20Database%20-%20Part%2009%20-%20SQLite%20-%20Create%20Skills%20App%20-%20Part%2003.py) |
| 126 | ⬜ | [Skills App - Part 04](Lessons/Week%2015/126%20-%20Database%20-%20Part%2010%20-%20SQLite%20-%20Create%20Skills%20App%20-%20Part%2004.py) |
| 127 | ⬜ | [Very Important Information](Lessons/Week%2015/127%20-%20Database%20-%20Part%2011%20-%20SQLite%20-%20Very%20Important%20Information.py) |

</details>

---

## 📝 Assignments

**0 / 113** assignments solved across 24 topics. Progress will be updated as assignments are completed.

| Status | Lessons | Topic | Solution |
| :---: | :--- | :--- | :---: |
| ⬜ | [001 – 010](https://elzero.org/python-assignments-lesson-from-1-to-10/) | Introduction & Variables | [Code](Assignments/Assignments%20From%20%5B%20001%20%5D%20To%20%5B%20010%20%5D) |
| ⬜ | [011 – 018](https://elzero.org/python-assignments-lesson-from-11-to-18/) | String & Methods | [Code](Assignments/Assignments%20From%20%5B%20011%20%5D%20To%20%5B%20018%20%5D) |
| ⬜ | [019 – 020](https://elzero.org/python-assignments-lesson-from-19-to-20/) | Numbers & Arithmetic | [Code](Assignments/Assignments%20From%20%5B%20019%20%5D%20To%20%5B%20020%20%5D) |
| ⬜ | [021 – 023](https://elzero.org/python-assignments-lesson-from-21-to-23/) | List & Methods | [Code](Assignments/Assignments%20From%20%5B%20021%20%5D%20To%20%5B%20023%20%5D) |
| ⬜ | [024 – 025](https://elzero.org/python-assignments-lesson-from-24-to-25/) | Tuple & Methods | [Code](Assignments/Assignments%20From%20%5B%20024%20%5D%20To%20%5B%20025%20%5D) |
| ⬜ | [026 – 032](https://elzero.org/python-assignments-lesson-from-26-to-32/) | Set & Dictionary | [Code](Assignments/Assignments%20From%20%5B%20026%20%5D%20To%20%5B%20032%20%5D) |
| ⬜ | [033 – 037](https://elzero.org/python-assignments-lesson-from-33-to-37/) | Operators & Type Conversion | [Code](Assignments/Assignments%20From%20%5B%20033%20%5D%20To%20%5B%20037%20%5D) |
| ⬜ | [038 – 040](https://elzero.org/python-assignments-lesson-from-38-to-40/) | User Input & Practice | [Code](Assignments/Assignments%20From%20%5B%20038%20%5D%20To%20%5B%20040%20%5D) |
| ⬜ | [041 – 046](https://elzero.org/python-assignments-lesson-from-41-to-46/) | Control Flow | [Code](Assignments/Assignments%20From%20%5B%20041%20%5D%20To%20%5B%20046%20%5D) |
| ⬜ | [047 – 050](https://elzero.org/python-assignments-lesson-from-47-to-50/) | While Loop | [Code](Assignments/Assignments%20From%20%5B%20047%20%5D%20To%20%5B%20050%20%5D) |
| ⬜ | [051 – 055](https://elzero.org/python-assignments-lesson-from-51-to-55/) | For Loop | [Code](Assignments/Assignments%20From%20%5B%20051%20%5D%20To%20%5B%20055%20%5D) |
| ⬜ | [056 – 059](https://elzero.org/python-assignments-lesson-from-56-to-59/) | Functions | [Code](Assignments/Assignments%20From%20%5B%20056%20%5D%20To%20%5B%20059%20%5D) |
| ⬜ | [060 – 064](https://elzero.org/python-assignments-lesson-from-60-to-64/) | Packing, Recursion & Lambda | [Code](Assignments/Assignments%20From%20%5B%20060%20%5D%20To%20%5B%20064%20%5D) |
| ⬜ | [065 – 068](https://elzero.org/python-assignments-lesson-from-65-to-68/) | File Handling | [Code](Assignments/Assignments%20From%20%5B%20065%20%5D%20To%20%5B%20068%20%5D) |
| ⬜ | [069 – 071](https://elzero.org/python-assignments-lesson-from-69-to-71/) | Built-In Functions | [Code](Assignments/Assignments%20From%20%5B%20069%20%5D%20To%20%5B%20071%20%5D) |
| ⬜ | [072 – 075](https://elzero.org/python-assignments-lesson-from-72-to-75/) | Map, Filter & Reduce | [Code](Assignments/Assignments%20From%20%5B%20072%5D%20To%20%5B%20075%20%5D) |
| ⬜ | [076 – 078](https://elzero.org/python-assignments-lesson-from-76-to-78/) | Modules & Packages | [Code](Assignments/Assignments%20From%20%5B%20076%20%5D%20To%20%5B%20078%20%5D) |
| ⬜ | [079 – 080](https://elzero.org/python-assignments-lesson-from-79-to-80/) | Date & Time | [Code](Assignments/Assignments%20From%20%5B%20079%20%5D%20To%20%5B%20080%20%5D) |
| ⬜ | [081 – 085](https://elzero.org/python-assignments-lesson-from-81-to-85/) | Generators & Decorators | [Code](Assignments/Assignments%20From%20%5B%20081%20%5D%20To%20%5B%20085%20%5D) |
| ⬜ | [086 – 089](https://elzero.org/python-assignments-lesson-from-86-to-89/) | Collection of Modules | [Code](Assignments/Assignments%20From%20%5B%20086%20%5D%20To%20%5B%20089%20%5D) |
| ⬜ | [090 – 094](https://elzero.org/python-assignments-lesson-from-90-to-94/) | Error Handling & Debugging | [Code](Assignments/Assignments%20From%20%5B%20090%20%5D%20To%20%5B%20094%20%5D) |
| ⬜ | [095 – 102](https://elzero.org/python-assignments-lesson-from-95-to-102/) | Regular Expressions | [Code](Assignments/Assignments%20From%20%5B%20095%20%5D%20To%20%5B%20102%20%5D) |
| ⬜ | [103 – 116](https://elzero.org/python-assignments-lesson-from-103-to-116/) | Object-Oriented Programming | [Code](Assignments/Assignments%20From%20%5B%20103%20%5D%20To%20%5B%20116%20%5D) |
| ⬜ | [117 – 127](https://elzero.org/python-assignments-lesson-from-117-to-127/) | SQLite Database | [Code](Assignments/Assignments%20From%20%5B%20117%20%5D%20To%20%5B%20127%20%5D) |

---

## 🧪 Testing & CI

### Run Tests Locally

```bash
# Using unittest (no extra dependencies)
python -m unittest discover tests

# Using pytest (if installed)
pip install pytest
pytest tests/ -v

# Or via the CLI dashboard
python course_runner.py --test-all
```

### GitHub Actions CI

Every push and pull request triggers automated testing across **Python 3.10, 3.11, and 3.12**. See the [workflow configuration](.github/workflows/python-ci.yml).

### Test Coverage

| Test Module | What It Validates |
| :--- | :--- |
| `test_lessons_week01_05` | Syntax validation for Weeks 01–05, string & collection operations |
| `test_lessons_week06_10` | Syntax validation for Weeks 06–10, `*args`/`**kwargs`, `map`/`filter`/`reduce` |
| `test_lessons_week11_15` | Syntax validation for Weeks 11–15, decorators, generators, regex, OOP, SQLite |
| `test_assignments` | Validates all 100+ assignment files compile without syntax errors |

---

## 🙏 Credits

- **Course**: [Mastering Python](https://elzero.org/study/mastering-python-study-plan/) by [Elzero Web School](https://elzero.org/)
- **Instructor**: [Osama Elzero](https://www.youtube.com/user/OsamaElzero)
- **Original Notes**: [Philopater Hany](https://github.com/PhilopaterHany)

---

<p align="center">
  Made with ❤️ for learning Python
</p>
