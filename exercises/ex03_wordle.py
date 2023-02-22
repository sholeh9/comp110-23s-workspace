"""EX03 - One-shot Wordle!"""

__author__ = "730402453"


def contains_char(secret, guess) -> bool:
    assert len(guess) == 1
    i = 0
    while i < len(secret): #checking to makes sure you have right amount of characters
        if secret[i] == guess:
            return True
        i += 1
    return False
    
def emojified(guess:str, secret:str):
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    result: str = ""
    i = 0

    while i < len(secret):
        if secret[i] == guess[i]: #checks each character in relation to the secret word
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result

def input_guess(word_length: int):
    input_guess: str = input(f"Enter a {word_length} character word: ")
    playing: bool = True #need to say true in order to end the game with false
    while playing is True:
        if len(input_guess) == word_length:
            return input_guess
        if len(input_guess) != word_length:
            input_guess = input(f"That wasn't {word_length} chars! Try again: ")

def main() -> None:
    """The entrypoint of the program and main game loop."""
    num_guesses: int = 0
    Secret: str = "codes"
    Game_over: bool = False

    while num_guesses < 6 and Game_over is False: #gives number of guesses and ends game
        print(f"=== Turn {num_guesses + 1}/{6} === ")
        guess = input_guess(len(Secret))
        result = emojified(guess, Secret)
        print (result)

        if guess == Secret:
            print(f"You won in {num_guesses + 1}/{6} turns!")
            Game_over = True
        else:
            num_guesses += 1
   
    if Game_over == False:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()