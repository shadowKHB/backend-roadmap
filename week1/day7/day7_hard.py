import random
# ===========================
# H1 - Number Guessing Game (Difficulty Levels)
# ===========================
# User picks a difficulty: Easy = 12 guesses, Medium = 8 guesses, Hard = 6 
# guesses. Computer picks a random number, user plays with that guess limit. 
# If they run out of guesses, show "You lost" and reveal the number.

difficulty = input("Enter the difficulty (easy=12, medium=8, hard=6 guesses): ").lower()
number = random.randint(1,100)
print(number)
guesses = 0
while True:
    if difficulty == "hard":
        guesses = 6
        break
    elif difficulty == "medium":
        guesses = 8
        break
    elif difficulty == "easy":
        guesses = 12  
        break
    else:
        difficulty = input("Please enter the difficulty (easy=12, medium=8, hard=6 guesses): ").lower()

while guesses > 0:
    guess_n = int(input("Guess a number between (1-100): "))
    guesses -= 1

    if guess_n == number:
        print(f"Great! You won, the number is: {number}")
        break
    elif guess_n > number:
        print(f"Too high! ({guesses} guesses remaining)")
    else:
        print(f"Too low! ({guesses} guesses remaining)")
    
    if guesses == 0:
        print(f"You failed! the number is: {number}") 
   


# ===========================
# H2 - Simplified ATM
# ===========================
# A dictionary stores {"username": balance} for 2-3 fake users. Ask the user 
# to log in by username, then show a menu: Check Balance / Deposit / 
# Withdraw / Quit. Validate: no negative deposits, no withdrawing more than 
# the balance.

dic = {"khaled": 15000,
       "mohammed": 16000,
       "taher": 10000 }

username = input("Enter your username to log in: ").lower()

if dic.get(username) == None:
    print(f"ERROR! Your username {username} is Invalid!")
else:
    print(f"Welcome {username}.")
    print("======= MENU =======")    
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("0. Quit")
    print("====================")

    option = int(input("How can I help you today?: "))

    while option < 0 or option > 3:
        option = int(input("ERROR! Invalid option. Try again: "))

    while option != 0:
        if option == 1:
            print(f"Your Balance is: {dic.get(username)}")
        elif option == 2:
            to_deposit = int(input("How much would you like to deposit into your account?: "))
            if to_deposit < 0:
                print("ERROR! Deposit amount cannot be negative. ")
            else:    
                dic[username] += to_deposit
                print("Deposit successful.")
        elif option == 3:
            to_withdraw = int(input("How much would you like to withdraw from the bank?: "))
            if to_withdraw > dic[username]:
                print("ERROR! Withdrawal amount cannot exceed the current balance.")
            else:
                dic[username] -= to_withdraw
                print("Withdrawal successful.")
        else:
            while option < 0 or option > 3:
                option = int(input("ERROR! Invalid option. Try again: "))

        print("======= MENU =======")    
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("0. Quit")
        print("====================")
        option = int(input("How can I help you: "))


    print("Thank you! See you later..")    






# ===========================
# H3 - Tic-Tac-Toe Board
# ===========================
# Build just the board logic (not full game rules): a 3x3 grid, two players 
# take turns entering row/col to place X or O, the board prints after every 
# move, and the game ends after 9 total moves. Win-detection isn't required 
# yet — that needs functions, coming in Week 2.

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

for i in range(9):
    
    row = int(input("Enter the row (1-3): "))
    while row < 1 or row > 3:
        row = int(input("Please enter the row (1-3): "))
        
    column = int(input("Enter the column (1-3): "))
    while column < 1 or column > 3:
        column = int(input("Please enter the column (1-3): "))


    while board[row - 1][column - 1] != ' ':
        print(f"This place is already taken!")

        row = int(input("Enter the row (1-3): "))
        while row < 1 or row > 3:
            row = int(input("Please enter the row (1-3): "))
        
        column = int(input("Enter the column (1-3): "))
        while column < 1 or column > 3:
            column = int(input("Please enter the column (1-3): "))
        

    if i % 2 == 0:
        print("Now the turn of player 2: ")
        board[row - 1][column - 1] = 'X'
    else:
        print("Now the turn of player 1: ")        
        board[row - 1][column - 1] = 'Y'
            
print(board[0])
print(board[1])
print(board[2])




# ===========================
# H4 - Inventory Price Calculator
# ===========================
# A dictionary of items and prices. The user can add multiple items with 
# quantities (e.g. "apple x3"), and the program prints an itemized receipt 
# with subtotals per item and a grand total.

inventory = {"apple": 2.00,
             "bread": 1.50,
             "milk": 3.00}

print(inventory)
list_items = []
while True:
    item = input("Enter the item with his quantity (example: 'apple *3'), (q to quit): ").lower()
    if item == 'q':
        break
    else:
        item_q = item.split()
        if inventory.get(item_q[0]) == None:
            print("Item NOT founded!")
        else:
            item_i = item_q[0]
            quantity = int(item_q[1][1:])
            list_items.append([item_i , quantity])

if len(list_items) == 0:
    print("You haven't items!")
else:
    print("RECEIPT")
    sum = 0
    for item in list_items:
        print(f"{item[0]}  *{item[1]}  ${item[1] * inventory.get(item[0])}")  
        sum += item[1] * inventory.get(item[0])  
    print("---------------------")
    print(f"TOTAL:     ${sum}")

