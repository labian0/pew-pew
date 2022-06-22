from entities import Player, Bullet, cmath
import tkinter

def find_angle(coords1, coords2): #compare le 2e set de coordonnées par rapport au premier
    x = coords2[0] - coords1[0]
    y = coords2[1] - coords1[1]
    return cmath.phase(complex(x, y))

def main():
    f = tkinter.Tk()
    canvas = tkinter.Canvas(f, height=500, width=500, bg="black", bd=0)
    #le programme va ici
    
    canvas.pack()
    f.mainloop()

if __name__ == "__main__":
    main()