# from ..elements import create_air
from ..elements import create_air
from alchemy.potions import strength_potion
import elements as base_elements


def lead_to_gold() -> str:
    air = create_air()
    strength = strength_potion()
    fire = base_elements.create_fire()
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{air}' and '{strength}' mixed with '{fire}'"
    )




if __name__ == "__main__":
    print(lead_to_gold())






















# def lead_to_gold() -> str:
#     air = create_air()
#     strength = strength_potion()
#     fire = base_elements.create_fire()
#     return (
#         "Recipe transmuting Lead to Gold: "
#         f"brew '{air}' and '{strength}' mixed with '{fire}'"
#     )


# import elements as base_elements
# from alchemy.potions import strength_potion

# from ..elements import create_air