import random
# =========================
# M1 - Word Frequency Counter
# =========================
# Write a program that asks for a sentence and counts how many times each 
# word appears, using a dictionary. Print each word with its count.


sentence = input("Enter a sentence: ").lower()

while len(sentence) == 0:
    sentence = input("Please enter a sentence: ").lower()

words = sentence.split()

dic = {}

for word in words:
    if dic.get(word) == None:
        dic[word] = 1
    else:
        dic[word] += 1

for key, value in dic.items():
    print(f"{key}: {value} ")
        


# =========================
# M2 - Coin Flip Simulator
# =========================
# Write a program that simulates flipping a coin 100 times (using random) 
# and prints how many heads and tails resulted.


print("===== Coin Flip Simulator =====")
coin = ["head", "tail"]
count_head = 0
count_tail = 0

for i in range(100):
    flip = random.choice(coin)
    if flip == "head":
        count_head += 1
    else:
        count_tail += 1    

print(f"How many heads: {count_head}/100 ")
print(f"How many tails: {count_tail}/100 ")




# =========================
# M3 - Separate Evens and Odds
# =========================
# Write a program that takes a list of numbers and separates them into two 
# new lists: evens and odds. Print both lists.


numbers = [0, 5, 7, 2, 20, 25, 15, 13, 6]
odds = []
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

print(f"The odd numbers are: {odds}")
print(f"The even numbers are: {evens}")



# =========================
# M4 - Secret Password Checker
# =========================
# Store a set of 3 valid passwords. Ask the user to guess, give them 3 tries 
# total, tell them if they're right or wrong, and lock them out after 3 
# failed attempts.


valid_passwords = {"admin123", "12345678", "0963258"}
guesses = 3

while guesses > 0:
    test = input(f"Enter the password ({guesses} guesses remaining): ")
    guesses -= 1
    if test in valid_passwords:
        print("Great your password is Valid! ")
        break
    else:
        print("Your password is Invalid! Try again..")

if guesses == 0:
    print("You lose! (0 guesses remaining)")



# =========================
# M5 - 2D Grid Placement
# =========================
# Create a 3x3 grid (list of lists) filled with "-". Ask the user for a row, 
# column, and a symbol, place that symbol at that position, then print the 
# updated grid.


matrix = [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]

print("===== The Origin Matrix =====")
for row in matrix:
    print(row)

while True: 
    row = int(input("Enter the row(1-3): "))
    while row < 1 or row > 3:
        row = int(input("Enter the row(1-3): "))
    column = int(input("Enter the column(1-3): "))
    while column < 1 or column > 3:
        column = int(input("Enter the column(1-3): "))
    symbol = input("Enter the symbol: ")

    matrix[row - 1][column - 1] = symbol

    is_running = input("Do you want to quit (yes/no)?: ").lower()
    if is_running == "no":
        break
      
print()
print("===== The New Matrix =====")
for row in matrix:
    print(row)



# =========================
# M6 - Palindrome Checker
# =========================
# Write a program that takes a string and checks if it's a palindrome 
# (reads the same forwards and backwards), ignoring case and spaces.


string = input("Enter a string: ").lower().replace(" ","")
string_reversed = ""

string_reversed = string[::-1]

if string == string_reversed:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")    