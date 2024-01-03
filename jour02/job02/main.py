class Livre:


    def __init__(self, titre, auteur, nb_de_pages) -> None:
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = nb_de_pages
        pass

    # Création des Ascenseurs
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_de_pages(self):
        return self.__pages
    
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

# Les modifications
livre.set_titre("Discours de la méthode")
livre.set_auteur("DESCARTES")
livre.set_nb_de_pages(608)

# Afficher les modifications
print("Titre modifié :", livre.get_titre())
print("Auteur modifiée :", livre.get_auteur())
print("Nombre de page modifiée :", livre.get_nb_de_pages())