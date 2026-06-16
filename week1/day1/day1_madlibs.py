# Madlibs game 
# Word game where you create a story
# by filling in blanks with random words

adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective2 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")
place = input("Enter a place: ")
emotion = input("Enter an emotion: ")
verb2 = input("Enter a verb: ")

story = f"One {adjective1} day, a {noun1} decided to {verb1} to {place}. \
  It felt very {emotion} when it saw a {adjective2} {noun2} trying to {verb2}."

print("\n--- YOUR STORY ---")
print(story)