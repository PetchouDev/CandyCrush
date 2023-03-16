from tkinter import Button

from ..manager import MANAGER

class Candy(Button):
    def __init__(self, parent, holder, x, y, type, **kwargs):
        Button.__init__(self, holder, **kwargs)
        self.holder = holder
        self.x = x
        self.y = y
        self.type = type
        self.parent = parent

        self.selected = False

        self.bind(f"<Button-1>", lambda event: self.clicked())

        self.configure(bg=MANAGER.get("CANDY_BG"))

    def change_color(self, color):
        self.configure(bg=color)

    def clicked(self):
        selected = self.parent.click_handler(self)
        try:
            if selected:
                self.change_color(MANAGER.get("SELECTED_COLOR"))
            else:
                self.change_color(MANAGER.get("CANDY_BG"))
        except:
            pass

