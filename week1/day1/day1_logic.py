# =====================
# ARITHMETIC & MATH
# =====================

import math


friends = 5

# friends = friends + 1
# friends += 1 

# friends = friends - 1
# friends -= 1

# friends = friends * 3
# friends *= 3 

# friends = friends / 2
# friends /= 2

# friends = friends ** 2
# friends **= 2

# remainder = friends % 3

# print(remainder)


x = 3.14
y = -4
z = 9

# result = round(x)
# result = abs(y)
# result = pow(z,3) 
# result = max(x,y,z)
# result = min(x,y,z)
# print(math.pi)
# print(math.e)
# result = math.sqrt(z)
# result = math.ceil(x)
# result = math.floor(x)


#Exercise 1 Calc the circumference of a circle
radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)}cm")


# #Exercice 2 calc the area of a circle
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius,2)

print(f"The area of the circle is: {round(area,2)}")


#Exercise 3 calc the hypotenuse of a right triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c= math.sqrt(pow(a,2)+pow(b,2))

print(f"The hypotenuse of this triangle is: {round(c,2)}cm")



# =====================
# IF STATEMENTS
# =====================

age = int(input("Enter your age: "))
if age < 0:
  print("You haven't been born yet!") 
elif age >= 100:
  print("You are too old to sign up")  
elif age >= 18:
  print("You are now signed up!")
else:
  print("You must be 18+ to sign up")  


name = input("Enter your name: ")

if name == "":
  print("You did not type in your name!")
else:
  print(f"Hello {name}") 


for_sale = True

if for_sale:
  print("This item is for sale")
else:
  print("This item is NOT for sale")   