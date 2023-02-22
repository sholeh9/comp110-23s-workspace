"Guessing game-Asks user for a number and goes until you get it right"

#all caps is a variable that is NOT changing
SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True


while playing:
    if guess == SECRET:
        print("Yay! You got it right.")
        playing = False
    else:
        print("Wrong number :(")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd. The answer is even")
        if guess > SECRET:
            print("Your guess is too high! ")
        else: #guess< secret
            print("Your guess is too low. ")
        guess = int(input("Make another guess! "))

5
