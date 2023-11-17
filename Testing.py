import turtle as trtl
setup = trtl.Turtle()


def drawground(x,y, height, width): 
    setup.goto(x,y)
    setup.pendown()
    setup.fillcolor("green")
    setup.begin_fill()
    setup.pendown()
    setup.setx(x+width)
    setup.sety(y+height)
    setup.setx(x)
    setup.sety(y)
    setup.end_fill()

drawground(-250, 0, 20, 100)