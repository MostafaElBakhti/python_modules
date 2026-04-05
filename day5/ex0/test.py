from abc import ABC, abstractmethod
import typing

class Animal(ABC):
    def __init__(self,name , action):
        self.name = name
        self.action = action

    @abstractmethod
    def animate(self) -> str:
        pass

class Dog(Animal):
    def __init__(self,name, action):
        super().__init__(name, action)

    def animate(self) -> str:
        return self.action

class Cat(Animal):
    def __init__(self,name ,action):
        super().__init__(name, action)

    def animate(self) -> str:
        return self.action
    

dog = Dog("Rex", "test")
cat = Cat("Luna", "meow")

print(dog.action)
print(dog.animate())
print(cat.action)
print(cat.animate())