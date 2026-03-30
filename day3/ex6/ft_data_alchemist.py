import random

names: list = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
    ]

cap = [item.capitalize() for item in names]
capitalized_names = [item for item in names if item == item.capitalize()]
scores = {item: random.randint(0, 1000) for item in cap}
total = sum(scores.values())
count = len(scores)
average = round(total / count)
high_score = {name: score for name, score in scores.items() if score > average}

print("=== Game Data Alchemist ===")
print(f"Initial list of players: {names}")
print(f"New list with all names capitalized: {cap}")
print(f"New list of capitalized names only: {capitalized_names}")
print(f"Score dict : {scores}")
print(f"Score average is {average}")
print(f"High scores: {high_score}")
