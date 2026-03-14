class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        # self.age: int = age
        self.test: str = name

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points: int = points


class GardenManager:
    def __init__(self, owner: str):
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.stats = GardenManager.GardenStats()

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.stats.plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1

    def show_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                prize += 1
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming), "
                      f"Prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                flowering += 1
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming)")
            else:
                regular += 1
                print(f"- {plant.name} Tree: {plant.height}cm")
        print(f"Plants added: {self.stats.plants_added}, "
              f"Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")

    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0

    @classmethod
    def create_garden_network(cls, owners):
        gardens = []

        for owner in owners:
            gardens.append(cls(owner))

        return gardens

    @staticmethod
    def validate_height(height) -> bool:
        if height > 0:
            return True
        else:
            return False

    def calculate_score(self) -> int:
        score = 0
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                score += plant.points
        return score


if __name__ == "__main__":
    tree = Plant("Oak", 500)
    flower = FloweringPlant("Rose", 25, "red")
    prize_flower = PrizeFlower("Sunflower", 30, "yellow", 10)

    owners = ["Alice", "Bob"]
    gardens = GardenManager.create_garden_network(owners)
    alice, bob = gardens

    alice.add_plant(tree)
    alice.add_plant(flower)
    alice.add_plant(prize_flower)

    prize_flower2 = PrizeFlower("Tulip", 40, "purple", 20)
    bob.add_plant(prize_flower2)

    alice.help_plants_grow()
    alice.show_report()

    print("Height validation test:", GardenManager.validate_height(10))

    print(f"Garden scores - Alice: {alice.calculate_score()}, "
          f"Bob: {bob.calculate_score()}")
    print(f"Total gardens managed: {len(gardens)}")
