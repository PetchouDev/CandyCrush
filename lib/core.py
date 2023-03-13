class Color:
    _blue = '\033[94m'
    _green = '\033[92m'
    _yellow = '\033[93m'
    _red = '\033[91m'
    _purple = '\033[95m'
    _cyan = '\033[96m'
    
    end = '\033[0m'

    white_bg = '\033[107m'

    colors = {"blue": _blue, "green": _green, "yellow": _yellow, "red": _red, "purple": _purple}

    def all(self):
        return [c for c in self.colors.keys()]

def colored(text, color, bg=False):
    if bg:
        res =  Color.colors[color] + Color.white_bg + text + Color.end
    else: 
        res = Color.colors[color] + text + Color.end
    return res
    
