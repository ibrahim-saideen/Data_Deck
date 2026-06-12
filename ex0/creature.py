from abc import ABC, abstractmethod


class Creature(ABC):

    name: str
    type: str

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return (f'{self.name} is a {self.type} type Creature')


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class Flameling(Creature):

    name = 'Flameling'
    type = 'Fire'

    def attack(self) -> str:
        return (f'{self.name} uses Ember!')


class Pyrodon(Creature):

    name = 'Pyrodon'
    type = 'Fire/Flying'

    def attack(self) -> str:
        return (f'{self.name} uses Flamethrower!')


class Aquabub(Creature):

    name = 'Aquabub'
    type = 'Water'

    def attack(self) -> str:
        return (f'{self.name} uses  Water Gun!')


class Torragon(Creature):

    name = 'Torragon'
    type = 'Water'

    def attack(self) -> str:
        return (f'{self.name} uses Hydro Pump!')


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        flam = Flameling()
        return (flam)

    def create_evolved(self) -> Creature:
        pyr = Pyrodon()
        return (pyr)


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        aqua = Aquabub()
        return (aqua)

    def create_evolved(self) -> Creature:
        torr = Torragon()
        return (torr)
