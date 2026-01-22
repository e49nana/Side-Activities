import random
import string
import time


def random_username(length=8):
    """Génère un pseudo aléatoire"""
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def roll_dice(sides=6):
    """Lance un dé"""
    return random.randint(1, sides)


def random_quote():
    """Retourne une citation aléatoire"""
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "Talk is cheap. Show me the code.",
        "Fix the cause, not the symptom.",
        "First, solve the problem. Then, write the code.",
    ]
    return random.choice(quotes)


def countdown(seconds):
    """Petit compte à rebours inutile"""
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("🚀 Go!")


if __name__ == "__main__":
    print("=== Random Python Script ===")
    print("Username :", random_username())
    print("Dice roll :", roll_dice())
    print("Quote :", random_quote())
    countdown(3)
