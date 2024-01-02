class Personne:


    def __init__(self, nom, prenom) -> None:
        self.surname = nom
        self.first_name = prenom
        pass

    def SePresenter(self):
        return f"Je suis {self.surname} {self.first_name}"

# Création d'instances de la classe Personne  
nom = "AROUNA"
prenom = "Abdou Rachidou"
full_name1 = Personne(nom, prenom)

nom = "BOTTERO"
prenom = "Mathis"
full_name2 = Personne(nom, prenom)

# Appel de la méthode SePresenter de l'instance
Personne1 = full_name1.SePresenter()
Personne2 = full_name2.SePresenter()
print(Personne1)
print(Personne2)