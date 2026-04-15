from ex0.CreatureFactory import CreatureFactory
from .healing import Sproutling, Bloomelle
from .transforming import Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):

    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
