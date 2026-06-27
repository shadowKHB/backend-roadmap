# =========================
# E1 - Even or Odd
# =========================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is Even!")
else:
    print(f"{number} is Odd")    



# =========================
# E2 - Largest of 5 numbers
# =========================

numbers = []


for i in range(5):
    n = int(input(f"Enter the number {i+1}: "))
    numbers.append(n)
largest = numbers[0]
for i in range(1,5):
    if numbers[i] > largest:
        largest = numbers[i]

print(f"Your list is of numbers is: {numbers}")

print(f"The max is: {largest}")



# =========================
# E3 - Reverse a word
# =========================

word = input("Enter a word: ")
word_reversed = ""

for i in range(len(word)):
    word_reversed += word[len(word)-i-1] 

print(f"Your word is: {word}")
print(f"The reversed word is: {word_reversed}")



# =========================
# E4 - Count Vowels in a Sentence
# =========================

sentence = input("Enter a sentence: ").lower()
while len(sentence) == 0:
    sentence = input("Please enter a sentence: ").lower()

vowels = ["a", "e", "i", "o", "u", "y"]
count = 0
i = 0
while i < len(sentence):
    if sentence[i] in vowels:
        count += 1
    i += 1    

print(f"Your sentence contains {count} vowels!")



# =========================
# E5 - Divisible by 3 and 5
# =========================

nums = []
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        nums.append(i)

print(f"The numbers that are divisible by both 3 and 5 are: {nums}")



# =========================
# E6 - Uppercase Fruit List
# =========================

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit.upper(), end=' ')



# =========================
# E7 - Country Capitals Dictionary
# =========================

countries = {
    "ALGERIA" : "Alger",
    "CANADA" : "Ottawa",
    "SPAIN" : "Madrid"
}

print(countries)

while True:
    country = input("Enter a country (q to quit): ").upper()
    if country == 'Q':    
        break
    elif countries.get(country) == None:
        print("Unknown")
    else:
        print(f"The capital of {country}: {countries.get(country)}")


print("See you later!")


