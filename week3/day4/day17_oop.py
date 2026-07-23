# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class  Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"    
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author 
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Designing Data-Intensive Applications", "Martin Kleppmann", 616)    
book3 = Book("Atomic Habits", "James Clear", 320)  
book4 = Book("The Hobbit", "J.R.R Tolkien", 310)

# __str__
print(book1)
print(book2)
print(book3)

# __eq__
print(book1 == book4)

# __lt__
print(book1 < book3)
print(book2 > book3)

# __add__
print(book1 + book2)

# __contains__
print("Peace" in book2)
print("Hobbit" in book4)

# __getitem__
print(book2["title"])
print(book1["author"])
print(book4["num_pages"])
print(book3["source"])



# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width   # _ -> Private attribute
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero") 

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height= new_height
        else:
            print("Height must be greater than zero")  

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted") 

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")     


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height



# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator


def myDecorator(func):# Decorator

    def nestedFunc():
        
        print("Before")

        func() # Execute function

        print("After")

    return nestedFunc 

@myDecorator
def sayHello():
    print("Hello from say hello function")    


@myDecorator
def sayHowAreYou():
    print("Hello from say how are you function")


sayHello() 
print('#' * 25)
sayHowAreYou()   



def myDecorator2(func):
    def nestedFunc(*numbers):
        for number in numbers:
            if number < 0:
                print("Beware one of the numbers is less than zero")

        func(*numbers)

    return nestedFunc

@myDecorator2
def calculate(n1, n2, n3):
    print(n1 + n2 + n3)

calculate(-5, 90, 13)


from time import time

def speedTest(func):
    def wrapper():
        
        start = time()

        func()

        end = time()

        print(f"Function Running time is: {end - start}")
    return wrapper

@speedTest
def bigloop() :
    for number in range(1, 100000):
        print(number)        

bigloop()        