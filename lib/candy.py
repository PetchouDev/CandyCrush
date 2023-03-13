from lib.core import colored

class Candy:
    def __init__(self, color):
        self.color = color
        self.selected = False

    def __str__(self):
        return colored('■', self.color, self.selected)
    


