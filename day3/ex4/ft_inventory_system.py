import sys

def main():
    inventory = {}
    print("=== Inventory System Analysis ===")
    for arg in sys.argv[1:]:  ## 1: --> from arg 1 to end
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
        else:
            item , quantity = arg.split(":")
            try:
                quantity = int(quantity)
                if item in inventory:
                    print(f"Redundant item '{item}' - discarding")
                else: 
                    inventory[item] = quantity
            except ValueError as error:
                 print(f"Quantity error for '{item}': {error}")
    print(f"Got inventory: {inventory}")


if __name__ == "__main__":
    main()