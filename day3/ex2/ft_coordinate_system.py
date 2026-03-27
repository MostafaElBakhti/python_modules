import math

print("=== Game Coordinate System ===")
def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
        except ValueError as error:
            print(f"Error on parameter '{parts[0]}': {error}")
            continue

        try:
            y = float(parts[1])
        except ValueError as error:
            print(f"Error on parameter '{parts[1]}': {error}")
            continue

        try:
            z = float(parts[2])
        except ValueError as error:
            print(f"Error on parameter '{parts[2]}': {error}")
            continue

        return (x, y, z)
    
print("Get a first set of coordinates")
first_pos = get_player_pos()
print(f"Got a first tuple: {first_pos}")