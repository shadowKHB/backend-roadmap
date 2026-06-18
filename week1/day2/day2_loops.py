# ====================
# WHILE LOOP
# ====================


name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("See you later !")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")



# ====================
# FOR LOOP
# ====================

for x in range(1,5):
    print(x)

print("=========")

for x in reversed(range(1,5)):
    print(x)    

print("=========")

for x in range(1,10,2):
    print(x)

print("=========")

credit_card = "1234-5678-9012-3456"

for y in credit_card:
    print(y)

print("=========")

for x in range(1,11):
    if x == 5:
        continue
    else:
        print(x)

print("=========")

for x in range(1,11):
    if x == 5:
        break
    else:
        print(x)



# ====================
# NESTED LOOP
# ====================

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()    