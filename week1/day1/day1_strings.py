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