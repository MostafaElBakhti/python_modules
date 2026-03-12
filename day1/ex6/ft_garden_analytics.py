class Plant:
    def __init__(self,name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        # self.age: int = age
        self.test: str = name
    def grow(self) -> None :
        self.height += 1
        print(f"{self.name} grew 1cm")

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str)-> None:
        super().__init__(name,height)
        self.color = color

    def bloom(self)-> None:
        print(f"{self.name} is blooming")

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points : int):
        super().__init__(name,height,color)
        self.points: int = points

class GardenManager:
    def __init__(self,owner:str):
        self.owner: str = owner
        self.plants: list[Plant] = []

    def add_plant(self,plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")
    
    def help_plants_grow(self)->None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def show_report(self)->None : 
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant,PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.points}")
            elif isinstance(plant,FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name} Tree: {plant.height}cm")
            


if __name__ == "__main__":
    tree : Plant = Plant("Oak", 500)
    flower : FloweringPlant = FloweringPlant("Rose", 25, "red")
    prize_flower : PrizeFlower = PrizeFlower("Sunflower", 30, "yellow", 10)
    alice  = GardenManager("Alice")
    # prize_flower.grow()
    alice.add_plant(tree)
    alice.add_plant(flower)
    alice.help_plants_grow()
    alice.show_report()
