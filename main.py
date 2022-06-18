from entities import Player, Bullet, cmath

def find_angle(coords1, coords2): #compare le 2e set de coordonnées par rapport au premier
    x = coords2[0] - coords1[0]
    y = coords2[1] - coords1[1]
    return cmath.phase(complex(x, y))
