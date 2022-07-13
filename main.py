from entities import Player, Bullet, cmath
import tkinter

def main():
    f = tkinter.Tk()
    canvas = tkinter.Canvas(f, height=500, width=500, bg="black", bd=0)
    def shoot_bullet(event):
        x,y = event.x,event.y
        proj = Bullet((250,250),(x, y), 250)
        proj.shoot(canvas)

    #le programme va ici
    canvas.bind('<Button-1>', shoot_bullet)

    canvas.pack()
    f.mainloop()

if __name__ == "__main__":
    main()