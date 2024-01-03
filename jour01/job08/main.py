class Cercle:
    pi = 3.14
    
    def __init__(self, rayon) -> None:
        self.rayon = rayon

    def changer_rayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficher_infos(self):
        print(f"Rayon : {self.rayon}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")
        print(f"Diamètre : {self.diametre()}")

    def circonference(self):
        diametre = 2 * self.rayon
        return self.pi * diametre

    def aire(self):
        return self.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

# Exemple d'utilisation de la classe Cercle
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Afficher toutes les informations du cercle
cercle1.afficher_infos()
cercle2.afficher_infos()