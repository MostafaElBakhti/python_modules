from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def fight(c1, strategy1, c2, strategy2) -> bool:
    print("* Battle *")
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("now fight!")

    if not strategy1.is_valid(c1) or not strategy2.is_valid(c2):
        print("Battle error, aborting tournament: incompatible strategy")
        return False

    strategy1.act(c1)
    strategy2.act(c2)
    return True


def battle(opponents: list[tuple]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            if not fight(c1, strategy1, c2, strategy2):
                return


def main() -> None:
    print("Tournament 0 (basic)")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()

    print("Tournament 1 (error)")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()

    print("Tournament 2 (multiple)")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()
