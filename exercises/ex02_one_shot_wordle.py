"""EX02 - Wordle!"""

__author__ = "730402453"

Correct: str = "python"
guess: str = str(input("What is your 6 letter-guess? "))
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while playing:
    if len(guess) != (len(Correct)):
        guess = str(input("That was not 6 letters! Try again: "))
    else: 
        write: str = ""
        character: int = 0
        character1: int = 0

        while character < 6:
            character1 = 0
            yellow_box_added: bool = False
            if guess[character] == Correct[character]:
                write = write + GREEN_BOX
            else: 
                
                while character1 < 6 and yellow_box_added is False:
                    if guess[character] == Correct[character1]: 
                        write = write + YELLOW_BOX
                        yellow_box_added = True
                    character1 = character1 + 1 

                if yellow_box_added is False: 
                    write = write + WHITE_BOX

            character = character + 1 
        
        print(write)
        all_correct: str = GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX
        if write == all_correct: 
            print("Woo! You got it!")
        else: 
            print("Not quite. Play again soon!")
        playing = False
