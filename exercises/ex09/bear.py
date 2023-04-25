"""File to define Bear class."""


class Bear:
    """Create New Bear."""
    age: int
    hunger_score: int

    def __init__(self):
        """New bear with an age and hunger score."""
        self.age: int = 0
        self.hunger_score: int = 0    
        return None
    
    def one_day(self):
        """Decreased hunger score after one day."""
        self.age += 1
        self.hunger_score = self.hunger_score - 1 
        return None
    
    def eat(self, num_fish: int):
        """Increases hungerscore based on number of fish consumed."""
        self.hunger_score = self.hunger_score + num_fish