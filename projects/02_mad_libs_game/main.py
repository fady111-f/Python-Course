"""
🎮 Mad Libs Word Game
=====================
Videos 6-10: variables, escape sequences, concatenation

An interactive word game that creates funny stories
using player-provided words!
"""

import sys

# ===== UTF-8 Terminal Support =====
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ===== Game Header =====
print()
print("=" * 50)
print("  🎮  WELCOME TO THE PYTHON MAD LIBS GAME  🎮")
print("=" * 50)
print()
print("Fill in the blanks to create a funny story!")
print("Type a word for each prompt and press Enter.\n")

def safe_input(prompt, default):
    try:
        val = input(prompt).strip()
        return val if val else default
    except (EOFError, KeyboardInterrupt):
        return default

# ===== Collect Words =====
adjective_1 = safe_input("Enter an adjective (e.g., silly): ", "sparkly")
noun_1 = safe_input("Enter a noun (e.g., dragon): ", "dragon")
verb_past = safe_input("Enter a verb in past tense (e.g., jumped): ", "teleported")
place = safe_input("Enter a place (e.g., the moon): ", "the moon")
adjective_2 = safe_input("Enter another adjective (e.g., enormous): ", "gigantic")
food = safe_input("Enter a food (e.g., pizza): ", "pizza")
number = safe_input("Enter a number (e.g., 42): ", "42")
animal = safe_input("Enter an animal (e.g., penguin): ", "penguin")
verb_ing = safe_input("Enter a verb ending in -ing (e.g., dancing): ", "dancing")
celebrity = safe_input("Enter a famous person's name: ", "Einstein")
color = safe_input("Enter a color (e.g., purple): ", "purple")
noun_2 = safe_input("Enter another noun (e.g., spaceship): ", "spaceship")

# ===== Story Templates =====
print()
print("=" * 50)
print("  📖  YOUR MAD LIBS STORY  📖")
print("=" * 50)
print()

# Story 1: The Adventure
story_1 = "🏔️  THE " + adjective_1.upper() + " ADVENTURE\n"
story_1 = story_1 + "-" * 40 + "\n\n"
story_1 = story_1 + "Once upon a time, a " + adjective_1 + " " + noun_1 + "\n"
story_1 = story_1 + verb_past + " all the way to " + place + ".\n\n"
story_1 = story_1 + "There, it discovered a " + adjective_2 + " mountain\n"
story_1 = story_1 + "made entirely of " + food + "!\n\n"
story_1 = story_1 + "Exactly " + number + " " + animal + "s were seen\n"
story_1 = story_1 + verb_ing + " around it while " + celebrity + "\n"
story_1 = story_1 + "painted it " + color + " with a giant " + noun_2 + ".\n\n"
story_1 = story_1 + "THE END 🎬\n"

print(story_1)

# Story 2: The News Report
print("=" * 50)
print()
story_2 = "📺  BREAKING NEWS\n"
story_2 = story_2 + "-" * 40 + "\n\n"
story_2 = story_2 + "BREAKING: A " + adjective_1 + " " + animal + " was spotted\n"
story_2 = story_2 + verb_ing + " near " + place + " today.\n\n"
story_2 = story_2 + "Witnesses say it was carrying " + number + " " + noun_1 + "s\n"
story_2 = story_2 + "and wearing a " + color + " " + noun_2 + " on its head.\n\n"
story_2 = story_2 + celebrity + " was called to investigate but was\n"
story_2 = story_2 + "too busy eating " + adjective_2 + " " + food + ".\n\n"
story_2 = story_2 + 'The ' + animal + ' reportedly said: "No comment."\n'

print(story_2)

# ===== Play Again? =====
print("=" * 50)
print("\n🎉 Thanks for playing Mad Libs!")
print("Run the script again for a new story!\n")
