# 🎮 Mad Libs Word Game

**Concepts Used**: Variables, escape sequences (`\n`, `\t`), string concatenation, `input()`

## What It Does

An interactive word game where you provide random words (adjectives, nouns, verbs, etc.) and the program creates hilarious stories with your words!

## How to Run

```bash
python main.py
```

## How It Works

1. The game asks you for 12 different words (adjectives, nouns, verbs, etc.)
2. Your words get inserted into 2 pre-written story templates
3. The result is a unique, funny story every time!

## Sample Session

```
==================================================
  🎮  WELCOME TO THE PYTHON MAD LIBS GAME  🎮
==================================================

Fill in the blanks to create a funny story!

Enter an adjective (e.g., silly): sparkly
Enter a noun (e.g., dragon): toaster
Enter a verb in past tense (e.g., jumped): teleported
...

==================================================
  📖  YOUR MAD LIBS STORY  📖
==================================================

🏔️  THE SPARKLY ADVENTURE
----------------------------------------

Once upon a time, a sparkly toaster
teleported all the way to the moon.
...
```

## Concepts from Videos 6–10

| Concept | Where It's Used |
|---|---|
| Variables (Part 1 & 2) | Storing all player words |
| Escape Sequences | `\n` for newlines, `\t` for tabs |
| Concatenation | Building story strings with `+` |
| `input()` | Collecting words from the player |
| String repetition | `"=" * 50` for dividers |
