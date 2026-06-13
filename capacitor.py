from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import creature

def creat_heal_creature(healing: creature) -> None:
    
    print(healing.describe())
    print(healing.attack())
    print(healing.heal())
    

def creat_trans_creature(trans: creature) -> None:
    
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