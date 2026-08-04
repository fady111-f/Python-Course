"""
🎴 Personal Card Generator
===========================
Videos 1-5: print(), variables, data types

Generate a styled personal info card in the terminal.
"""

import sys

# ===== UTF-8 Terminal Support =====
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ===== Your Information =====
first_name = "Fady"
last_name = "Hany"
age = 22
job_title = "Software Developer"
country = "Egypt"
email = "fady@example.com"
github = "github.com/fady111-f"
skills = "Python, Dart, Flutter"
hobby = "Building Apps"

# ===== Card Dimensions =====
card_width = 48
border_char = "█"
inner_char = "░"

# ===== Build the Card =====
def build_line(label, value):
    """Build a single info line with padding."""
    content = f"  {label}: {value}"
    padding = card_width - len(content) - 4
    if padding < 0:
        padding = 0
    return f"{border_char} {content}{' ' * padding} {border_char}"

def build_empty():
    """Build an empty inner line."""
    return f"{border_char} {' ' * (card_width - 4)} {border_char}"

def build_separator():
    """Build a decorative separator line."""
    inner = inner_char * (card_width - 4)
    return f"{border_char} {inner} {border_char}"

# ===== Print the Card =====
print()
print(border_char * card_width)
print(build_empty())

# Name (centered)
full_name = f"{first_name} {last_name}"
name_padding = card_width - len(full_name) - 4
left_pad = name_padding // 2
right_pad = name_padding - left_pad
print(f"{border_char} {' ' * left_pad}{full_name}{' ' * right_pad} {border_char}")

# Title (centered)
title_padding = card_width - len(job_title) - 4
t_left = title_padding // 2
t_right = title_padding - t_left
print(f"{border_char} {' ' * t_left}{job_title}{' ' * t_right} {border_char}")

print(build_empty())
print(build_separator())
print(build_empty())

# Info Lines
print(build_line("Age", str(age)))
print(build_line("Country", country))
print(build_line("Email", email))
print(build_line("GitHub", github))
print(build_line("Skills", skills))
print(build_line("Hobby", hobby))

print(build_empty())
print(build_separator())
print(build_empty())

# Footer
footer = "Made with Python"
f_padding = card_width - len(footer) - 4
f_left = f_padding // 2
f_right = f_padding - f_left
print(f"{border_char} {' ' * f_left}{footer}{' ' * f_right} {border_char}")

print(build_empty())
print(border_char * card_width)
print()
