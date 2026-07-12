# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable                          
# [1] Object contains data that can be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ----------------------------------------------
# Iterator
# [1] Object used to iterate over iterable using next() method return 1 element at a time
# [2] You can generate Iterator from iterable when using iter() method
# [3] For loop already calls iter() method on the Iterable behind the scene
# [4] Gives "StopIteration" if theres no next element
# ----------------------------------------------

myString = "Khaled"

# myList = [1, 2, 3, 4, 5]

# for letter in myString:
#     print(letter, end=' ')

# for number in myList:
#     print(number, end=" ")


myIterator = iter(myString)

print(next(myIterator)) # print the first element
print(next(myIterator)) # print the second element
print(next(myIterator)) # print the third element
print(next(myIterator)) # print the fourth element
print(next(myIterator)) # print the fifth element
print(next(myIterator)) # print the last element

# for letter in 'khaled': == for letter in iter('khaled')



# ----------------      
# -- Generators --                
# ----------------                      
# [1] Generator is a Function with "yield" Keyword instead of "return"
# [2] It support iteration and return generator iterator by calling "yield"
# [3] Generator Function can have one or more "yield"
# [4] By using next() it resume from where it called "yield" not from begining
# [5] When called, Its Not start automatically, its only give you the control
# -------------------------------------------------------------------

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

# print(myGenerator())    

myGen = myGenerator()
print(next(myGen))
print("Hello world")
print(next(myGen))
print("Hello world")
print('#' * 20)
for number in myGen:
    print(number)
