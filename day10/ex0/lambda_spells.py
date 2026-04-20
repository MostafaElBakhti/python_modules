def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    avg_power = round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "fire"},
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Ice Wand", "power": 78, "type": "ice"}
    ]

    mages = [
        {"name": "A", "power": 50, "element": "fire"},
        {"name": "B", "power": 80, "element": "ice"},
        {"name": "C", "power": 30, "element": "wind"}
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
        f"comes before "
        f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )
    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print("\nTesting power filter...")
    print(power_filter(mages, 60))

    print("\nTesting mage stats...")
    print(mage_stats(mages))
