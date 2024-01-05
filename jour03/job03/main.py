class Tache:
    def __init__(self, titre, description, statut="Faire ou terminer") -> None:
        self.titre = titre
        self.description = description
        self.statut = statut

    def Titre(self):
        return self.titre

    def Des(self):
        return self.description

    def Stat(self):
        return self.statut


class ListeDeTaches:
    def __init__(self, taches=None) -> None:
        self.taches = taches if taches else []

    def travail(self, liste):
        self.taches = liste

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.Titre() != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.Titre() == titre:
                tache.statut = "Terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(f"{tache.Titre()} - {tache.Des()} ")

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.Stat() == statut]


# Exemple d'utilisation
tache1 = Tache("1.Les courses", "Acheter des légumes.")
tache2 = Tache("2.Réviser", "Chapitres 1-3.")
tache3 = Tache("3.Visite", "Aller voir tante Polly.")

liste_taches = ListeDeTaches([tache1, tache2, tache3])

print('\n')
print("A. La Liste des taches initiale :")
liste_taches.afficherListe()

# Ajouter une nouvelle tâche
nouvelle_tache = Tache("4.Faire du sport", "30 minutes de jogging.")
liste_taches.ajouterTache(nouvelle_tache)

print('\n')
# Afficher la liste mise à jour
print("B. La Listes des taches après l'ajout d'une nouvelle tache :")
liste_taches.afficherListe()

# Supprimer une tâche par titre
liste_taches.supprimerTache("2.Réviser")


# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie("1.Les courses")
liste_taches.marquerCommeFinie("3.Visite")

print('\n')
print("C. Liste des taches après suppression d'une tache :")
# Afficher la liste mise à jour
liste_taches.afficherListe()

print('\n')
# Filtrer la liste par statut
taches_terminées = liste_taches.filterListe("Terminée")
print("D. Tâches Terminées:")
for tache in taches_terminées:
    print(f"{tache.Titre()} - {tache.Des()} : {tache.Stat()}")