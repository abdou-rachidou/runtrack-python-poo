class Rectangle:
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        # Convertion les valeurs en nombres avant d'effectuer le calcul
        longueur = float(self.__longueur.replace("cm", "").strip())
        largeur = float(self.__largeur.replace("cm", "").strip())
        return 2 * (longueur + largeur)

    def surface(self):
        # Convertion les valeurs en nombres avant d'effectuer le calcul
        longueur = float(self.__longueur.replace("cm", "").strip())
        largeur = float(self.__largeur.replace("cm", "").strip())
        return longueur * largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur_modifiee):
        self.__longueur = longueur_modifiee

    def set_largeur(self, largeur_modifiee):
        self.__largeur = largeur_modifiee


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur) -> None:
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        # Convertion des valeurs en nombres avant d'effectuer le calcul
        longueur = float(self.get_longueur().replace("cm", "").strip())
        largeur = float(self.get_largeur().replace("cm", "").strip())
        hauteur = float(self.__hauteur.replace("cm", "").strip())
        return longueur * largeur * hauteur


# Exemple des instances
rectangle = Rectangle("20 cm", "10 cm")
print("Le périmètre du Rectangle est :", rectangle.perimetre(), "cm")
print("La surface du Rectangle est :", rectangle.surface(), "cm²")

parallelepipede = Parallelepipede("20 cm", "10 cm", "50 cm")
print("Le volume du Parallélépipède est :", parallelepipede.volume(), "cm³")