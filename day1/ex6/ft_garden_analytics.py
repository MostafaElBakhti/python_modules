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

class PrizeFlower(FloatingPointError):
    def __init__(self, name: str, height: int, color: str, points : int):
        super().__init__()