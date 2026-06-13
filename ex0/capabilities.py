from abc import ABC, abstractmethod
from .creature import Creature, CreatureFactory

class HealCapability(ABC):

    @abstractmethod
    def heal() -> str:
        ...


class TransformCapability(ABC):

    state: bool
    @abstractmethod
    def transform() -> str:
        ...
    
    @abstractmethod
    def revert() -> str:
        ...


class Sproutling(Creature,HealCapability):
    
    name = 'Sproutling'
    type = 'Grass'
    def describe(self) -> str:
        return super().describe()

    def attack(self) -> str:
        return (f'{self.name} uses Vine Whip!')

    def heal() -> str:
        return('Sproutling heals itself '
               'for a small amount')
        


class Bloomelle(Creature, HealCapability):

    name = 'Bloomelle'
    type = 'Grass/Fairy'
    def describe(self) -> str:
        return super().describe()

    def attack(self) -> str:
        return (f'{self.name} uses Petal Dance!')
    
    def heal() -> str:
        return('Bloomelle heals itself and '
               'others for a large amount')
    
class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        spr = Sproutling()
        return(spr)
    
    def create_evolved(self) -> Creature:
        blo = Bloomelle()
        return (blo)
    

class Shiftling(Creature, TransformCapability):
    
    name = 'Shiftling'
    type = 'Normal'
    state = False

    def describe(self) -> str:
        return super().describe()
    
    def transform() -> str:
        state = True
        return ('Shiftling shifts into a sharper form!')
    
    def revert() -> str:
        state = False
        return ('Shiftling returns to normal.')
    
    def attack(self) -> str:

        if state:
            return ('Shiftling performs a boosted strike!')
        else:
            return ('Shiftling attacks normally.')



class Morphagon(Creature, TransformCapability):
    ...