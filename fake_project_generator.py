import random
import datetime


PROJECT_NAMES = [
    "QuantumBanana",
    "UltraTodo",
    "NeuralCoffee",
    "CryptoDuck",
    "HyperWeather",
    "SmartFridgeAI",
]

DESCRIPTIONS = [
    "A revolutionary tool that nobody asked for.",
    "Solves a problem that does not exist yet.",
    "Built for fun, not for production.",
    "An overengineered solution to a simple idea.",
    "Because why not?",
]

TECH_STACK = [
    "Python",
    "JavaScript",
    "Rust",
    "Go",
    "Docker",
    "FastAPI",
    "React",
]


def generate_project():
    name = random.choice(PROJECT_NAMES)
    description = random.choice(DESCRIPTIONS)
    stack = random.sample(TECH_STACK, random.randint(2, 4))
    created_at = datetime.datetime.now().strftime("%Y-%m-%d")

    return {
        "name": name,
        "description": description,
        "stack": stack,
        "created_at": created_at,
    }


def print_project(project):
    print("📦 Fake Project Generator")
    print("-" * 30)
    print(f"Name        : {project['name']}")
    print(f"Description : {project['description']}")
    print(f"Tech stack  : {', '.join(project['stack'])}")
    print(f"Created at  : {project['created_at']}")


if __name__ == "__main__":
    project = generate_project()
    print_project(project)
