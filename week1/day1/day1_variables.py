# =====================
# VARIABLES
# =====================

#===Strings=== 
first_name = "Khaled"
sport = "Football"
email = "Khaled@fake.com"

# print(f"Hello {first_name}")
# print(f"I like {sport}")
# print(f"My email is: {email}")


#===Integers===
age = 20
quantity = 5
points = 30

# print(f"You are {age} years old")
# print(f"You are buying {quantity} items ")
# print(f"You have {points} points")


#===Floats===
price = 9.99
gpa = 2.7
grade = 16.5

# print(f"The price is ${price}")
# print(f"Your gpa is: {gpa}")
# print(f"Your grade is {grade}")


#===Boolean===

is_student = True
for_sale = False
is_online = True


# print(f"Are you a student?: {is_student}")
# print(f"Is that item for sale?: {for_sale}")
# print(f"Is he online?: {is_online}")



# =====================
# TYPE CASTING
# =====================

name = "Khaled khb"
age = 20
gpa = 2.7
is_student = True

# print(type(gpa))

gpa = int(gpa)
# print(gpa)

age = float(age)
# print(age)

age = str(age)
# print(age)
# print(type(age))

name = bool(name)
# print(name)

name = ""
name = bool(name)
# print(name) # empty = False



# =====================
# USER INPUT
# =====================

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))

# print(f"Hello {name}!")
# print(f"You are {age} years old")


#Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is: {area}")


#Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"The total is: ${total}")
