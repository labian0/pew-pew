class Player():
    def __init__(self, x: int, y: int): #initial coords
        self.coords = [x,y]

    def move(self, direction, step):
        compass = {
        "north": (1, 1),
        "south": (1, -1),
        "west": (0, -1),
        "east": (0, 1)
        }
        ref = compass[direction] #ref[0] is wether this affects x or y, ref[1] multiplies the step (either positive or neg)
        self.coords[ref[0]] += step*ref[1]
        return self.coords