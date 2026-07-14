# =========================
# M1 - Word Lengths
# =========================
# Write a function word_lengths(sentence) that returns a dictionary where
# each key is a word and each value is its length.
# Use a comprehension inside the function.

def word_lengths(sentence):
    return {word: len(word) for word in sentence.split()}

sentence = input("Enter a sentence: ")
print("The dictionary is: ")
print(word_lengths(sentence))
        


# =========================
# M2 - User Profile Builder
# =========================
# Write a function using **kwargs that builds and returns a user profile
# dictionary. Keys should be things like name, age, city.
# Print the result formatted cleanly.

def build_profile(**kwargs):
    return kwargs

profile = build_profile(name="khaled", age= 20, city="Algiers", job="Developer")
print(profile)



# =========================
# M3 - Fibonacci Generator
# =========================
# Write a generator function fibonacci(n) that yields the first n
# Fibonacci numbers. Loop through it and print each one.

n = int(input("Enter a number: "))
def fibonacci(n):
    a = 0
    b = 1 
    
    for i in range(n):
        yield a
        a , b = b , a + b

for num in fibonacci(n):
    print(num)

# =========================
# M4 - Flatten Nested List
# =========================
# Write a function flatten(nested_list) that takes a list of lists and
# returns a single flat list using a list comprehension.
# Example: [[1,2],[3,4],[5,6]] → [1,2,3,4,5,6]
nested_list = [[1, 2],
               [3, 4],
               [5, 6]]

def flatten(nested_list):
    liste = [ item for ligne in nested_list for item in ligne]
    return liste

print(flatten(nested_list))



# =========================
# M5 - Most Frequent Element
# =========================
# Write a function most_frequent(lst) that takes a list and returns
# the most frequently occurring element.
# Use a dictionary to count occurrences inside the function.

lst = [1, 3, 3, 2, 1, 3, 2, 1, 1]
def most_frequent(lst):
    dic = {}
    for item in lst:
        if item in dic:
            dic[item] += 1
        else: 
            dic[item] = 1    
    most_freq = None
    highest_count = 0      
    for key, value in dic.items():
        if value > highest_count:
            highest_count = value
            most_freq = key
    return most_freq
print(f"The most frequently occurring element is: {most_frequent(lst)}")        


    




# =========================
# M6 - Day of the Week
# =========================
# Use match-case to write a function get_day(number) that takes a number
# 1-7 and returns the corresponding day name.
# Handle invalid numbers with a default case.
number = int(input("Enter a number (1-7): "))
def get_day(number):
    match number:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid number"

print(get_day(number))