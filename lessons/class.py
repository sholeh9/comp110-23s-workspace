class ChristmasTreeFarm:
    plots: list[int]

def __init__(self, plots: int, initial_planting: int) -> None:
    """sets up the farm"""
    self.plots = []
    for _ in range(0, initial_planting):
        self.plots.append(1)
    for _ in range(initial_planting, plots):
        self.plots.append(0)

    def plant(self, spot:int):
        self.plant[spot] = 1

    def growth(self):
        for x in range(0, len(self.plots)):
            if(self.plots[x]>0):
                self.plots[x]+=1
    
    def harvest(self, replant: bool)-> int:
       cut: int = 0
       for x in range(0, len(self.plots)):
            if(self.plots[x] >= 5):
                cut+= 1
                if(replant):
                    self.plots[x] = 1
                else:
                    self.plots[x] = 0
            return cut
