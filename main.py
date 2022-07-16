from entities import Player, Bullet, cmath
import tkinter

def main():
    f = tkinter.Tk()
    canvas = tkinter.Canvas(f, height=500, width=500, bg="black", bd=0)
    canvas.pack()
    player = Player(0, 0)
    def shoot(event):
        x,y = event.x,event.y
        bullet = Bullet(player.coords,(x, y), 250, canvas)
        bullet.shoot()

    player_oval = canvas.create_oval(player.coords[0]-10,player.coords[1]-10,player.coords[0]+10,player.coords[1]+10, fill="white")
    def move_player(event):
        directions = {
            "Right": (0, 1),
            "Down": (1, 1),
            "Left": (0, -1),
            "Up": (1, -1),
        }
        coords = [0,0]
        step = 10 #nombre de pixels traversés en 1 mouvement
        direction = directions[event.keysym] #direction[0] va décider de la coordonnée à changer (x ou y) et direction[1] va décider le signe du vecteur mouvement
        coords[direction[0]] += step*direction[1] 
        player.move(coords[0], coords[1]) #normalement, 1 de ces valeurs est forcément 0 et l'autre 10 ou -10
        canvas.move(player_oval, coords[0], coords[1])
    
    #le programme va ici
    canvas.bind('<Button-1>', shoot)
    f.bind_all('<Down>', move_player)
    f.bind_all('<Up>', move_player)
    f.bind_all('<Right>', move_player)
    f.bind_all('<Left>', move_player)

    f.mainloop()

if __name__ == "__main__":
    main()