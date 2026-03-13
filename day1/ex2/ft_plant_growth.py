class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.Age = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.Age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Fly", 35, 50)
    grow1: int = plant.height
    grow2: int = plant2.height
    print("=== Day 1 ===")
    plant.get_info()
    plant2.get_info()
    for i in range(6):
        plant.grow()
        plant.age()
        plant2.grow()
        plant2.age()
    print("=== Day 7 ===")
    plant.get_info()
    plant2.get_info()
    plant_grow: int = plant.height - grow1 + plant2.height - grow2
    print(f"Growth this week: +{plant_grow}cm")
