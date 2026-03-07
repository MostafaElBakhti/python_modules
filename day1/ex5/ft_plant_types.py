class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

class Flower(Plant):
    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name: str, height: int,
                  age: int, trunk_diameter: str) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: str = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} is providing shade with its branches.")

class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                  age: int, harvest_season: str,
                  nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    