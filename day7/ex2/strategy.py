from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature):
        pass

    @abstractmethod
    def act(self, creature):
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature):
        return True

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}'"
                            f" for this normal strategy")

        print(creature.attack())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return hasattr(creature, "heal")

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}'"
                            f" for this defensive strategy")

        print(creature.attack())
        print(creature.heal())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return hasattr(creature, "transform")

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}'"
                            f" for this aggressive strategy")

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
