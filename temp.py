class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third, fourth):
        print(first)
        print(second)
        print(third)
        print(fourth)

ex = Example('data', second=25, third=3.14, fourth=44)
'''
('data',)                             # print(args)
{'second': 25, 'third': 3.14}                      # print(kwargs)
data                                  # print(first)
25                                               # print(second)
3.14                                                   # print(third)
'''