# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position 

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Khaled", "Manager")
employee2 = Employee("Serine", "Cashier")
employee3 = Employee("Mohammed", "Cook")


print(Employee.is_valid_position("Cook"))    
print(employee1.get_info())        
print(employee2.get_info())        
print(employee3.get_info())        




# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

class Student:


    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"  

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count :.2f}"

student1 = Student("Khaled", 19.5)
student2 = Student("Serine", 19.5)
student3 = Student("Taher", 19)


print(Student.get_count())    
print(Student.get_average_gpa())