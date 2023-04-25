class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("L'âge est :", self.age)

    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, newAge):
        self.age = newAge
        print("L'âge a été modifié à :", self.age)

class Eleve(Personne):
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")
    
    def afficherMatiere(self):
        print("Matière enseignée :", self.matiereEnseignee)

personne = Personne()
eleve = Eleve()
prof = Professeur("Mathématiques")

personne.afficherAge()
personne.bonjour()
personne.modifierAge(16)

eleve.allerEnCours()
eleve.afficherAge()


prof.afficherMatiere()
prof.enseigner()
