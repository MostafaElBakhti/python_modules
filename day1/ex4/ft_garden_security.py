class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height: int = 0
        self.test = 5
        self.__age: int = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: Age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"{self.name}: {self.__height}cm, {self.__age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    plant.set_age(-5)
    height: int = plant.get_height()
    age: int = plant.get_age()
    print(f"Current plant: {plant.name} ({height}cm, {age} days)")
