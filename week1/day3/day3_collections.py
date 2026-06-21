# collection = single "variable" used to store multiple values
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and mutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# ==============
# LIST
# ==============

fruits = ["apple","banana", "coconut"]

print(dir(fruits))  # shows built-in methods of list 
print(help(fruits)) # describe what each function does 
print(fruits[0])
print(len(fruits))

print("apple" in fruits)

print("The original list: ")
for fruit in fruits:
  print(fruit)

fruits[0] = "pineapple"
print(fruits)
print("====================================")

fruits.append("orange")
print(fruits)
print("====================================")

fruits.remove("pineapple")
print(fruits)
print("====================================")

fruits.insert(0,"pineapple")
print(fruits)
print("====================================")

fruits.sort()
print(fruits)
print("====================================")

fruits.reverse()
print(fruits)
print("====================================")

print(fruits.index("orange"))
print(fruits.count("apple"))

fruits.clear()
print(fruits)
print("====================================")
print("====================================")


# ==============
# SET
# ==============

fruits = {"apple","banana", "coconut","banana"}

print(dir(fruits))  # shows built-in methods of SET 
print(help(fruits)) # describe what each function does 
print(len(fruits))
print("pineapple" in fruits)

print(fruits)

for fruit in fruits:
  print (fruit)

fruits.add("pineapple") # Add an element in the first
print(fruits)
print("====================================")

fruits.remove("apple")
print(fruits)
print("====================================")

fruits.pop() # Remove the first element of the set
print(fruits)
print("====================================")

fruits.clear()
print(fruits)
print("====================================")



# ==============
# TUPLE
# ==============

fruits = ("apple","banana", "coconut","banana")

print(dir(fruits))  # shows built-in methods of TUPLE 
print(help(fruits)) # describe what each function does 
print(len(fruits))
print("pineapple" in fruits)

print(fruits)
for fruit in fruits:
  print(fruit)

print(fruits.index("banana"))
print(fruits.count("banana"))
