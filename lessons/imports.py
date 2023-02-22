"""Practice impoting from other modules"""

from lessons import my_functions

print(my_functions.addition(1,2)) #keepgettingerror?

#can also do this by writing from lessons.my_functions import addition (kind of like from random import randint)

print(my_functions.my_variable)

if __name__ == "__main__":
    print("howdy")

