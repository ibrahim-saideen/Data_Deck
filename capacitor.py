from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import Creature


def creat_heal_creature(healing: Creature) -> None:

    print(healing.describe())
    print(healing.attack())
    print(healing.heal())


def creat_trans_creature(trans: Creature) -> None:

    print(trans.describe())
    print(trans.attack())
    print(trans.transform())
    print(trans.attack())
    print(trans.revert())


def main() -> None:
    base_heal = HealingCreatureFactory().create_base()
    evolv_heal = HealingCreatureFactory().create_evolved()
    base_trans = TransformCreatureFactory().create_base()
    evolv_trans = TransformCreatureFactory().create_evolved()
    print('Testing Creature with healing capability')
    print('base:')
    creat_heal_creature(base_heal)
    print('evolved:')
    creat_heal_creature(evolv_heal)
    print('\nTesting Creature with transform capability')
    print('base:')
    creat_trans_creature(base_trans)
    print('evolved:')
    creat_trans_creature(evolv_trans)


if __name__ == '__main__':
    main()
