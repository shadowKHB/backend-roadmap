# =========================
# H1 - Caesar Cipher
# =========================
# Write a function caesar_cipher(text, shift, mode) where mode is either
# "encrypt" or "decrypt". Use ord() and chr() to shift each letter by
# the shift amount. Non-letter characters stay unchanged.
# Test both modes with the same message to verify they are inverse operations.

def caesar_cipher(text, shift, mode):
    if mode == "encrypt":
        text_encrypted = ""
        for caractere in text:
            if caractere.isalpha():
                if caractere.isupper():
                    text_encrypted += chr((ord(caractere) - ord("A") + shift) % 26 + ord("A"))
                elif caractere.islower():
                    text_encrypted += chr((ord(caractere) - ord("a") + shift) % 26 + ord("a"))    
            else:
                 text_encrypted += caractere   

        return text_encrypted
    
    elif mode == "decrypt":
        text_decrypted = ""
        for caractere in text:
            if caractere.isalpha():
                if caractere.isupper():
                    text_decrypted += chr((ord(caractere) - ord("A") - shift) % 26 + ord("A"))
                elif caractere.islower():
                    text_decrypted += chr((ord(caractere) - ord("a") - shift) % 26 + ord("a"))    
            else:
                 text_decrypted += caractere

        return text_decrypted

    else:
        return "Error! Invalid mode"


text = input("Enter a text: ")
shift = int(input("Enter the number of shift: "))
mode = input("Enter the mode (encrypt/decrypt): ")
print(caesar_cipher(text,shift,mode))



# =========================
# H2 - Group By Length
# =========================
# Write a function group_by_length(words) that takes a list of words and
# returns a dictionary grouping them by their length.
# Example: ["hi", "hey", "hello", "bye"] → {2: ["hi"], 3: ["hey", "bye"], 5: ["hello"]}

words = ["hi", "hey", "hello", "bye", "python", "cat", "go"]

def group_by_length(words):
    dic = {}
    for word in words:
        length = len(word)
        if length in dic.keys():
            dic[length].append(word)
        else:
            dic[length] = [word]
    return dic            

print(f"{words} => {group_by_length(words)}")

# =========================
# H3 - Students Report
# =========================
# Build a students_report(students) function that takes a list of
# dictionaries (each with "name" and "grades" keys, where grades is a
# list of numbers), calculates each student's average, and returns a
# sorted list of (name, average) tuples — highest average first.
# Use functions, comprehensions, and your knowledge of dictionaries.

students = [
    {"name": "Khaled", "grades": [85, 90, 78, 92]},
    {"name": "Mohammed", "grades": [70, 65, 80, 75]},
    {"name": "Taher", "grades": [95, 88, 92, 97]},
]


def student_report(students):
    lis = [(student["name"],sum(student["grades"])/len(student["grades"]) )for student in students]
    return sorted(lis, key=lambda x : x[1], reverse = True)

print(student_report(students))

# =========================
# H4 - Number Filter Generator
# =========================
# Write a generator number_filter(numbers, condition) where condition is
# a function passed as an argument. The generator should yield only numbers
# from the list where condition(number) is True.
# Test it with at least 2 different condition functions
# (example: is_even, is_greater_than_10).

def number_filter(numbers, condition):
    for number in numbers:
        if condition(number):
            yield number

def is_even(n):
    return n % 2 == 0

def is_greater_than_10(n):
    return n > 10

numbers = [1, 4, 7, 12, 3, 18, 5, 20, 9, 15]

# Test 1:
for num in number_filter(numbers, is_even):
    print(num, end=' ')
print()
 
# Test 2:
for num in number_filter(numbers, is_greater_than_10):
    print(num, end=' ')
print()

