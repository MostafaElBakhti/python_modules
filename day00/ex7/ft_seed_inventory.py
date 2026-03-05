def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed} seeds: {quantity} {unit} meters")
    else:
        print("Unknown unit type")


ft_seed_inventory("test", 5, "ho")
