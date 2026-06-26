import random

# print(help(random))

low = 1
high = 100
options = ("paper", "rock", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

number = random.randint(low, high)
n = random.random() #Random number between 0 and 1
option = random.choice(options)
random.shuffle(cards)

print("------------------")
print(number)
print("------------------")
print(n)
print("------------------")
print(option)
print("------------------")
print(cards)
print("------------------")

