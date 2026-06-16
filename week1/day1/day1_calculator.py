# Python calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+ - * /): ")

if operator == "+":
    print(f"{num1} + {num2} = {round(num1+num2,2)}")
elif operator == "-":
    print(f"{num1} - {num2} = {round(num1-num2,2)}") 
elif operator == "*":
    print(f"{num1} * {num2} = {round(num1*num2,2)}") 
elif operator == "/":
    if num2 == 0:
        print("ERROR! You can't divide by zero")
    else:
        print(f"{num1} / {num2} = {round(num1/num2,2)}")      
else:
  print(f"ERROR! {operator} is not a valid operator")  