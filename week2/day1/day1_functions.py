import time
# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you !")
    print()

happy_birthday()    


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("JoeSchmo", 100.01, "01/02")    



# return = statement used to end a function 
#          and send a result back to the caller

def add(x, y):
    z = x + y 
    return z

def substract(x, y):
    z = x - y 
    return z

def multiply(x, y):
    z = x * y 
    return z

def divide(x, y):
    z = x / y 
    return z

print(add(1, 2))
print(substract(1,2))
print(multiply(1,2))
print(divide(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("khaled", "bouchoucha")

print(full_name)



# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1)) 
print(net_price(500, 0.1, 0))                     

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")    

count(10, 0)    



# keyword arguments = an argument preceded by an identifier 
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)



# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keywords-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

def add(*nums): # * = unpacking to tuple 
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3,4))    


def print_address(**kwargs): # ** = unpacking to dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              city="Detroit", 
              state="MI",
              zip="54321")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}") 
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")   

shipping_label("Dr.", "Mohammed", "Taher",
               street = "123 Fake St.",
               city = "Detroit",
               state = "MI",
               zip = "54321")    