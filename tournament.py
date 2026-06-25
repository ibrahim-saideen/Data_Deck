from ex0 import FlameFactory, AquaFactory, Creature
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import BattleStrategy


def battle(lst: list[tuple[Creature, BattleStrategy]]) -> None:

    print('*** Tournament ***')
    print(f'{len(lst)} opponents involved\n')
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            print('\n* Battle *')
            print(lst[i][0].describe())
            print('vs.')
            print(lst[j][0].describe())
            print('now fight!')
            lst[i][1].act(lst[i][0])
            if not lst[i][1].is_valid(lst[i][0]):
                return
            lst[j][1].act(lst[j][0])
            if not lst[j][1].is_valid(lst[j][0]):
                return


def main() -> None:

    flam = FlameFactory().create_base()
    spr = HealingCreatureFactory().create_base()
    aqua = AquaFactory().create_base()
    shif = TransformCreatureFactory().create_base()
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

    print('\nTournament 2 (multiple)')
    lst = [(aqua, normal), (spr, Defens), (shif, agg)]
    print(f'[ ({aqua}+{normal}), ({spr}+{Defens}), ({shif}+{agg})]')
    battle(lst)


if __name__ == '__main__':
    main()
