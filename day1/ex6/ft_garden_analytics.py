class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

class FloweringPlant:
    def __init__(self,name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

class PrizeFlower:
    def __init__(self,name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

class GardenManager:
    