class Commande:
    def __init__(self, numero_commande) -> None:
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouterPlat(self, nom, prix):
        if nom not in self.__plats_commandes:
            self.__plats_commandes[nom] = {"prix": prix, "statut": "en cours"}
        else:
            print("Ce plat est déjà dans la commande.")

    def annulerCommande(self):
        self.__plats_commandes.clear()
        self.__statut_commande = "annulée"

    def __calculerTotal(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficherCommande(self):
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés:")
        for nom, plat in self.__plats_commandes.items():
            print(f"- {nom} ({plat['statut']}): {plat['prix']} euros")
        print(f"Statut de la commande : {self.__statut_commande}")
        print(f"Total à payer : {self.__calculerTotal()} euros\n")

    def calculerTVA(self, taux_tva):
        return self.__calculerTotal() * (taux_tva / 100)

# Exemple d'utilisation
commande1 = Commande(numero_commande="CMD123")
commande1.ajouterPlat(nom="Pizza", prix=12.5)
commande1.ajouterPlat(nom="Burger", prix=9.75)

# Affichage de la commande avant annulation
print("Commande avant annulation :")
commande1.afficherCommande()

# Calcul de la TVA
taux_tva = 10  # Exemple de taux de TVA de 10%
tva = commande1.calculerTVA(taux_tva)
print(f"TVA à payer : {tva} euros\n")

# Annulation de la commande
commande1.annulerCommande()

# Affichage de la commande après annulation
print("Commande après annulation :")
commande1.afficherCommande()