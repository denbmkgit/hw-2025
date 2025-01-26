#
# class User:
#     def __new__(cls, *args, **kwargs):
#         print('Я в нью')
#         return super().__new__(cls)
#
#     def __init__(self, *args, **kwargs):
#         print('Я в ините')
#         self.args = args
#         self.kwargs = kwargs
#         # self.name = kwargs.get('name')
#         # self.age = kwargs.get('age')            # Но МОЖНО и так как ниже - setattr
#         # self.hight = kwargs.get('hight')
#         # self.weight = kwargs.get('weight')
#
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
#
# other = [1, 2, 3]
# user = {'name': 'Den', 'age': 25, 'weight': 90}
#
#
# user1 = User(*other, **user)
# user2 = User(other, user, name='Denden', age=53, hight=185)
# print('user1', user1.args)
# print('user1', user1.kwargs)
# print('user2', user2.args)
# print('user2', user2.kwargs)
# # print(user2.weight)
























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
#
# print(object)

class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)

ex = Example('data', second=25, third=3.14)