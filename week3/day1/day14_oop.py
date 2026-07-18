from car import Car
from student import Student
from animal import *

print("#" * 30)

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print("CAR1:")
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale) 
car1.drive()
car1.stop()
car1.describe() 
print()

print("CAR2:")
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop() 
car2.describe() 
print()

print("CAR3:")
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
car3.drive()
car3.stop()
car3.describe() 
print()

print("#" * 30)
print()
student1 = Student("Khaled", 20)
student2 = Student("Serine", 20)
student3 = Student("Taher", 21)
student4 = Student("Mohammed", 35)


print(f"My graduating class of {Student.class_year} has {Student.num_student} students")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print()

print("#" * 30)

dog = Dog("Scooby")
cat = Cat("Garfield")
mousse = Mousse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
print()


print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
print()


print(mousse.name)
print(mousse.is_alive)
mousse.eat()
mousse.sleep()
mousse.speak()

                