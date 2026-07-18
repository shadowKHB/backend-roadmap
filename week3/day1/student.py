# class variables = Shared among all instances of a class
#                   defined outside the constructor
#                   Allow you to share data among all objects created from that class
class Student:

    class_year = 2024
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

