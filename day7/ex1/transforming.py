from ex0.creature import Creature
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self):
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self):
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self):
        self._transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self):
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self):
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self):
        self._transformed = False
        return "Morphagon stabilizes its form."
