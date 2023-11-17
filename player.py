import turtle as trtl
import rectangle
import keyboard
import data
class player:
    width = 10
    height = 40
    x = 0
    y = 0
    x_vel = 0
    y_vel = 0
    x_acc = 0
    y_acc = 0
    player = None
    jump_vel = 20
    rect = None
    color = "red"
    movement_vel = 10
    jump_vel = 10
    on_ground = True

    def __init__(self, color, x, y) -> None:
        self.x = x
        self.y = y
        self.player = trtl.Turtle()
        self.player.penup()
        self.player.goto(x,y)
        self.player.color(color)
        self.color = color
        self.rect = rectangle.rectangle(x, y, self.height, self.width)

    def update(self, dt):
        left_pressed = keyboard.is_pressed('a')
        right_pressed = keyboard.is_pressed('d')
        up_pressed = keyboard.is_pressed('w')

        #try to move left or right
        if (left_pressed == right_pressed):
            #TODO: change this if we want the player to glide through the air
            self.x_vel = 0
        elif left_pressed:
            self.x_vel = -self.movement_vel
        elif right_pressed:
            self.x_vel = self.movement_vel

        #check if we can jump
        if (up_pressed and self.on_ground):
            self.y_vel = self.jump_vel
        #attempt movement update
        
        #first, update our velocity
        #self.x_vel += (self.x_acc * dt) #(commenting this out because we won't have any x acceleration)
        self.y_vel += ((self.y_acc + data.gravity) * dt)

        #calculate the X and the Y the player is trying to move to due to its velocity
        new_x = self.x + (self.x_vel * dt)
        new_y = self.y + (self.y_vel * dt)

        #print(str(new_x) + " " + str(new_y))

        #finalize movement according to collision with platforms
        x_and_y = self.adjust_for_collision(new_x, new_y)
        #x_and_y = [new_x, new_y]
        self.x = x_and_y[0]
        self.y = x_and_y[1]
        self.rect = rectangle.rectangle(self.x, self.y, self.height, self.width)
        #finally, draw ourselves!
        self.player.clear()
        self.rect.draw(self.player, self.color)

    def adjust_for_collision(self, new_x, new_y):
        x = self.x
        y = self.y

        #we will calculate collision in the x direction first, and then in the y direction.
        #----------------------------------------------------------------------------------#
        #check left/right collisions
        reset_x_vel = False
        for i in range(len(data.platforms)):
                #a rectangle of the player's potential new bounding box in 
            #the x direction
            new_x_rect = rectangle.rectangle(new_x, y, self.rect.get_height(), self.rect.get_width())
            platform_rect = data.platforms[i]

                #create a boolean value for if the potential rectangle intersects with
                #the platform
            did_intersect = new_x_rect.check_intersect(platform_rect)
                
                #if did_intersect is true, the player needs to collide with the side of a 
            #wall
            if (did_intersect):
                reset_x_vel = True
                #figure out if we intersected by either...
                #going too far left
                if (self.x_vel < 0):
                    distance_between_rectangles = x - (platform_rect.get_x() + platform_rect.get_width())
                    new_x = x - distance_between_rectangles
                #or too far right
                elif (self.x_vel > 0):
                    distance_between_rectangles = platform_rect.get_x() - (x + self.rect.get_width())
                    new_x = x + distance_between_rectangles
                #if we collided in the x without any x velocity, something went wrong!
            else:
                    print("That shouldn't have happened!")
                    new_x = x
        #if we collided at all, reset our x velocity
        if (reset_x_vel):
            self.x_vel = 0
        #finally, update our x position.
        x = new_x
        #----------------------------------------------------------------------------------#
        #check up/down collisions
        reset_y_vel = False
        for i in range(len(data.platforms)):
            #a rectangle of the player's potential new bounding box in 
        #the x direction
            new_y_rect = rectangle.rectangle(x, new_y, self.rect.get_height(), self.rect_get_width())
            platform_rect = data.platforms[i]

            #create a boolean value for if the potential rectangle intersects with
            #the platform
            did_intersect = new_y_rect.check_intersect(platform_rect.get_rect())
            
            #if did_intersect is true, the player needs to collide with the top or bottom of a 
        #platform
            if (did_intersect):
                reset_y_vel = True
                #figure out if we intersected by either...
                #going too far down
                if (self.y_vel < 0):
                    self.on_ground = True #important line of code -- allows us to jump!
                    distance_between_rectangles = y - (platform_rect.get_y() + platform_rect.get_height())
                    new_y = y - distance_between_rectangles
                #or too far up
                elif (self.y_vel > 0):
                    distance_between_rectangles = platform_rect.get_y() - (y + self.rect.get_height())
                    new_y = y + distance_between_rectangles
                #if we collided in the y without any y velocity, something went wrong!
            else:
                    print("That shouldn't have happened!")
                    new_y = y
        #if we collided at all, reset our y velocity
        if (reset_y_vel):
            self.y_vel = 0
        #finally, update our y position.
        y = new_y

        #now that we have our new x and y, return them.
        return [x,y]
    
    def goto(self, x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x_vel(self, v):
        self.x_vel = v

    def set_y_vel(self, v):
        self.y_vel = v

    def get_x_vel(self):
        return self.x_vel

    def get_y_vel(self):
        return self.y_vel

    def set_x_acc(self, v):
        self.x_acc = v

    def set_y_acc(self, v):
        self.y_acc = v

    def get_x_acc(self):
        return self.x_acc

    def get_y_acc(self):
        return self.y_acc