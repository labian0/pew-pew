from entities import Player, Bullet, cmath
import tkinter

def main():
    f = tkinter.Tk()
    canvas = tkinter.Canvas(f, height=500, width=500, bg="black", bd=0)
    player = Player(0, 0)
    def shoot_bullet(event):
        x,y = event.x,event.y
        proj = Bullet((250,250),(x, y), 250)
        proj.shoot(canvas)

    def move_player(event):
        directions = {
            "Right": (0, 1),
            "Down": (1, 1),
            "Left": (0, -1),
            "Up": (1, -1),
        }
        coords = player.coords
        step = 10 #nombre de pixels traversés en 1 mouvement
        direction = directions[event.keysym] #direction[0] va décider de la coordonnée à changer (x ou y) et direction[1] va décider le signe du vecteur mouvement
        coords[direction[0]] += step*direction[1] 
        player.move(coords[0], coords[1]) #normalement, 1 de ces valeurs est forcément 0 et l'autre 10 ou -10
        print(coords)
    
    #le programme va ici
    canvas.bind('<Button-1>', shoot_bullet)
    f.bind_all('<Down>', move_player)
    f.bind_all('<Up>', move_player)
    f.bind_all('<Right>', move_player)
    f.bind_all('<Left>', move_player)

    canvas.pack()
    f.mainloop()

if __name__ == "__main__":
    main()