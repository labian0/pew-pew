import cmath
class Player():
    def __init__(self, x, y):
        self.coords = [x,y]

    def move(self, x, y):
        self.coords[0] += x
        self.coords[1] += y
        

class Bullet():
    def __init__(self, x, y):
        self.coords = [x,y]

    def shoot(self, angle):
        pass #à faire