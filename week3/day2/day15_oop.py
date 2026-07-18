# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent wich inherits from another parent 
#                          C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")    


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.sleep()



# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color 
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")    

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm²")
        

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm²")
        

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2 }cm²")    


circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("yellow", True, 7, 8)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

circle.describe()
print()
square.describe()
print()
triangle.describe()



# Polymorphism = Greek work that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form 

#                TWO WAYS TO ACHIEVE POLYMORPHISM     
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

# 1. Inheritance

from abc import ABC, abstractmethod
class Shape1:
    
    @abstractmethod
    def area(self):
        pass
    

class Circle1(Shape1):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
        


class Square1(Shape1):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    


class Triangle1(Shape1):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
    

class Pizza(Circle1):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle1(4), Square1(5), Triangle1(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")




# 2. "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                    Object must have the minimum necessary attributes/methods
#                    "If it looks like a duck and quacks like a duck, it must be a duck"     

class Animal1:
    alive = True

class Dog(Animal1):
    def speak(self):
        print("WOOF!")

class Cat(Animal1):
    def speak(self):
        print("MEOW!")

class Car:
    
    alive = False

    def speak(self):
        print("HONK!")



animals = [Dog(), Cat(), Car()]                        

for animal in animals:
    animal.speak()
    print(animal.alive)