"""random practice"""

x:int = 1

def f(y: int) -> int:
    return x + y

print(f(x + 1))


def main1() -> None:
    """Adding additional points that the wizard has received"""
    global points
    global player_name
    global gameplay 
    while gameplay:      
        print("Now let's test your knowledge!")
        answer = input("What is the name of the wizard who defeated Voldemort? ")
        if answer == "Harry Potter":
                points += 25
        else:
            print("Sorry, that's incorrect.")
            points += 0   

        answer = input("What woman guards the entrance to the Gryffindor common room? ")
        if answer == "Fat lady": or if answer == "Fat Lady"
            points += 25
        else:
            print("Sorry, that's incorrect.")

    else:
        print("Seems like you don't want to further your studies at Hogwarts. Maybe we will see you in the Muggle world!")