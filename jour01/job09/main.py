class Produit:
    def __init__(self, nom, prixHT, tva) -> None:
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.tva / 100)

    def afficher(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix HT : {self.prixHT} euros")
        print(f"TVA : {self.tva}%")
        print(f"Prix TTC : {self.calculerPrixTTC()} euros\n")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.tva

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 500, 10)

# Affichage des informations initiales
print("Informations initiales des produits :")
produit1.afficher()
produit2.afficher()

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Laptop")
produit1.modifierPrix(900)
produit2.modifierNom("Smartphone")
produit2.modifierPrix(550)

# Affichage des informations après modification
print("Informations après modification :")
produit1.afficher()
produit2.afficher()