from ex0 import FlameFactory, AquaFactory, CreatureFactory


def creat_creature(factory: CreatureFactory) -> None:
    print("\nTesting factory")
    base_creature = factory.create_base()
    evole_creature = factory.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())

    print(evole_creature.describe())
    print(evole_creature.attack())


def fight(factory1: CreatureFactory,
          factory2: CreatureFactory
          ) -> None:
    print('\nTesting battle')

    base_creature1 = factory1.create_base()
    base_creature2 = factory2.create_base()

    print(base_creature1.describe())
    print('vs.')
    print(base_creature2.describe())
    print('fight!')
    print(base_creature1.attack())
    print(base_creature2.attack())


def main() -> None:
    creat_creature(FlameFactory())
    creat_creature(AquaFactory())

    fight(FlameFactory(), AquaFactory())


if __name__ == '__main__':
    main()
