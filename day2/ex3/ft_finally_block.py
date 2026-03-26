class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)

def plantError() -> None:
    raise PlantError("The tomato plant is wilting!")

def waterError() -> None:
    raise WaterError(" Not enough water in the tank!")

def test_all_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        plantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        waterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for error_func in [plantError, waterError]:
        try:
            error_func()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")
test_all_errors()