def water_plants(plant_list) -> None:
    print("Testing normal watering...")
    print("Opening watering system")
    for plan in plant_list:
        print(f"watering {plan}")
    print("Closing watering system (cleanup)")
