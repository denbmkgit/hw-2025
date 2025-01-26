# module 5.hard









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
