# 🧠 Flashcard System

A CLI-based **spaced repetition** flashcard tool to test and reinforce your Python knowledge.

---

## How to Run

```bash
# Interactive menu
python flashcards/flashcards.py

# Load a specific deck
python flashcards/flashcards.py --deck 01

# List available decks
python flashcards/flashcards.py --list
```

## Available Decks

| Deck | Topic | Cards |
|---|---|---|
| `01_fundamentals` | Syntax, variables, data types | 20 |
| `02_strings` | Indexing, slicing, string methods | 20 |

## Features

- 🃏 **Shuffled cards** — different order every time
- 💡 **Hints** — optional hints for each question
- 📝 **Explanations** — learn why the answer is correct
- 📊 **Score tracking** — see your results and progress over time
- 🎯 **Smart matching** — partial answer matching for long answers
- 💾 **Persistent scores** — your history is saved to `.scores.json`

## Adding Your Own Decks

Create a JSON file in `flashcards/decks/` with this format:

```json
{
  "id": "my_deck",
  "name": "My Custom Deck",
  "description": "Description here",
  "cards": [
    {
      "question": "What is Python?",
      "answer": "A programming language",
      "hint": "Named after Monty Python",
      "explanation": "Python is a high-level language."
    }
  ]
}
```
