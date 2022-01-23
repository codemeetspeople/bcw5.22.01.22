class Animal:
    def get_title(self):
        return self.__class__.__name__

    def eats(self):
        print(f'{self.get_title()} eats everything')


class Cat(Animal):
    def eats(self):
        print(f'{self.get_title()} eats fish')

    def meow(self):
        print(f'{self.get_title()} say meow...')


class Dog(Animal):
    def eats(self):
        print(f'{self.get_title()} eats meat')

    def bark(self):
        print(f'{self.get_title()} say grrr...')


class CatDog(Dog, Cat):
    def eats(self):
        print(f'{self.get_title()} eats fish and meat')


if __name__ == '__main__':
    cd = CatDog()

    cd.eats()
    super(CatDog, cd).eats()
