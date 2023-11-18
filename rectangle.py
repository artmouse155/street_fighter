import turtle as trtl

class rectangle:

    x = 0
    y = 0
    height = 0
    width = 0

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    #return a boolean saying if this rectangle intersects another rectangle
    def check_intersect(self, rect2):
        
        #first, check if any corner coordinate is inside the other rectangle
        
        #check for rect1
        for point in self.get_points():
            if rect2.contains_point(point):
                return True
        
        #check for rect2
        points =  rect2.get_points()
        for point in points:
            if self.contains_point(point):
                return True

        #if no corner coordinate is inside the other rectangle, there is
        #still another way the rectangles could intersect; that is if they form
        # a cross shape, where only their centers intersect.

        #check for rect1
        if (self.x < rect2.get_x()):
            if (self.x + self.width > rect2.get_x() + rect2.get_width()):
                if (self.y < rect2.get_y()):
                    if (self.y + self.height > rect2.get_y() + rect2.get_height()):
                        return True

        #check for rect2
        if (self.x > rect2.get_x()):
            if (self.x + self.width < rect2.get_x() + rect2.get_width()):
                if (self.y > rect2.get_y()):
                    if (self.y + self.height < rect2.get_y() + rect2.get_height()):
                        return True
        #if we have not returned True yet, then (i'm pretty sure that) we didn't collide.
        return False

    def contains_point(self, point):
        p_x = point[0]
        p_y = point[1]
        if ((p_x > self.x) and (p_x < (self.x + self.width))):
            #print("X:" + str(p_x) + " is between" + str(self.x) + " and " + str(self.x + self.width))
            if ((p_y > self.y) and (p_y < (self.y + self.height))):
                #print("Y:" + str(p_y) + " is between" + str(self.y) + " and " + str(self.y + self.height))
                return True
        return False

    def get_points(self):
        x = self.x
        y = self.y
        h = self.height
        w = self.width
        p1 = [x,y]
        p2 = [x+w,y]
        p3 = [x+w, y+h]
        p4 = [x, y+h]
        return [p1,p2,p3,p4]

    def draw(self, turtle, color):
        t = turtle
        old_x = turtle.xcor()
        old_y = turtle.ycor()
        t.penup()
        t.fillcolor(color)
        t.goto(self.x, self.y)
        t.begin_fill()
        t.setx(self.x + self.width)
        t.sety(self.y + self.height)
        t.setx(self.x)
        t.sety(self.y)
        t.end_fill()
        t.goto(old_x, old_y)	

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
