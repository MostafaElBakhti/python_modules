class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    plant_name: list[str] = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    plant_height: list[int] = [25, 200, 5, 80, 15]
    plant_age: list[int] = [30, 365, 90, 45, 120]
    for i in range(len(plant_height)):
        plant: Plant = Plant(plant_name[i], plant_height[i], plant_age[i])
        plant.get_info()
    print(f"\nTotal plants created: {i + 1}")
