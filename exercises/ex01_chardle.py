"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730402453"

user_name: str = input("Enter a 5-character word: ")
if len(user_name) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
inst: int = 0
print("Searching for " + character + " in " + user_name)
if (user_name[0] == character):
    print(character + " found at index 0")
    inst = inst + 1
if (user_name[1] == character):
    print(character + " found at index 1")
    inst = inst + 1
if (user_name[2] == character):
    print(character + " found at index 2")
    inst = inst + 1
if (user_name[3] == character):
    print(character + " found at index 3")
    inst = inst + 1
if (user_name[4] == character):
    print(character + " found at index 4")
    inst = inst + 1 
if inst == 0:
    print("No instances of " + character + " found in " + user_name)
elif inst == 1: 
    print(str(inst) + " instance of " + character + " found in " + user_name)
else:
    print(str(inst) + " instances of " + character + " found in " + user_name)
