import random

names: list = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory"
    ]

cap = [item.capitalize() for item in names]
capitalized_names = [ item for item in names if item == item.capitalize()]

print("=== Game Data Alchemist ===")
print(f"Initial list of players: {names}")
print(f"New list with all names capitalized: {cap}")
print(f"New list of capitalized names only: {capitalized_names}")