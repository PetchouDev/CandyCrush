class Color:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    purple = '\033[95m'
    cyan = '\033[96m'
    
    end = '\033[0m'

    white_bg = '\033[107m'

    def all(self):
        return [self.blue, self.green, self.yellow, self.red, self.purple, self.cyan]
