from ex0.concrete_factories import FlameFactory, AquaFactory
from ex0.CreatureFactory import CreatureFactory


def demo_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing Factory")
    demo_factory(flame_factory)
    print()
    print("Testing Factory")
    demo_factory(aqua_factory)
    print()
    print("Testing battle")
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
