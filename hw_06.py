# module 6.3 old
class Horse:
    def __init__(self):         # создали метод инит - нечего не передаем сюда (кроме самого объекта)
        self.x_distance = 0     # При создании объекта дистанция у него 0
        self.sound = 'Frrr'     # При создании объекта ом може "издавать" звук Фррр


    # x_distance = 0
    # sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self):      # создали метод инит - нечего не передаем сюда (кроме самого объекта)
        self.y_distance = 0  #  При создании объекта дистанция у него 0
        self.sound = 'I train, eat, sleep, and repeat'    # При создании объекта ом може "сказать" фразу "Я ...


    # y_distance = 0
    # sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):             #  Созадли метод литеть и передаем сюда дистанцию
        self.y_distance += dy       # дистанция объкта при вызове этого метода увеличиться на велечину ДУ
        return self.y_distance       # метод возвращает новую "дистанцию" объекта (точку на оси У)


    # def fly(self, dy):
    #         self.y_distance += dy
    #         return self.y_distance

class Pegasus (Horse, Eagle):

    def __init__(self):       # Создали метод инит, в который нечего не передаем, кроме самого объекта
        super().__init__()    # сказали, что бы "запустил" инит в Лошади и принял все значения от туда
        Eagle.__init__(self)  # сказали, что бы "запустил" инит в Орле и принял все значения от туда
    # def __init__(self):
    #     super().__init__()
    #     Eagle.__init__(self)

    def move(self, dx, dy):  #  созадли метод двингаться
        self.run(dx)        #  запустили метод Бежать и передали туда "дистацию" (на какое значение увеличиться ДХ - Х)
        self.fly(dy)        #  запустили метод Лететь и передали туда "дистацию" (на какое значение увеличиться ДУ - У)

    # def move(self, dx, dy):
    #     self.run(dx)
    #     self.fly(dy)

    def get_pos(self):       #    созадли метод дай позицию (покажи, скажи свою позицию)
        return (self.x_distance, self.y_distance)  # вернули позицию объекта по осям Х и У

    # def get_pos(self):
    #     return (self.x_distance, self.y_distance)

    def voice(self):         #  создали метод "подай голос"
        print(self.sound)    # печатаем "голосом" того кто сейчас "круче" - "Первее", Левее или правее???

    # def voice(self):
    #     print(self.sound)

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
print(Pegasus.mro())
# # ТО Что было решено раньше:
# class Horse:   # Создали в бдующем родительский класс Лошадь
#
#     def __init__(self):         # создали метод инит - нечего не передаем сюда (кроме самого объекта)
#         self.x_distance = 0     # При создании объекта дистанция у него 0
#         self.sound = 'Frrr'     # При создании объекта ом може "издавать" звук Фррр
#
#     def run(self, dx):         #   Созадли метод бежать и передаем сюда дистанцию
#         self.x_distance += dx  #   дистанция объкта при вызове этого метода увеличиться на велечину ДХ
#         return self.x_distance #   метод возвращает новую "дистанцию" объекта (точку на оси Х)
#
# class Eagle:                 # Создали в бдующем родительский класс Орел, который будет "за" Лошадью
#
#     def __init__(self):      # создали метод инит - нечего не передаем сюда (кроме самого объекта)
#         self.y_distance = 0  #  При создании объекта дистанция у него 0
#         self.sound = 'I train, eat, sleep, and repeat'    # При создании объекта ом може "сказать" фразу "Я ...
#
#     def fly(self, dy):             #  Созадли метод литеть и передаем сюда дистанцию
#         self.y_distance += dy       # дистанция объкта при вызове этого метода увеличиться на велечину ДУ
#         return self.y_distance       # метод возвращает новую "дистанцию" объекта (точку на оси У)
#
#
# class Pegasus(Horse, Eagle): #  Создали дочерний Лошади и Орла - класс Пегас
#
#     def __init__(self):       # Создали метод инит, в который нечего не передаем, кроме самого объекта
#         super().__init__()    # сказали, что бы "запустил" инит в Лошади и принял все значения от туда
#         Eagle.__init__(self)  # сказали, что бы "запустил" инит в Орле и принял все значения от туда
#
#     def move(self, dx, dy):  #  созадли метод двингаться
#         self.run(dx)        #  запустили метод Бежать и передали туда "дистацию" (на какое значение увеличиться ДХ - Х)
#         self.fly(dy)        #  запустили метод Лететь и передали туда "дистацию" (на какое значение увеличиться ДУ - У)
#
#     def get_pos(self):       #    созадли метод дай позицию (покажи, скажи свою позицию)
#         return (self.x_distance, self.y_distance)  # вернули позицию объекта по осям Х и У
#
#     def voice(self):         #  создали метод "подай голос"
#         print(self.sound)    # печатаем "голосом" того кто сейчас "круче" - "Первее", Левее или правее???
#
#
# p1 = Pegasus()              # Созадли объект Пегас_1
#
#
# print(p1.get_pos())          # Вывводим позицию Пегаса 1
# p1.move(10, 15)      # Сказали (вызвали метод Дивигайся) пегасу увиличить ДХ на 10 ДУ  на 15
# print(p1.get_pos())          # Вывводим позицию Пегаса 1 (должно быть 10, 15)
# p1.move(-5, 20)          # Сказали (вызвали метод Дивигайся) пегасу увиличить ДХ на -5 ДУ  на 20
# print(p1.get_pos())           # Вывводим позицию Пегаса 1 (должно быть 5, 35)
#
# p1.voice()  # Сказали (вызвали метод Голос) скажи тем голосом кто сейчас активен "круче",    И так как
# # сначала был вызван инит Лошади, а уже ПОТОМ инит Орла, инит Орла "переопределил" - "перезаписал" sound на Орлиный,
# # поэтому Пегас теперь говорит голосом Орла 'I train, eat, sleep, and repeat'


















