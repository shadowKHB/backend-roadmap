# =========================
# E1 - Even or Odd Checker
# =========================
# Write a function is_even(n) that returns True if a number is even,
# False if odd. Call it 5 times with different numbers and print each result.


def is_even(n):
    return n % 2 == 0 

print(f"2 is even? : {is_even(2)}")
print(f"7 is even? : {is_even(7)}")
print(f"0 is even? : {is_even(0)}")
print(f"15 is even? : {is_even(15)}")    
n = int(input("Enter a number: "))    
print(f"{n} is even? : {is_even(n)}")    


# =========================
# E2 - Temperature Converter
# =========================
# Write a function celsius_to_fahrenheit(temp) that converts and returns
# the result. Add a second function fahrenheit_to_celsius(temp).
# Call both and print results.

def celsius_to_fahrenheit(temp):
        return f"{(temp * 9 / 5 + 32):.2f} F"

def fahrenheit_to_celsius(temp):
        return f"{(temp - 32) * 5 / 9:.2f} C"


unit = input("Enter the unit (C/F): ").upper()
if unit == 'C':
    temp = float(input("Enter the temp in C to convert to F: "))
    print(celsius_to_fahrenheit(temp))

elif unit == 'F':
    temp = float(input("Enter the temp in F to convert to C: "))
    print(fahrenheit_to_celsius(temp))

else: 
    print("Invalid Input")





# =========================
# E3 - Vowel Counter
# =========================
# Write a function count_vowels(sentence) that returns the number of vowels.
# Call it with 3 different sentences and print each result.


vowels = 'aeyuio'
string = input("Enter a string: ").lower()

def count_vowels(string):
    count = 0 
    for caracter in string:
        if caracter in vowels:
            count += 1       
    return count

print(f"The number of vowels in 'hello world': {count_vowels("hello world")}")
print(f"The number of vowels in 'python programming': {count_vowels("python programming")}")
print(f"The number of vowels in your string is: {count_vowels(string)}")

# =========================
# E4 - Repeat String
# =========================
# Write a function repeat_string(text, times=3) that prints a string
# 'times' times. Test it with and without the default argument.

def repeat_string(text, times=3):
    for i in range(times):
        print(text)
    

text = input("Enter the text: ")

print("By Default:")
repeat_string(text)
print("#" * 20)

print("Times = 5")
repeat_string(text,5)
print("#" * 20)

print("Times = 2 ")
repeat_string(text,2)
print("#" * 20)

# =========================
# E5 - Average Calculator
# =========================
# Write a function using *args that takes any number of numbers and
# returns their average. Test with 3, 5, and 7 numbers.

def average(*args):
    if len(args) == 0:
        return 0
    else :
        return sum(args) / len(args)

print(f"{average(10,20,30):.2f}")    
print(f"{average(1,2,3,4,5):.2f}")    
print(f"{average(9.845,99):.2f}")    



# =========================
# E6 - Divisible by 7
# =========================
# Use a list comprehension to generate a list of all numbers from 1 to 50
# that are divisible by 7. Print the result.

divisible_by_7 = [i for i in range(1,51) if i % 7 == 0]
print(divisible_by_7)

# =========================
# E7 - Get Initials
# =========================
# Write a function get_initials(full_name) that takes a full name string
# and returns the initials. Example: "Khaled Bouchoucha" → "K.B"
full_name = input("Enter your full name: ")
def get_initials(full_name):
    words = full_name.split()
    initials = ""
    for word in words:
        initials += word[0].upper() + '.'

    initials = initials[:-1]
    
    print(initials)

get_initials(full_name)    