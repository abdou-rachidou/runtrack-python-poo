class Joueur:
    def __init__(self, nom, numero, position) -> None:
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (Joueur {self.numero}, Position: {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}\n")


class Equipe:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:\n")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, numero_joueur, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.liste_joueurs:
            if joueur.numero == numero_joueur:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges

# Exemple d'utilisation
equipe1 = Equipe("FC BARCELONE ")
equipe2 = Equipe("FC REAL MADRID")

joueur1 = Joueur("LEWANDOWSKI", 9, "Attaquant")
joueur2 = Joueur("VALVERDE", 15, "Milieu de terrain")

equipe1.ajouterJoueur(joueur1)
equipe2.ajouterJoueur(joueur2)

# Simulation d'un match
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()

# Affichage des statistiques avant la mise à jour
print("STATISTIQUES DU JOUEUR :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Mise à jour des statistiques suite à un match
equipe1.mettreAJourStatistiquesJoueur(9, buts=2, passes=1)
equipe2.mettreAJourStatistiquesJoueur(15, jaunes=1)

# Affichage des statistiques après la mise à jour
print("STATISTIQUE DU JOUEUR APRES LA MISE A JOUR :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()