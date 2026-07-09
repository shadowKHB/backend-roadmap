# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")
print()


name = "Khaled KHB"

for character in name:
    print(character, end=" ")
print()


my_dictionary = {"A": 1, 
                 "B": 2,
                 "C": 3}

for key, value in my_dictionary.items():
    print(f"{key}= {value}")



# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in 
#                        2. not in

word = "Hello"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a '{letter}' ")
else:
    print(f"'{letter}' was not found")


students = {"Khaled", "Taher", "Malik"}
student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not found")  
else:
    print(f"{student} is a student")  


grades = {"Khaled": "A",
          "Taher": "B",
          "Malik": "C",
          "Mohammed": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")



# List comprehension = A concise way to create lists in python 
#                      Compact and easier to read than traditional loops 
#                      [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z ** 2 for z in range(1, 11)]
print(f"doubles: {doubles}") 
print(f"triples: {triples}") 
print(f"squares: {squares}") 

fruits = ["apples", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num > 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(f"Positive numbers: {positive_nums}")
print(f"Negative numbers: {negative_nums}")
print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")


grades = [80, 34, 25, 70, 66, 99, 59]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

# ===== M3 Rewrite =====

# =========================
# M3 - Separate Evens and Odds
# =========================
# Write a program that takes a list of numbers and separates them into two 
# new lists: evens and odds. Print both lists.


numbers = [0, 5, 7, 2, 20, 25, 15, 13, 6]
odds = [num for num in numbers if num % 2 == 1]
evens = [num for num in numbers if num % 2 == 0]

print(f"The odd numbers are: {odds}")
print(f"The even numbers are: {evens}")