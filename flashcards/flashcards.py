"""
🧠 Python Flashcard System
===========================
A CLI-based spaced repetition flashcard tool.

Usage:
    python flashcards.py                  # Interactive menu
    python flashcards.py --deck 01        # Load a specific deck
    python flashcards.py --list           # List available decks
"""

import json
import os
import sys
import random
import time

# ===== UTF-8 Support =====
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ===== Constants =====
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DECKS_DIR = os.path.join(SCRIPT_DIR, "decks")
SCORES_FILE = os.path.join(SCRIPT_DIR, ".scores.json")

# ===== Colors (ANSI) =====
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_GREEN = "\033[42m"
    BG_RED = "\033[41m"
    BG_BLUE = "\033[44m"


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def load_scores():
    """Load saved scores from file."""
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_scores(scores):
    """Save scores to file."""
    try:
        with open(SCORES_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, indent=2)
    except Exception:
        pass


def get_available_decks():
    """Scan the decks directory for available flashcard decks."""
    decks = []
    if not os.path.exists(DECKS_DIR):
        return decks
    for filename in sorted(os.listdir(DECKS_DIR)):
        if filename.endswith(".json"):
            filepath = os.path.join(DECKS_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                decks.append({
                    "file": filename,
                    "path": filepath,
                    "name": data.get("name", filename),
                    "description": data.get("description", ""),
                    "card_count": len(data.get("cards", [])),
                })
            except Exception:
                continue
    return decks


def load_deck(filepath):
    """Load a flashcard deck from a JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def print_header():
    """Print the app header."""
    print()
    print(f"{C.PURPLE}{C.BOLD}{'=' * 55}{C.RESET}")
    print(f"{C.PURPLE}{C.BOLD}  {'':>5}PYTHON FLASHCARD SYSTEM{C.RESET}")
    print(f"{C.PURPLE}{C.BOLD}  {'':>5}Spaced Repetition for Python Mastery{C.RESET}")
    print(f"{C.PURPLE}{C.BOLD}{'=' * 55}{C.RESET}")
    print()


def print_card_front(card, index, total):
    """Print the front of a flashcard (question)."""
    print()
    print(f"{C.BLUE}{C.BOLD}  Card {index + 1} / {total}{C.RESET}")
    print(f"{C.DIM}  {'─' * 45}{C.RESET}")
    print()
    print(f"{C.WHITE}{C.BOLD}  Q: {card['question']}{C.RESET}")
    print()

    if "hint" in card and card["hint"]:
        print(f"{C.DIM}  Hint: {card['hint']}{C.RESET}")
        print()

    if "code" in card and card["code"]:
        print(f"{C.CYAN}  Code:{C.RESET}")
        for line in card["code"].split("\n"):
            print(f"{C.CYAN}    {line}{C.RESET}")
        print()


def print_card_back(card, correct):
    """Print the back of a flashcard (answer)."""
    if correct:
        print(f"{C.GREEN}{C.BOLD}  ✅ CORRECT!{C.RESET}")
    else:
        print(f"{C.RED}{C.BOLD}  ❌ Not quite!{C.RESET}")

    print()
    print(f"{C.YELLOW}{C.BOLD}  A: {card['answer']}{C.RESET}")
    print()

    if "explanation" in card and card["explanation"]:
        print(f"{C.DIM}  📝 {card['explanation']}{C.RESET}")
        print()


def run_quiz(deck_data):
    """Run a flashcard quiz session."""
    cards = deck_data.get("cards", [])
    if not cards:
        print(f"\n{C.RED}  No cards in this deck!{C.RESET}")
        return

    deck_name = deck_data.get("name", "Unknown Deck")
    scores = load_scores()
    deck_key = deck_data.get("id", deck_name)

    # Shuffle cards
    shuffled = list(cards)
    random.shuffle(shuffled)

    correct_count = 0
    total = len(shuffled)
    results = []

    clear_screen()
    print_header()
    print(f"{C.WHITE}{C.BOLD}  Deck: {deck_name}{C.RESET}")
    print(f"{C.DIM}  {total} cards | Type your answer and press Enter{C.RESET}")
    print(f"{C.DIM}  Type 'skip' to skip, 'quit' to end early{C.RESET}")

    for i, card in enumerate(shuffled):
        print(f"\n{C.DIM}  {'━' * 45}{C.RESET}")
        print_card_front(card, i, total)

        user_answer = input(f"  {C.WHITE}Your answer: {C.RESET}").strip()

        if user_answer.lower() == "quit":
            total = i
            break

        if user_answer.lower() == "skip":
            print(f"\n{C.YELLOW}  ⏭️  Skipped{C.RESET}")
            print(f"{C.YELLOW}{C.BOLD}  A: {card['answer']}{C.RESET}")
            results.append({"card": card["question"], "correct": False, "skipped": True})
            continue

        # Check answer (case-insensitive, stripped)
        correct_answer = card["answer"].strip().lower()
        user_clean = user_answer.strip().lower()

        # Accept partial matches for longer answers
        is_correct = False
        if user_clean == correct_answer:
            is_correct = True
        elif len(correct_answer) > 20 and user_clean in correct_answer:
            is_correct = True
        elif correct_answer in user_clean:
            is_correct = True

        if is_correct:
            correct_count += 1

        print_card_back(card, is_correct)
        results.append({"card": card["question"], "correct": is_correct, "skipped": False})

    # ===== Results =====
    print(f"\n{C.PURPLE}{C.BOLD}{'=' * 55}{C.RESET}")
    print(f"{C.PURPLE}{C.BOLD}  SESSION RESULTS{C.RESET}")
    print(f"{C.PURPLE}{C.BOLD}{'=' * 55}{C.RESET}")
    print()

    if total > 0:
        percentage = round((correct_count / total) * 100)
        bar_filled = int(percentage / 5)
        bar_empty = 20 - bar_filled
        bar_color = C.GREEN if percentage >= 70 else C.YELLOW if percentage >= 40 else C.RED

        print(f"  Score: {C.BOLD}{correct_count} / {total}{C.RESET} ({percentage}%)")
        print(f"  [{bar_color}{'█' * bar_filled}{C.DIM}{'░' * bar_empty}{C.RESET}]")
        print()

        if percentage == 100:
            print(f"  {C.GREEN}{C.BOLD}🏆 PERFECT SCORE! You're a Python master!{C.RESET}")
        elif percentage >= 70:
            print(f"  {C.GREEN}🎉 Great job! Keep it up!{C.RESET}")
        elif percentage >= 40:
            print(f"  {C.YELLOW}📚 Good effort! Review the missed cards.{C.RESET}")
        else:
            print(f"  {C.RED}💪 Keep studying! You'll get there!{C.RESET}")

        # Show missed cards
        missed = [r for r in results if not r["correct"] and not r.get("skipped", False)]
        if missed:
            print(f"\n  {C.RED}Cards to review:{C.RESET}")
            for r in missed:
                print(f"  {C.DIM}  • {r['card']}{C.RESET}")

        # Save score
        if deck_key not in scores:
            scores[deck_key] = []
        scores[deck_key].append({
            "date": time.strftime("%Y-%m-%d %H:%M"),
            "score": correct_count,
            "total": total,
            "percentage": percentage,
        })
        save_scores(scores)
    else:
        print(f"  {C.DIM}No cards answered.{C.RESET}")

    print()


def show_deck_list():
    """Show available decks."""
    decks = get_available_decks()
    scores = load_scores()

    print(f"\n{C.WHITE}{C.BOLD}  Available Decks:{C.RESET}\n")

    if not decks:
        print(f"  {C.DIM}No decks found in {DECKS_DIR}{C.RESET}")
        return

    for i, deck in enumerate(decks, 1):
        best = ""
        deck_scores = scores.get(deck["name"], [])
        if deck_scores:
            best_pct = max(s["percentage"] for s in deck_scores)
            best = f" | Best: {best_pct}%"

        print(f"  {C.CYAN}{i}.{C.RESET} {C.WHITE}{deck['name']}{C.RESET}")
        print(f"     {C.DIM}{deck['description']} ({deck['card_count']} cards{best}){C.RESET}")
        print()

    return decks


def main_menu():
    """Main interactive menu."""
    while True:
        clear_screen()
        print_header()

        decks = show_deck_list()

        if not decks:
            print(f"\n  {C.DIM}Add JSON deck files to: {DECKS_DIR}{C.RESET}")
            input(f"\n  Press Enter to exit...")
            break

        print(f"  {C.DIM}Enter deck number to start, or 'q' to quit{C.RESET}")
        choice = input(f"\n  {C.WHITE}Choose: {C.RESET}").strip()

        if choice.lower() in ("q", "quit", "exit"):
            print(f"\n  {C.PURPLE}Happy studying! 🐍{C.RESET}\n")
            break

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(decks):
                deck_data = load_deck(decks[idx]["path"])
                run_quiz(deck_data)
                input(f"  Press Enter to continue...")
            else:
                print(f"\n  {C.RED}Invalid choice!{C.RESET}")
                time.sleep(1)
        except ValueError:
            print(f"\n  {C.RED}Please enter a number!{C.RESET}")
            time.sleep(1)


# ===== CLI Entry Point =====
if __name__ == "__main__":
    args = sys.argv[1:]

    if "--list" in args:
        print_header()
        show_deck_list()
    elif "--deck" in args:
        idx = args.index("--deck")
        if idx + 1 < len(args):
            deck_id = args[idx + 1]
            decks = get_available_decks()
            found = None
            for d in decks:
                if deck_id in d["file"] or deck_id in d["name"].lower():
                    found = d
                    break
            if found:
                deck_data = load_deck(found["path"])
                run_quiz(deck_data)
            else:
                print(f"Deck '{deck_id}' not found. Use --list to see available decks.")
        else:
            print("Usage: python flashcards.py --deck <deck_id>")
    else:
        main_menu()