# module 6.3 new
# from random import randint
# class Animal:
#     live = True
#     sound = None
#     _DEGREE_OF_DANGER =0
#
#     def __init__(self, _cords=[0, 0, 0], speed=int):
#         self._cords = _cords
#         self.speed = speed
#
#     def move(self, dx, dy, dz):
#         new_x = int(self._cords [0]) + dx * self.speed
#         new_y = self._cords [1] + dy * self.speed
#         new_z = self._cords [2] + dz * self.speed
#         if new_z < 0:
#             print("It's too deep, i can't dive :(")
#         else:
#             self._cords = [new_x, new_y, new_z]
#
#     def get_cords(self):
#         print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
#
#     def attack(self):
#         if self._DEGREE_OF_DANGER < 5:
#             print("Sorry, i'm peaceful :)")
#         else:
#             print("Be careful, i'm attacking you 0_0")
#
# class Bird(Animal):
#     beak =True
#
#     def lay_eggs(self):
#         random_eggs = randint(1, 4)
#         print(f'Here are(is) {random_eggs} eggs for you"')
#
#
# class AquaticAnimal(Animal):
#     _DEGREE_OF_DANGER = 3
#
#     def dive_in(self, dz):
#         if self._cords[2] < 0:
#             new_z = self._cords[2] - abs(dz) * .5 * self.speed  # ВЗЯЛ В ИНЕТЕ
#             self._cords[2] = max(new_z, 0)                      # ВЗЯЛ В ИНЕТЕ
#             self._cords[0] = self._cords[0]
#             self._cords[1] = self._cords[0]
#
#         #     self.speed = self.speed / 2
#         # self._cords[2] -= dz
#
#
# class PoisonousAnimal(Animal):
#     _DEGREE_OF_DANGER = 8
#
#
# class Duckbill(AquaticAnimal, Bird, PoisonousAnimal):
#     sound = "Click-click-click"
#
#     def __init__(self, speed):
#         super().__init__(_cords=[0,0,0], speed=speed)
#     # def __init__(self,sound):
#     #     self.sound = "Click-click-click"
#     def speak(self):                                       # ВЗЯЛ В ИНЕТЕ
#         print(self.sound)                                  # ВЗЯЛ В ИНЕТЕ
#
# db = Duckbill(10)
#
# print(db.live)
# print(db.beak)
#
#
# db.speak()
# db.attack()
#
# db.move(1, 2, 3)
# db.get_cords()
# db.dive_in(6)
# db.get_cords()
#
# db.lay_eggs()

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
