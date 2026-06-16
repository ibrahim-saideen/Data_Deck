from abc import ABC, abstractmethod
from ex0 import Creature, CreatureFactory


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):

    state: bool

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Sproutling(Creature, HealCapability,):

    name = 'Sproutling'
    type = 'Grass'

    def describe(self) -> str:
        return super().describe()

    def attack(self) -> str:
        return (f'{self.name} uses Vine Whip!')

    def heal(self) -> str:
        return ('Sproutling heals itself '
                'for a small amount')


class Bloomelle(Creature, HealCapability):

    name = 'Bloomelle'
    type = 'Grass/Fairy'

    def describe(self) -> str:
        return super().describe()

    def attack(self) -> str:
        return (f'{self.name} uses Petal Dance!')

    def heal(self) -> str:
        return ('Bloomelle heals itself and '
                'others for a large amount')


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        spr = Sproutling()
        return (spr)

    def create_evolved(self) -> Creature:
        blo = Bloomelle()
        return (blo)


class Shiftling(Creature, TransformCapability):

    name = 'Shiftling'
    type = 'Normal'
    state = False

    def describe(self) -> str:
        return super().describe()

    def transform(self) -> str:
        self.state = True
        return ('Shiftling shifts into a sharper form!')

    def revert(self) -> str:
        self.state = False
        return ('Shiftling returns to normal.')

    def attack(self) -> str:

        if self.state:
            return ('Shiftling performs a boosted strike!')
        else:
            return ('Shiftling attacks normally.')


class Morphagon(Creature, TransformCapability):
    name = 'Morphagon'
    type = 'Normal/Dragon'
    state = False

    def describe(self) -> str:
        return super().describe()

    def transform(self) -> str:
        self.state = True
        return ('Morphagon morphs into a dragonic battle form!')

    def revert(self) -> str:
        self.state = False
        return ('Morphagon stabilizes its form.')

    def attack(self) -> str:

        if self.state:
            return ('Morphagon unleashes a devastating morph strike!')
        else:
            return ('Morphagon attacks normally.')


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        shif = Shiftling()
        return (shif)

    def create_evolved(self) -> Creature:
        mor = Morphagon()
        return (mor)
