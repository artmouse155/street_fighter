import turtle as trtl
import healthbar
import keyboard
import datetime
import player
import rectangle
import data

wn = trtl.Screen()
wn.tracer(False)
running = True
# important keyboard command if keyboard.is_pressed('a'):

setup = trtl.Turtle()

platforms = []

#draw a platform
def drawground(x,y, height, width): 
    global setup
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


def setup_game():
    global setup, platforms
    wn.bgcolor("white")
    #draw the ground
    platforms.append(rectangle.rectangle(-400, -400, 200, 800))
    platforms.append(rectangle.rectangle(-250, 0, 20, 100))
    platforms.append(rectangle.rectangle(150, 0, 20, 100))
    platforms.append(rectangle.rectangle(-50, 100, 20, 100))
    
    #platforms 
    #drawground(-400, -400, 200, 800)
    #drawground(-250, 0, 20, 100)
    #drawground(150, 0, 20, 100)
    #drawground(-50, 100, 20, 100)
    for i in range(len(platforms)):
	    platforms[i].draw(setup,"green")

#variables for player 1
max_health_1 = 100
health_1 = 100

setup_game()
max_health_2 = 100
health_2 = 100

#gravity

def loop():
    global health_1, gravity, platforms
    
    health_bar_1 = healthbar.healthbar(max_health_1,50,50)
    health_bar_2 = healthbar.healthbar(max_health_2,-50,-50)

    player_1 = player.player("maroon", 0,0)

    dt = 0
    old_time = datetime.datetime.now()
    while running: #this is actually the only loop across all our code! (If you don't count movement.py, which doesn't run anyways)
        dt = (old_time - datetime.datetime.now()).microseconds / 1000000
        old_time = datetime.datetime.now()
        
        health_bar_1.set_hp(health_1)

        health_bar_1.update()
        player_1.set_y_vel(0)
        player_1.goto(player_1.get_x(), 0)
        print(dt)
        player_1.update(dt)
        #health_bar_2.update()
        wn.update()
#----------------------------------------------------------------

loop()
wn.mainloop()