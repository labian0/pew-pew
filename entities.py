import cmath

def find_angle(coords1, coords2): #compare le 2e set de coordonnées par rapport au premier
    x = coords2[0] - coords1[0]
    y = coords2[1] - coords1[1]
    return cmath.phase(complex(x, y))

def compare(a, b, biggest: bool): #compare deux nombres, si biggest est True, compare() retournera le plus grand nombre (je comptais appeler ce paramètre "croissant" au début)
    return (a*(a>b) + b*(b>a))*biggest + (a*(a<b) + b*(b<a))*(not biggest)

class Player():
    def __init__(self, x, y):
        self.coords = [x,y]

    def move(self, x, y):
        self.coords[0] += x
        self.coords[1] += y
        

class Bullet():
    def __init__(self, start: tuple or list, end: tuple or list, range, canvas):
        self.start_coords, self.canvas = start, canvas
        #bigger = compare(end[0], end[1], biggest=True)
        angle = find_angle(start, end)
        self.end_coords = (start[0] + cmath.cos(angle).real*range, start[1] + cmath.sin(angle).real*range)

    def draw(self):
        self.line = self.canvas.create_line(self.start_coords[0], self.start_coords[1], self.end_coords[0],self.end_coords[1], fill="white", width=3)
    
    def remove(self):
        self.canvas.delete(self.line)
    
    def shoot(self):
        self.draw()
        self.canvas.after(250, self.remove)