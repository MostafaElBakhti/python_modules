from creature import Creature

class Aquabubble(Creature):
    def __init__(self):
        super().__init__("Aquabubble", "Water")

    def attack(self) -> str:
        return "Aquabubble uses Water Gun!"

class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"

