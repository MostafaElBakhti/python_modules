def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    tests = ["25", "abc"]

    for temp in tests:
        print(f"Input data is '{temp}'")
        try:
            temp_value = input_temperature(temp)
            print(f"Temperature is now {temp_value}°C\n")
        except Exception as error:
            print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
