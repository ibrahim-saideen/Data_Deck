from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import healtype, transtype
from typing import cast


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, c: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, c: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):

    def __str__(self) -> str:
        return ('Normal')

    def is_valid(self, c: Creature) -> bool:
        if hasattr(c, 'attack'):
            return (True)
        else:
            return (False)

    def act(self, c: Creature) -> None:
        print(c.attack())


class AggressiveStrategy(BattleStrategy):

    def __str__(self) -> str:
        return ('Aggressive')

    def is_valid(self, c: Creature) -> bool:
        if hasattr(c, 'revert') and hasattr(c, 'transform'):
            return (True)
        else:
            return (False)

    def act(self, c: Creature) -> None:
        t = cast(transtype, c)
        try:
            print(t.transform())
            print(t.attack())
            print(t.revert())
        except Exception:
            print('Battle error, aborting tournament: '
                  'Invalid Creature ’Flameling’ for this '
                  'aggressive strategy')


class DefensiveStrategy(BattleStrategy):

    def __str__(self) -> str:
        return ('Defensive')

    def is_valid(self, c: Creature) -> bool:
        if hasattr(c, 'heal'):
            return (True)
        else:
            return (False)

    def act(self, c: Creature) -> None:
        t = cast(healtype, c)
        print(t.attack())
        print(t.heal())
