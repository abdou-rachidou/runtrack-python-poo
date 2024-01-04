class Ville:
    def __init__(self, nom, nb_habitant) -> None:
        self.__nom = nom
        self.__nb_habitant = nb_habitant

    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitant


class Personne:
    def __init__(self, nom, age, ville) -> None:
        self.__name = nom
        self.__age = age
        self.__ville = ville

    def mon_objet(self):
        print(f"Population de la ville de {self.__ville.get_nom()} : {self.__ville.get_nb_habitants()}")

    def ajouterPopulation(self, ajout_nb_habitant):
        self.__ville._Ville__nb_habitant += ajout_nb_habitant
        
        print(f"Mise à jour de la population de la Ville de {self.__ville.get_nom()} {self.__ville.get_nb_habitants()} habitants")


# Utilisation
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

population_paris = Personne("Rach", "15 ans", paris)
population_marseille = Personne("Jean", "20 ans", marseille)

# Afficher la population des deux villes
population_paris.mon_objet()
population_marseille.mon_objet()

# Création des objets
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


# Arrivée de nouvelles personnes
john and myrtille.ajouterPopulation(2)
chloe.ajouterPopulation(1)