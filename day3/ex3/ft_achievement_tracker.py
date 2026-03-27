import random


achievements = [
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Treasure Hunter",
    "Sharp Mind",
    "Crafting Genius",
    "Collector Supreme",
    "World Savior",
    "Speed Runner",
    "Untouchable",
    "Strategist",
    "Survivor",
    "Unstoppable",
    "Hidden Path Finder"
]
def gen_player_achievements():
    count = random.randint(5, 9)
    picked = random.sample(achievements, count)
    return set(picked)

Alice = gen_player_achievements()
Bob = gen_player_achievements()
Charlie = gen_player_achievements()
Dylan = gen_player_achievements()

all_achievements = set(achievements)
all_distinct_achievements = Alice.union(Bob, Charlie, Dylan)
common_achievements = Alice.intersection(Bob, Charlie, Dylan)



print("=== Achievement Tracker System ===")
print(f"Player Alice: {Alice}")
print(f"Player Bob: {Bob}")
print(f"Player Charlie: {Charlie}")
print(f"Player Dylan: {Dylan}")
print(f"\nAll distinct achievements: {all_distinct_achievements}")
print(f"\nCommon achievements: {common_achievements}")
print(f"\nOnly Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}")
print(f"\nAlice is missing: {all_achievements.difference(Alice)}")
print(f"\nAlice is missing: {all_achievements.difference(Bob)}")
print(f"\nAlice is missing: {all_achievements.difference(Charlie)}")
print(f"\nAlice is missing: {all_achievements.difference(Dylan)}")