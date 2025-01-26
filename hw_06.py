# module 6.1
class Animal:
    def __init__(self, alive, fed, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, adble, name):
        self.edble = False
        self.name = name

class Mammal(Animal):
    pass



class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    pass

