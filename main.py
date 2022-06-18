import entities
joueur = entities.Player(0, 0)
print(joueur.coords)
joueur.move(1, 0)
print(joueur.coords)