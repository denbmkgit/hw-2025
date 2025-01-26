# module 5.hard
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if i[0] == nickname and i[1] == password:
                self.current_user = nickname
                print(f'identification successful for {nickname}')
                return
            print(f'Incorrect password for {nickname}')
            return
        print("Неверные данные для входа.")

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        for n in self.users:
            if n[0] == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append((nickname, password, age))
        # Обновите текущего пользователя после успешной регистрации
        self.current_user = nickname
        print(f'Пользователь {nickname} зарегистрирован')

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        list_title = []
        for v in self.videos:
            # print(v.title, 'IT IS v!!!!!!!!!!')
            if word.upper() in v.title.upper():
                list_title.append(v.title)
        return list_title

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for v in self.videos:
            if title == v.title:
                if v.adult_mode:
                    for u in self.users:
                        if u[0] == self.current_user:
                            if int(u[2]) < 18:
                                print(f'{u[0]} {u[2]} Вам нет 18 лет, пожалуйста покиньте страницу')
                                return
                for i in range(1, v.duration + 1):
                    sleep(0.2)
                    print(i, end=" ")
                print('\n Конец видео')
                return
        print("Видео не найдено.")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')









# # module 5.4
# class House:
#     houses_history = []
#
#     def __new__(cls, *args, **kwargs):
#         cls.houses_history.append(args[0])
#         return object.__new__(cls)
#     def __init__(self, name, number_of_floor):
#         self.name = name
#         self.number_of_floor = number_of_floor
#
#     def go_to(self, new_floor):
#         if self.number_of_floor < new_floor or new_floor < 1:
#             print("Такого этажа не существует")
#         else:
#             for i in range(1, new_floor + 1):
#                 print(i)
#
#     def __len__(self):
#         return self.number_of_floor
#
#     def __str__(self):
#         return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"
#
#     def __eq__(self, other):
#         if isinstance(other, House) and self.number_of_floor == other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if isinstance(other, House) and self.number_of_floor < other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __le__(self, other):
#         if isinstance(other, House) and self.number_of_floor <= other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if isinstance(other, House) and self.number_of_floor > other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __ge__(self, other):
#         if isinstance(other, House) and self.number_of_floor >= other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if isinstance(other, House) and self.number_of_floor != other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __add__(self, value):
#         if isinstance(value, int):
#             self.number_of_floor += value
#         return self
#
#     def __radd__(self, value):
#         if isinstance(value, int):
#             self.number_of_floor += value
#         return self
#
#     def __iadd__(self, value):
#         if isinstance(value, int):
#             self.number_of_floor = self.number_of_floor + value
#         return self
#         #     self.number_of_floor += value  #  Так Тоже РАБОТАЕТ
#         # return self                        #  Так Тоже РАБОТАЕТ
#
#     def __del__(self):
#         print(f"{self.name} снесён, но он останется в истории")
#
#
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
#
# # Удаление объектов
# del h2
# del h3
#
# print(House.houses_history)
# h1.go_to(10)

#
#
#
# # Про Классовый атрибут
# class Human:
#     head = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# den = Human('Den', 53)
# max = Human('Max', 33)
#
# print('HumEn have a head? - ', Human.head)
# print('Den have a head? - ', den.head)
# print(den.__dict__)
# print('Max have a head? - ', max.head)
# print(max.__dict__)
#
# Human.head = False
# den.head = True
# max.head = False
# print('HumEn have a head? - ', Human.head)
# print('Den have a head? - ', den.head)
# print(den.__dict__)
# print('Max have a head? - ', max.head)
# print(max.__dict__)
#
# # module 5.3
# class House:
#     def __init__(self, name, number_of_floor):
#         self.name = name
#         self.number_of_floor = number_of_floor
#
#     def go_to(self, new_floor):
#         if self.number_of_floor < new_floor or new_floor < 1:
#             print("Такого этажа не существует")
#         else:
#             for i in range(1, new_floor + 1):
#                 print(i)
#
#     def __len__(self):
#         return self.number_of_floor
#
#     def __str__(self):
#         return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"
#
#     def __eq__(self, other):
#         if isinstance(other, House) and self.number_of_floor == other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if isinstance(other, House) and self.number_of_floor < other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __le__(self, other):
#         if isinstance(other, House) and self.number_of_floor <= other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if isinstance(other, House) and self.number_of_floor > other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __ge__(self, other):
#         if isinstance(other, House) and self.number_of_floor >= other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if isinstance(other, House) and self.number_of_floor != other.number_of_floor:
#             return True
#         else:
#             return False
#
#     def __add__(self, value):
#         if isinstance(value, int):
#             self.number_of_floor += value
#         return self
#
#     def __radd__(self, value):
#         if isinstance(value, int):
#             self.number_of_floor += value
#         return self
#
#     def __iadd__(self, value):
#         if isinstance(value, int):
#             self.number_of_floor = self.number_of_floor + value
#         return self
#         #     self.number_of_floor += value  #  Так Тоже РАБОТАЕТ
#         # return self                        #  Так Тоже РАБОТАЕТ
#
#
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2)  # __eq__
#
# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__

# # module 5.2
# class House:
#     def __init__(self, name, number_of_floor):
#         self.name = name
#         self.number_of_floor = number_of_floor
#
#     def go_to(self, new_floor):
#         if self.number_of_floor < new_floor or new_floor < 1:
#             print("Такого этажа не существует")
#         else:
#             for i in range(1, new_floor + 1):
#                 print(i)
#
#     def __len__(self):
#         return self.number_of_floor
#
#     def __str__(self):
#         return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"
#
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))


# # module 5.1
# class House:
#     def __init__(self, name, number_of_floor):
#         self.name = name
#         self.number_of_floor = number_of_floor
#
#     def go_to(self, new_floor):
#         if self.number_of_floor < new_floor or new_floor < 1:
#             print("Такого этажа не существует")
#         else:
#             for i in range(1, new_floor + 1):
#                 print(i)
#
#
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
