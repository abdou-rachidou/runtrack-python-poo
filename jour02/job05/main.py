class Voiture:
    def __init__(self, marque, modele, annee, km) -> None:
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = km 
        self.en_marche = False
        self.__reservoire = 50

    def get_Marque(self):
        return self.__marque
    
    def get_Modele(self):
        return self.__modele
    
    def get_Annee(self):
        return self.__annee
    
    def get_Kilometrage(self):
        return self.__kilometrage
    
    def set_Marque(self, marque_modifiee):
        self.__marque = marque_modifiee
    
    def set_Modele(self, modele_modifiee):
        self.__modele = modele_modifiee

    def set_Annee(self, annee_modifiee):
        self.__annee = annee_modifiee

    def set_Kilometrage(self, kilometre_modifiee):
        self.__kilometrage = kilometre_modifiee

    def demarrer(self):
        if self.get_verifier_plein() > 5:
            self.en_marche = True
            print("La voiture peut se demarer :")
            return True
        else:
            print("Le réservoir est trop bas, veuillez faire le plein :")
        return False


    def arreter(self):
        if self.en_marche:
            self.en_marche = False
            return False
        
    def get_verifier_plein(self):
        return self.__reservoire
    
    def set_verifier_plein(self, reserve):
        self.__reservoire = reserve

    
    def InfosVoiture(self):
        print("Informations sur la voiture :")
        print(f"Marque : {self.get_Marque()}")
        print(f"Modèle : {self.get_Modele()}")
        print(f"Année : {self.get_Annee()}")
        print(f"Kilométrage : {self.get_Kilometrage()} km")


auto = Voiture("Tesla", "ModèleX", "2025", "150km/h")

# Modifier le reservoire
auto.set_verifier_plein(7)

# Afficher les informations de la voiture
auto.InfosVoiture()

# Démarrer la voiture
print(auto.demarrer())