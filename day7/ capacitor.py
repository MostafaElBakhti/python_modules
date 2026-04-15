from ex1.factories import HealingCreatureFactory, TransformCreatureFactory


def demo_healing_factory(factory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def demo_transform_factory(factory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    demo_healing_factory(healing_factory)

    print()
    print("Testing Creature with transform capability")
    demo_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
