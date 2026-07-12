# Match-case statement (switch): An alternativeto using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def day_of_week (day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"

print(day_of_week(1))        



# Module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in on your own)       
#          useful to break up a large program reusable separate files

# import math
# import math as m
# print(m.pi)

# from math import pi 
# print(pi) 

import example 

result1 = example.pi
result2 = example.square(3)
result3 = example.cube(3)
result4 = example.circumference(3)
result5 = example.area(3)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)



# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()



# if __name__ == __main__: (this script can be imported OR run standalone)
#                          Functions and classes in this module can be reused
#                          without the main block of code executing

# The file you RUN DIRECTLY  →  __name__ = '__main__'
# The file you IMPORT        →  __name__ = its filename

