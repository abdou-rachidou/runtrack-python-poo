class Vehicule:

    def __init__(self, marque, modele, annee, prix) -> None:
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix

    def informationsVehicule(self):
        infos = f"Marque = {self.__marque}\n" \
                f"Modèle = {self.__modele}\n" \
                f"Année = {self.__annee}\n" \
                f"Prix = {self.__prix} euros."
        return infos
    

class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix, portes=4) -> None:
        super().__init__(marque, modele, annee, prix)
        self.__portes = portes

    def informationsVehicule(self):
        infos = super().informationsVehicule()
        return f"{infos}\nNombre de portes = {self.__portes}"


voiture = Voiture(marque="Mercedes", modele="Class A", annee=2020, prix=18500, portes=4)

# Les infos sur la voitures
print(voiture.informationsVehicule())