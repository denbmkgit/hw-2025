# module 6.3
from random import randint
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER =0

    def __init__(self, _cords=[0, 0, 0], speed=int):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords = [f'{dx}', f'{dy}', f'{dz}']

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak =True

    def lay_eggs(self):
        random_eggs = randint(1, 4)
        print(f'Here are(is) {random_eggs} eggs for you"')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self):
        super().__init__()

    def dive_in(self, dz):
        if self._cords[2] < 0:
            self.speed = self.speed / 2

        self._cords[2] -= dz


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    # def __init__(self,sound):
    #     self.sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()





# # module 6.2
# class Vehicl:
#     __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
#     def __init__(self, owner=str, __model=str, __engine_power=str, __color=str):
#         self.owner = owner
#         self.__model = __model
#         self.__engine_power = __engine_power
#         self.__color = __color
#
#     def get_model(self):
#         return f'Модель: {self.__model}'
#
#     def get_horsepower(self):
#         return f'Мощность двигателя: {self.__engine_power}'
#
#     def get_color(self):
#         return f'Цвет: {self.__color}'
#
#     def print_info(self):
#         print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \n{self.owner}')
#
#     def set_color(self, new_color=str):
#         if new_color.upper() in map(str.upper,self.__COLOR_VARIANTS):
#             self.__color = new_color
#         else:
#             print(f'Нельзя сменить цвет на {new_color}')
#
# class Sedan(Vehicl):
#     __PASSENGERS_LIMIT = 5
#
#
# # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
# vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
#
# # Изначальные свойства
# vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
# vehicle1.print_info()

# # module 6.1
# class Animal:
#     alive = True
#     fed = False
#
#     def __init__(self, name):
#             # self.name = name
#
#
#     def eat(self, food):
#         # if isinstance(food, Fruit):  # Можно так, если переданный параметр будет из класса Fruit, то ...
#         if food.edible == True:
#             print(f'{self.name} съел {food.name}')
#             self.fed = True
#         else:
#             print(f'{self.name} не стал есть {food.name}')
#             self.alive = False
#
# class Plant:
#     edible = False
#
#     def __init__(self, name):
#         self.name = name
#
# class Mammal(Animal):
#     pass
#
#
# class Predator(Animal):
#     pass
#
#
# class Flower(Plant):
#     pass
#
#
# class Fruit(Plant):
#     edible = True
#
# a1 = Predator('Волк с Уолл-Стрит')
# a2 = Mammal('Хатико')
# p1 = Flower('Цветик семицветик')
# p2 = Fruit('Заводной апельсин')
#
# print(a1.name)
# print(p1.name)
#
# print(a1.alive)
# print(a2.fed)
# a1.eat(p1)
# a2.eat(p2)
# print(a1.alive)
# print(a2.fed)
