import sys


def main():
    inventory: dict[str, int] = {}
    print("=== Inventory System Analysis ===")
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
        else:
            item, quantity = arg.split(":")
            try:
                quantity = int(quantity)
                if item in inventory:
                    print(f"Redundant item '{item}' - discarding")
                else:
                    inventory[item] = quantity
            except ValueError as error:
                print(f"Quantity error for '{item}': {error}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    length = len(inventory)
    print(f"Total quantity of the {length} items: {sum(inventory.values())}")

    total_quantity = sum(inventory.values())

    for item in inventory:
        percentage = (inventory[item] / total_quantity) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")
    if inventory:
        first_item = list(inventory.keys())[0]
        most_item = first_item
        least_item = first_item
    else:
        print("No valid inventory items!")
        return
    for item in inventory:
        if inventory[item] > inventory[most_item]:
            most_item = item

        if inventory[item] < inventory[least_item]:
            least_item = item

    print(f"Item most abundant: {most_item} "
          f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item} "
          f"with quantity {inventory[least_item]}")
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
