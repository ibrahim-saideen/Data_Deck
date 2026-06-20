from ex0 import FlameFactory, AquaFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(lst) -> None:

    print('*** Tournament ***')
    print(f'{len(lst)} opponents involved\n')

    print('* Battle *')
    for i in range(len(lst)):
        print(lst[i][0].describe())
        if(i < len(lst) - 1):
            print('vs.')
    print('now fight!')

    for i in range(len(lst)):
        try:
            lst[i][1].act(lst[i][0])
        except Exception:
            return




def main() -> None:

    flam = FlameFactory().create_base()
    spr = HealingCreatureFactory().create_base()
    normal = NormalStrategy()
    Defens = DefensiveStrategy()
    agg = AggressiveStrategy()

    print('Tournament 0 (basic)')
    print(f'[ ({flam}+{normal}), ({spr}+{Defens}) ]')
    lst = [(flam, normal), (spr, Defens)]
    battle(lst)
    print('\nTournament 1 (error)')
    lst = [(flam, agg), (spr, Defens)]
    print(f'[ ({flam}+{agg}), ({spr}+{Defens}) ]')
    battle(lst)


    


if __name__ == '__main__':
    main()