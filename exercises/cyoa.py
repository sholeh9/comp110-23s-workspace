"""EX06 - Create your own Adventure!"""

__author__ = "730402453"

import random
points: int = 0
player: str = ""
gameplay: bool = True
wizard_emoji = '\U0001F9D9'
chess_emoji = '\U00002656'


def greet() -> None:
    """Greets player and asks for their name."""
    global player
    print(f"Welcome to Hogwarts!{wizard_emoji}")
    player = input("What is your name?")


def main() -> None:
    """Adding up points that the wizard has received while giving game options."""
    global points
    global player
    global gameplay
    greet()
    while gameplay:
        answer: str = input(f" Welcome {player} You have made it to Hogwarts! I am the sorting hat! Are you ready to begin? (Y/N) ")
        if answer == "Y" or answer == "Yes" or answer == "y":
            answer_options: str = input("Would you like to choose your wand (1), play wizard chess (2), or know your Hogwarts House and end the game(3)")
            if answer_options == "1":
                wand_type()
            if answer_options == "2":
                points = custom_function(points)
            if answer_options == "3":
                choosing_house()
                gameplay = False
        else:
            gameplay = False
        print(f"You have collected {points} points!")
    

def wand_type() -> None:
    """Provides wand options."""
    global points
    print("Great! I noticed your wand. Is it made out of Dragon Heartstring(1), Phoenix Feather(2), Unicorn Hair(3), or Dark Web(4)?")
    wand_material = input("Enter your wand material: ")
    if wand_material == "1":
        points += 25
    elif wand_material == "2":
        points += 20
    elif wand_material == "3":
        points += 15
    elif wand_material == "4":
        points += 10
    else:
        print("Sorry, I don't recognize that wand material.")
        points += 0
    choosing_house()


def custom_function(total_points: int) -> int:
    """Custom function that adds points to player's total points."""
    global player
    answer: str = input(f"{player}, would you like to play a game of wizard chess to earn more points? (Y/N)")
    if answer == "Y" or answer == "Yes" or answer == "y":
        total_points += 10
        print(chess_emoji + chess_emoji + chess_emoji + chess_emoji)
        print(f"{player}, you won the game of wizard chess! You have earned 10 points.")
    else:
        print("Maybe next time!")
        
    print(f"{player}, your current points total is {total_points}.")
    choosing_house()
    return total_points

    
def choosing_house() -> None:
    """Assigns the user their Hogwarts House."""
    global points
    global player
    global gameplay
    random_number = random.randint(1, 10)
    house: str = ""
    if points == 15:
        house = "Slytherin"
        print(f"{player}! Time to assign you to your Hogwarts House! You are player #{random_number}! You have been selected as {house}")
    elif points == 10:
        house = "Gryffindor"
        print(f"{player}! Time to assign you to your Hogwarts House! You are player #{random_number}! You have been selected as {house}")
    elif points == 20:
        house = "Hufflepuff"
        print(f"{player}! Time to assign you to your Hogwarts House! You are player #{random_number}! You have been selected as {house}")
    elif points == 0:
        house = "Ravenclaw"
        print(f"{player}! Time to assign you to your Hogwarts House! You are player #{random_number}! You have been selected as {house}")
    else:
        print("Sorry! You don't belong in Hogwarts! Go find Voldemort")
        
    
if __name__ == "__main__":
    main()