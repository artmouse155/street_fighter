import turtle as trtl

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
        bar.color("red")
        bar.goto(x,y)
        bar.begin_fill()
        bar.setx(x+bar_w)
        bar.sety(y+bar_h)
        bar.setx(x)
        bar.sety(y)
        bar.end_fill()

        bar.color("green")
        bar.goto(x,y)
        bar.begin_fill()
        bar.setx(x+hp_bar_w)
        bar.sety(y+bar_h)
        bar.setx(x)
        bar.sety(y)
        bar.end_fill()

    def set_hp(self, hp):
        self.hp = hp

    def goto(self, x, y):
        self.bar.goto(x,y)
