# 🔤 Python Strings — Cheat Sheet
> Covers: Videos 011–015 (Week 02, partial)

---

## 📌 Creating Strings

```python
# Single or double quotes
s1 = 'Hello'
s2 = "World"

# Multi-line strings
s3 = """This is a
multi-line string"""

s4 = '''Also works
with single quotes'''

# Empty string
empty = ""
```

---

## 📌 String Indexing

Strings are **zero-indexed** — each character has a position:

```
 H   e   l   l   o
 0   1   2   3   4      ← positive index
-5  -4  -3  -2  -1      ← negative index
```

```python
word = "Hello"
word[0]    # 'H'   — first character
word[4]    # 'o'   — last character
word[-1]   # 'o'   — last (from end)
word[-2]   # 'l'   — second to last
```

---

## 📌 String Slicing

**Syntax**: `string[start:end:step]`

| Slice | Result | Explanation |
|---|---|---|
| `s[0:3]` | `"Hel"` | Index 0, 1, 2 (end is exclusive) |
| `s[:3]` | `"Hel"` | From start to index 2 |
| `s[2:]` | `"llo"` | From index 2 to end |
| `s[:]` | `"Hello"` | Full copy |
| `s[::2]` | `"Hlo"` | Every 2nd character |
| `s[::-1]` | `"olleH"` | Reversed string |
| `s[-3:]` | `"llo"` | Last 3 characters |
| `s[1:4]` | `"ell"` | Index 1, 2, 3 |

```python
text = "Python Programming"

# Extract "Python"
text[:6]        # "Python"

# Extract "Programming"
text[7:]        # "Programming"

# Reverse the string
text[::-1]      # "gnimmargorP nohtyP"

# Every other character
text[::2]       # "Pto rgamn"
```

---

## 📌 String Methods — Reference Table

### Case Methods
| Method | Example | Result |
|---|---|---|
| `.upper()` | `"hello".upper()` | `"HELLO"` |
| `.lower()` | `"HELLO".lower()` | `"hello"` |
| `.title()` | `"hello world".title()` | `"Hello World"` |
| `.capitalize()` | `"hello world".capitalize()` | `"Hello world"` |
| `.swapcase()` | `"Hello".swapcase()` | `"hELLO"` |

### Search Methods
| Method | Example | Result |
|---|---|---|
| `.find(sub)` | `"Hello".find("ll")` | `2` (index) |
| `.find(sub)` | `"Hello".find("xyz")` | `-1` (not found) |
| `.index(sub)` | `"Hello".index("ll")` | `2` (index) |
| `.index(sub)` | `"Hello".index("xyz")` | `ValueError` ❌ |
| `.count(sub)` | `"hello".count("l")` | `2` |
| `.startswith()` | `"Hello".startswith("He")` | `True` |
| `.endswith()` | `"Hello".endswith("lo")` | `True` |

### Whitespace & Padding
| Method | Example | Result |
|---|---|---|
| `.strip()` | `"  hi  ".strip()` | `"hi"` |
| `.lstrip()` | `"  hi  ".lstrip()` | `"hi  "` |
| `.rstrip()` | `"  hi  ".rstrip()` | `"  hi"` |
| `.center(10)` | `"hi".center(10, "-")` | `"----hi----"` |
| `.ljust(10)` | `"hi".ljust(10, "-")` | `"hi--------"` |
| `.rjust(10)` | `"hi".rjust(10, "-")` | `"--------hi"` |
| `.zfill(5)` | `"42".zfill(5)` | `"00042"` |

### Modify & Replace
| Method | Example | Result |
|---|---|---|
| `.replace(a, b)` | `"Hello".replace("l", "r")` | `"Herro"` |
| `.split()` | `"a b c".split()` | `["a", "b", "c"]` |
| `.split(",")` | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| `.join()` | `"-".join(["a","b"])` | `"a-b"` |
| `.expandtabs(4)` | `"a\tb".expandtabs(4)` | `"a   b"` |

### Check / Validate
| Method | Returns `True` when... |
|---|---|
| `.isalpha()` | All characters are letters |
| `.isdigit()` | All characters are digits |
| `.isalnum()` | All characters are letters or digits |
| `.isspace()` | All characters are whitespace |
| `.isupper()` | All cased characters are uppercase |
| `.islower()` | All cased characters are lowercase |
| `.istitle()` | String is in title case |

---

## 📌 String Properties

```python
s = "Hello"

# Strings are IMMUTABLE — you can't change them in place
# s[0] = "h"  # ❌ TypeError

# Length
len(s)         # 5

# Membership
"ell" in s     # True
"xyz" not in s # True

# Iteration
for char in s:
    print(char)  # H, e, l, l, o
```

---

## 📌 Key Differences

| `.find()` vs `.index()` |
|---|
| `.find("x")` → returns `-1` if not found |
| `.index("x")` → raises `ValueError` if not found |

| `.strip()` variants |
|---|
| `.strip()` → removes from both sides |
| `.lstrip()` → removes from left only |
| `.rstrip()` → removes from right only |

---

## 💡 Common Pitfalls

| Mistake | Fix |
|---|---|
| `s[0] = "h"` | Strings are immutable! Use `s = "h" + s[1:]` |
| `s.upper()` then expecting `s` changed | Methods return new strings: `s = s.upper()` |
| `s.split("")` | Can't split on empty string — use `list(s)` instead |
| Off-by-one in slicing | Remember: `s[start:end]` — end is **exclusive** |

---

## 🧠 Quick Quiz

1. What does `"Python"[1:4]` return? → `"yth"`
2. How to reverse `"abc"`? → `"abc"[::-1]` → `"cba"`
3. Difference between `.find()` and `.index()`? → `.find()` returns -1, `.index()` raises error
4. Is `"hello".upper()` destructive? → No, returns new string
5. What does `"a-b-c".split("-")` return? → `["a", "b", "c"]`
