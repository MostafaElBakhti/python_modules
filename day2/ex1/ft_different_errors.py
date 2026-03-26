def input_temperature(temp_str: str) -> int:
    tmp = int(temp_str)
    if tmp < 0:
        raise ValueError(f"{tmp}°C is too cold for plants (min 0°C)")
    if tmp > 40:
        raise ValueError(f"{tmp}°C is too hot for plants (max 40°C)")
    return tmp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

    tests = ["25", "abc", "-5", "45"]

    for temp in tests:
        print(f"Input data is '{temp}'")
        try:
            temp_value = input_temperature(temp)
            print(f"Temperature is now {temp_value}°C\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
