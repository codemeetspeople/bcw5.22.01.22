from abc import ABC, abstractmethod

ANIMALS = {}


def animal_in_zoo(cls_):
    if cls_.get_title() not in ANIMALS:
        ANIMALS[cls_.get_title()] = cls_


class Animal(ABC):
    @classmethod
    def get_title(cls):
        return cls.__name__.lower()

    @classmethod
    @abstractmethod
    def make_sound(cls):
        pass


@animal_in_zoo
class Wolf(Animal):
    @classmethod
    def make_sound(cls):
        print(f'{cls.get_title()} say wooo-wooo!')

    @staticmethod
    def moon():
        print(f'All wolfs makes ...!')


@animal_in_zoo
class Tiger(Animal):
    @classmethod
    def make_sound(cls):
        print(f'{cls.get_title()} say grrr-grrr!')


@animal_in_zoo
class Hog(Animal):
    @classmethod
    def make_sound(cls):
        print(f'{cls.get_title()} say hrrr-hrrr!')
