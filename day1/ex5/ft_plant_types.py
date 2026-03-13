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
                  age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.height * 3} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                  age: int, harvest_season: str,
                  nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

if __name__ == "__main__":
    flower : Flower = Flower("Rose",25,30,"red")
    flower2 : Flower = Flower("Lily",30,45,"white")
    tree : Tree = Tree("Oak",500,1825,50)
    tree2 : Tree = Tree("Maple",300,1095,30)
    vegetable : Vegetable = Vegetable("Tomato",80,90,"summer","C")
    vegetable2 : Vegetable = Vegetable("Carrot",40,60,"fall","A")
    print("=== Garden Plant Types ===\n")
    print(f"{flower.name} (Flower): {flower.height}cm, {flower.age} days, {flower.color} color")
    print(f"{flower2.name} (Flower): {flower2.height}cm, {flower2.age} days, {flower2.color} color")
    flower.bloom()
    flower2.bloom()
    print("\n")
    print(f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, {tree.trunk_diameter} diameter")
    print(f"{tree2.name} (Tree): {tree2.height}cm, {tree2.age} days, {tree2.trunk_diameter} diameter")
    tree.produce_shade()
    tree2.produce_shade()
    print("\n")
    print(f"{vegetable.name} (Vegetable): {vegetable.height}cm, {vegetable.age} days, {vegetable.harvest_season} harvest")
    print(f"{vegetable2.name} (Vegetable): {vegetable2.height}cm, {vegetable2.age} days, {vegetable2.harvest_season} harvest")
    print(f"{vegetable.name} is rich in Vitamin {vegetable.nutritional_value}")
    print(f"{vegetable2.name} is rich in Vitamin {vegetable2.nutritional_value}")