def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open("test.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'test.txt'\n")

    print("Testing KeyError...")
    try:
        plants = {"rose": 1, "tree": 5}
        print(plants["sunflower"])
    except KeyError:
        print("Caught KeyError: 'sunflower'\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
        2 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


test_error_types()
