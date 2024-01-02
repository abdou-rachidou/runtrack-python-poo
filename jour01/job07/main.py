class Personnage:


    def __init__(self, x, y) -> None:
        self.position_x = x
        self.position_y = y
        pass

    def gauche(self):
        self.position_x -= 6

    def droite(self):
        self.position_x += 4

    def haut(self):
        self.position_y += 7
    
    def bas(self):
        self.position_y -= 2

    def position(self):
        return (self.position_x, self.position_y)
    
# Utilisation de la classe
joueur = Personnage(0, 0)

# Deplacement du personnage
joueur.gauche()
joueur.droite()
joueur.haut()
joueur.bas()
coordonnées = joueur.position()
print("La position actuelle est:", coordonnées)