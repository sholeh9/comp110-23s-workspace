"""File to define Fish class."""


class Fish:
    """New fish class."""
    age: int

    def __init__(self):
        """New fish with an age."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Increases age after one day."""
        self.age += 1
        return None