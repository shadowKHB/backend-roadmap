# =======================
# LOGIC OPERATORS
# =======================

# OR = at least one condition must be True

temp = 25
is_raining = False 

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


# AND = both conditions must be True

temp = 30
is_sunny = True 

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("IT is sunny")
elif temp <=0 and is_sunny:
    print("It is COLD outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("IT is CLOUDY")
elif temp <=0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")  



# =======================
# CONDITIONAL EXPRESSIONS
# =======================

num = 5 
a = 6
b = 7
age = 13
temperature = 20
user_role = "admin"

print("Positive" if num >= 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited access"

print(access_level)



# =======================
# STRING METHODS
# =======================

name = input("Enter your full name: ")

result = len(name)
result = name.find(" ")   #The index of the first occurrence
result = name.rfind("q")  #The index of the last occurrence
name = name.capitalize()  
name = name.upper()       
name = name.lower()
result = name.isdigit()
result = name.isalpha()

phone_number = input("Enter your phone number: ")

result = phone_number.count("-")
phone_number = phone_number.replace("-"," ")


print(result)
print(phone_number)


# EXERCISE: Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username INVALID ! Your username can't be more than 12 characters ")
elif not username.find(" ") == -1 :
    print("Username INVALID ! Your username can't contain spaces")
elif not username.isalpha(): 
    print("Username INVALID ! Your username can't contain digits")  
else:
    print(f"Welcome {username}")   



# =======================
# STRINGS INDEXING
# =======================

# [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::2])

last_digits = credit_number[-4 : ]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1]
print(credit_number)



# =======================
# FORMAT SPECIFIERS
# =======================

# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f ---> round to that many decimal places (fixed point)
# :(number)  ---> allocate that many spaces
# :03        ---> allocate and zero pad that many spaces
# :<         ---> left justify
# :>         ---> right justify
# :^         ---> center align
# :+         ---> use a plus sign to indicate positive value
# :=         ---> place sign to leftmost position
# :          ---> insert a space before positive numbers
# :,         ---> comma separator  


price1 = 3000.14159
price2 = -9807.65
price3 = 1002.34

print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")

print(f"Price 1 is {price1:10}")

print(f"Price 1 is {price1:010}")

print(f"Price 1 is {price1:>10}")

print(f"Price 1 is {price1:<10}")

print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")

print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")

print(f"Price 1 is {price1:,.2f}")
print(f"Price 2 is {price2:,.2f}")
print(f"Price 3 is {price3:,.2f}")


