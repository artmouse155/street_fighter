#initiliazing variables 
import turtle as trtl
import keyboard

class movement:
    wn = trtl.Screen()
    tester = trtl.Turtle(shape = "square")
    tester.goto(0,0)
    tester.penup()
    #---------------
    jumpingvelocity = 50
    gravity = .002
    dt = .001
    #----------------
    #the command for the keyboard imput is if keyboard.is_pressed('letter')
    while True:
        if keyboard.is_pressed('w'):
            tester.setheading(90)
            tester.forward(jumpingvelocity)
            tester.forward(jumpingvelocity * (gravity*dt))
        else:
            while tester.ycor() > 0:
                tester.setheading(270)
                tester.forward(jumpingvelocity)
                tester.forward(jumpingvelocity * (gravity*dt))