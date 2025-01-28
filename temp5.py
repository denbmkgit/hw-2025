class Human:
    def __init__(self, name, group):
        super().__init__(group)
        self.name = name
        super().about()

    def info(self):
        print(f'Hello my name is {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} study in group {self.group}')


class Student(Human, StudentGroup):
    # pass
    def __init__(self, name, place, group):
        super().__init__(name, group)  # The same
        #     # Human.__init__(self, name)     # The same
        self.place = place
        super().info()



# human = Human('Denis', 136)
# print(human.name)
student = Student('Max', 'Urban', 'Python 136')
print(student.name)
print(student.place)
print(Student.mro())
student.about()
# print(Human.mro())