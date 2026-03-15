def check_temperature(temp_str) -> int | None:
    try:
        temp = int(temp_str)

        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    tests = ["25", "abc", "100", "-50"]

    for i in tests:
        print(f"Testing temperature: {i}")
        check_temperature(i)
    print("All tests completed - program didn't crash!")


test_temperature_input()
