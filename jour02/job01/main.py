class Rectangle:


    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
        pass

    # Accesseurs (getters)
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    # Mutateurs (setters)
    def set_longueur(self, longueur_modifiee):
        self.__longueur = longueur_modifiee

    def set_largeur(self, largeur_modifiee):
        self.__largeur = largeur_modifiee

rectangle = Rectangle(10, 5)

# Afficher les valeurs initiales
print("Longueur initiale :", rectangle.get_longueur())
print("Largeur initiale :", rectangle.get_largeur())

# Modification de la longueur et de la largeur en utilisant les mutateurs
rectangle.set_longueur(13)
rectangle.set_largeur(7)

# Afficher les valeurs après modification
print("Longueur modifiée :", rectangle.get_longueur())
print("Largeur modifiée :", rectangle.get_largeur())