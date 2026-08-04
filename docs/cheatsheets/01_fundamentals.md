# 🐍 Python Fundamentals — Cheat Sheet
> Covers: Videos 001–010 (Week 01)

---

## 📌 Syntax Basics

```python
# This is a comment
print("Hello, World!")  # Your first Python program

"""
This is a multi-line comment
(actually a docstring)
"""
```

| Concept | Example |
|---|---|
| Print to console | `print("Hello")` |
| Single-line comment | `# comment here` |
| Multi-line comment | `""" ... """` or `''' ... '''` |
| End of statement | Newline (no `;` needed) |
| Code blocks | Indentation (4 spaces) |

---

## 📌 Data Types Overview

| Type | Example | Description |
|---|---|---|
| `str` | `"Hello"`, `'World'` | Text/string |
| `int` | `10`, `-5`, `0` | Whole numbers |
| `float` | `3.14`, `-0.5` | Decimal numbers |
| `bool` | `True`, `False` | Boolean values |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `set` | `{1, 2, 3}` | Unordered, unique items |
| `dict` | `{"key": "val"}` | Key-value pairs |
| `NoneType` | `None` | Represents nothing |

```python
# Check type of a value
print(type("Hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
```

---

## 📌 Variables

### Rules for Variable Names
| ✅ Valid | ❌ Invalid | Why |
|---|---|---|
| `my_name` | `my-name` | No hyphens |
| `_private` | `2fast` | Can't start with a number |
| `camelCase` | `my name` | No spaces |
| `CONSTANT` | `class` | Can't use reserved keywords |

### Declaration & Assignment
```python
# Single assignment
name = "Fady"
age = 22
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3

# Same value to multiple variables
a = b = c = 0

# Swap values
x, y = y, x
```

### Naming Conventions
```python
# Variables & functions → snake_case
user_name = "fady"
def calculate_total():
    pass

# Constants → UPPER_SNAKE_CASE
MAX_ATTEMPTS = 3
PI = 3.14159

# Classes → PascalCase
class MyClass:
    pass
```

---

## 📌 Escape Sequences

| Sequence | Output | Description |
|---|---|---|
| `\n` | Newline | Moves to next line |
| `\t` | Tab | Horizontal tab |
| `\\` | `\` | Backslash |
| `\'` | `'` | Single quote |
| `\"` | `"` | Double quote |
| `\r` | Carriage return | Goes to line start |
| `\b` | Backspace | Removes previous char |
| `\0` | Null | Null character |

```python
print("Line 1\nLine 2")
# Line 1
# Line 2

print("Name:\tFady")
# Name:   Fady

print("He said \"Hello\"")
# He said "Hello"

# Raw string — ignores escape sequences
print(r"C:\Users\new_folder")
# C:\Users\new_folder
```

---

## 📌 String Concatenation

```python
# Using + operator
first = "Hello"
last = "World"
full = first + " " + last  # "Hello World"

# Using * for repetition
line = "-" * 20  # "--------------------"

# f-strings (formatted strings) — preferred!
name = "Fady"
age = 22
print(f"My name is {name} and I'm {age} years old")

# You CANNOT concatenate str + int directly
# print("Age: " + 22)  # ❌ TypeError
print("Age: " + str(22))  # ✅ "Age: 22"
```

---

## 💡 Common Pitfalls

| Mistake | Fix |
|---|---|
| `print "Hello"` | `print("Hello")` — need parentheses in Python 3 |
| `"age: " + 25` | `"age: " + str(25)` or `f"age: {25}"` |
| `Name = "A"` then using `name` | Python is case-sensitive! |
| Forgetting indentation | Always use 4 spaces for blocks |

---

## 🧠 Quick Quiz

1. What does `type(3.14)` return? → `<class 'float'>`
2. Is `my_var` a valid variable name? → ✅ Yes
3. What does `\t` do? → Inserts a horizontal tab
4. How to repeat a string 3 times? → `"abc" * 3` → `"abcabcabc"`
5. What's the output of `print("A" + "B" + "C")`? → `ABC`
