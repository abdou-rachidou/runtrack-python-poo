class Animal:


    def __init__(self):
        self.age = 0
        self.prenom = ""
        pass

    def vieillir(self):
        grandir = self.age + 1
        print(f"L'age de l'animal {grandir} ans")

    def nommer(self):
        self.prenom = "Luna"
        print("L'animal se nomme", self.prenom)


animal = Animal()
print(f"L'age de l'animal {animal.age} ans")
# Age de l'animal après la methode vieillir
grandir = Animal()
grandir.vieillir()
# Le nom de l'animal
first_name = Animal()
first_name.nommer()