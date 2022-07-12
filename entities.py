import cmath
class Player():
    def __init__(self, x, y):
        self.coords = [x,y]

    def move(self, x, y):
        self.coords[0] += x
        self.coords[1] += y
        

class Bullet():
    def __init__(self, x, y, angle, range):
        self.coords = [x,y]
        self.angle = angle

    def shoot(self, canvas):    
        canvas.create_line(0,0,self.coords[0],self.coords[1], fill="white", width=3)