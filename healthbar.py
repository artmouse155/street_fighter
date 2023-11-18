import turtle as trtl
import rectangle
class healthbar:

    max_hp = 100
    hp = 100
    x = 0
    y = 0
    bar = None

    bar_w = 100
    bar_h = 10

    def __init__(self, max_hp, x, y) -> None:
        self.max_hp = max_hp
        self.hp = max_hp
        self.x = x
        self.y = y
        self.bar = trtl.Turtle()
        self.bar.hideturtle()
        self.bar.penup()
        self.bar.goto(x,y)


    def update(self):
        bar = self.bar
        x = self.x
        y = self.y
        bar_w = self.bar_w
        bar_h = self.bar_h
        hp_bar_w = bar_w * (self.hp / self.max_hp)
        bar.clear()
        rectangle.rectangle(x, y, bar_h, bar_w).draw(bar, "red")
        rectangle.rectangle(x, y, bar_h, hp_bar_w).draw(bar, "green")

    def set_hp(self, hp):
        self.hp = hp

    def goto(self, x, y):
        self.x = x
        self.y = y
