from abc import ABC, abstractmethod
from ex0 import Creature

class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, c: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, c: Creature) -> str:
        ...


class NormalStrategy(BattleStrategy):

    def is_valid(self, c: Creature) -> bool:
        if 'attack' in c.__dict__:
            return (True)
        else:
            return (False)
    
    def act(self, c: Creature) -> None:
        print(c.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, c: Creature) -> bool:
        if 'transform' and 'revert' in c.__dict__:
            return (True)
        else:
            return (False)
    
    def act(self, c: Creature) -> None:
        
        try:
            print(c.transform())
            print(c.attack())
            print(c.revert())
        except Exception as e:
            print(e)

class DefensiveStrategy(BattleStrategy):

    def is_valid(self, c:Creature) -> bool:
        if 'heal' in c.__dict__:
            return (True)
        else:
            return (False)

    def act(self, c: Creature) -> None:
        print(c.attack())
        print(c.heal())

