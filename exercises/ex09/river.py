"""File to define River class."""

__author__ = "730402453"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Creating the River class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears, then removes them once they reach a certain age."""
        self.rm_list_bears: list[Bear] = []
        self.rm_list_fish: list[Fish] = []
        for x in self.bears:
            if x.age <= 5:
                self.rm_list_bears.append(x)
        self.bears = self.rm_list_bears

        for x in self.fish:
            if x.age <= 3:
                self.rm_list_fish.append(x)
        self.fish = self.rm_list_fish
        return None

    def bears_eating(self):
        """The bears eat when the amount of fish are greater than five."""
        self.fish_population: list[Fish] = []
        for x in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                x.eat(3)
        return None
    
    def check_hunger(self):
        """Checks bear hunger and adds live bears into a new list."""
        self.live_bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score >= 0:
                self.live_bears.append(x)
        self.bears = self.live_bears
        return None
        
    def repopulate_fish(self):
        """Repopulates the Fish."""
        for x in self.fish:
            new_fish: int = ((len(self.fish)) // 2) * 4
            self.bears.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """Repopulates the Bears."""
        for x in self.bears:
            new_bears: int = (len(self.bears) // 2)
            self.bears.append(new_bears)
        return None
    
    def view_river(self):
        """Prints the amount of Fish, Bears, and days."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def remove_fish(self, amount: int):
        """Removes fish that is first located in the list."""
        if len(self.fish) < amount:
            raise ValueError("Not enough fish!")
        for x in range(amount):
            self.fish.pop(x)
        return None
    
    def one_river_week(self):
        """Calls one_river_day 7 times."""
        for x in range(7):
            self.one_river_day()
        return None