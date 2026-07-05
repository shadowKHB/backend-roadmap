# Python compound interest calculator
# A = P(1+(r/n))**t

principle = 0
rate = 0
time = 0

def get_positive_number(prompt):
    arg = float(input(prompt))
    while True:
        if arg < 0:
            print("It can't be less than to zero")
            arg = float(input(prompt))
        else:
            break
    return arg   

principle = get_positive_number("Enter the principle amount: ")
rate = get_positive_number("Enter the interest rate: ")
time = int(get_positive_number("Enter the time in years: "))

    
total = principle * pow((1 + (rate / 100)),time)
print(f"Balance after {time} year/s is: ${total:.2f}")