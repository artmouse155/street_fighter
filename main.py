import turtle as trtl
import healthbar
import keyboard
import datetime
import player
import rectangle
import data

wn = trtl.Screen()
wn.tracer(False)
# important keyboard command if keyboard.is_pressed('a'):

#draw a platform
"""def drawground(x,y, height, width): 
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
"""

def setup_game():

    setup = trtl.Turtle()
    setup.hideturtle()
    wn.bgcolor("white")
    #draw the ground
    data.platforms.append(rectangle.rectangle(-400, -400, 200, 800))
    data.platforms.append(rectangle.rectangle(-250, -100, 20, 100))
    data.platforms.append(rectangle.rectangle(150, -100, 20, 100))
    data.platforms.append(rectangle.rectangle(-50, 0, 20, 100))
    
    #platforms 
    #drawground(-400, -400, 200, 800)
    #drawground(-250, 0, 20, 100)
    #drawground(150, 0, 20, 100)
    #drawground(-50, 100, 20, 100)
    for i in range(len(data.platforms)):
	    data.platforms[i].draw(setup,"green")
    
    #INVISIBLE BARRIERS!!!!
    data.platforms.append(rectangle.rectangle(-390, -400, 1000, 20))
    data.platforms.append(rectangle.rectangle(370, -400, 1000, 20))

def loop():
    global health_1, gravity
    
    #health_bar_1 = healthbar.healthbar(max_health_1,50,50)
    #health_bar_2 = healthbar.healthbar(max_health_2,-50,-50)

    player_1 = player.player("maroon", -300, 50, data.player_1_controls)
    player_2 = player.player("purple", 300, 50, data.player_2_controls)

    dt = 0
    old_time = datetime.datetime.now()
    running = True
    while running: #this is actually the only loop across all our code! (If you don't count movement.py, which doesn't run anyways)
        dt = (datetime.datetime.now() - old_time).microseconds / 1000000
        old_time = datetime.datetime.now()
        
        #health_bar_1.set_hp(health_1)

        #health_bar_1.update()
        #player_1.set_y_vel(0)
        #player_1.goto(player_1.get_x(), 0)
        player_1.update(dt)
        player_2.update(dt)
        #health_bar_2.update()
        wn.update()
#----------------------------------------------------------------
setup_game()
loop()
wn.mainloop()