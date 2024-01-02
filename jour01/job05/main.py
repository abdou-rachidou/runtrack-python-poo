class Point:


    def __init__(self, x, y) -> None:
        self.horizontal = x
        self.vertical = y
        pass

    def afficherLesPoints(self):
        print("cordonnées des points :", self.horizontal, self.vertical)

    def afficherX(self):
        print("Cordonnée horizontale(x) :", self.horizontal)

    def afficherY(self):
        print("Cordonnée verticale(y) : ", self.vertical)

    def changerX(self, nouvelle_valeur_x):
        self.horizontal = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.vertical = nouvelle_valeur_y
        print("cordonnées des valeurs changées :", self.horizontal, self.vertical)

coordonnées = Point("60°", "25°")

#Afficher les point (x) et (y)
coordonnées.afficherLesPoints()

# Afficher la coordonnée horizontale (x)
coordonnées.afficherX()

# Afficher la coordonnée horizontale (y)
coordonnées.afficherY()

# Changement des valeurs de (x) et (y)
coordonnées.changerX("35°")
coordonnées.changerY("10°")