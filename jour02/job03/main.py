class Livre:


    def __init__(self, titre, auteur, nb_de_pages, disponible = True) -> None:
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = nb_de_pages
        self.__disponible = disponible

        pass

    # Création des Ascenseurs
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_de_pages(self):
        return self.__pages
    
    def verifiction(self):
        return self.__disponible
        
    def get_emprunter(self):
        if self.verifiction():
            print("Le livre a été emprunté :")
            self.__disponible = False
            return True
    
    def set_emprunter(self):
        return not self.__disponible
        
    def rendre(self):
        if self.set_emprunter():
            print("Le livre a été rendu :")
            self.__disponible = True
            return self.verifiction() == False

        
    # Création des Mutateurs
    def set_titre(self, titre_modifiee):
        self.__titre = titre_modifiee
    
    def set_auteur(self, auteur_modifiee):
        self.__auteur = auteur_modifiee
    
    def set_nb_de_pages(self, nb_de_page_modifiee) -> int:
        self.__pages = nb_de_page_modifiee
    
livre = Livre("Things fall apart","Chinua ACHEBE", 350)

print("Titre :", livre.get_titre())
print("Auteur :", livre.get_auteur())
print("Nombre de page :", livre.get_nb_de_pages())
print("Disponibilité du livre :", livre.verifiction())
print(livre.get_emprunter())

# Afficher la disponibilité après emprunt
print("Disponible après emprunt :", livre.verifiction())
print(livre.rendre())