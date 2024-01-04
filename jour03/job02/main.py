class CompteBancaire:

    def __init__(self, num_compte, nom, prenom, solde, decouvert = False) -> None:
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        pass

    def Numero_compte(self):
        return self.__num_compte
    
    def Nom(self):
        return self.__nom
    
    def Prenom(self):
        return self.__prenom
    
    def Solde(self):
        return self.__solde
    
    def afficher(self):
        print(f"Numéro de compte : {self.__num_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde total : {self.__solde} $")
        print(f"Autorisation de découvert : {self.__decouvert}")

    def afficherSolde(self):
        return self.__solde
    

    def versemment(self, montant_versement):
        self.__solde += montant_versement
        print(f"Solde total après virement : {self.__solde} $")

    
    def retrait(self, montant_retirer) -> int:
        if self.__solde >= montant_retirer or self.__decouvert:
            self.__solde -= montant_retirer
            return montant_retirer
        else:
            print("Opération de retrait impossible. Solde insuffisant.")
            return 0
        
    def agios(self, montant_agios):
        if self.__solde < 0:
            self.__solde -= montant_agios
            print(f"Solde après agios appliquer: {self.__solde} $")

    def verser(self, montant_versement):
        self.__solde += montant_versement


    def virement(self, compte_destinataire, montant):
        montant_retire = self.retrait(montant)
        if montant_retire > 0:
            compte_destinataire.verser(montant_retire)
            print("\n")
            print(f"Virement de {montant_retire} $ effectué vers le compte {compte_destinataire.Numero_compte()}")
            self.afficher()  # Afficher le solde après le virement
        else:
            print("Opération de virement impossible. Solde insuffisant.")


mon_compte = CompteBancaire("14587263", "RASHFORD", "Marcus", 5000, decouvert = True)
livret_A = CompteBancaire("14587586", "AROUNA", "Abdou", -2000)


# Le compte principal
mon_compte.afficher()
mon_compte.versemment(1000)
mon_compte.retrait(0)
mon_compte.agios(50)


# Versement sur le compte à découvert
mon_compte.virement(livret_A, 3500)
print("\n")

# Le livret A
livret_A.Solde()
livret_A.afficher()