class Animal:
    def __init__(self):
        self.age = 0

    
    def vieillir(self):
        self.age += 1


animal = Animal()


print("l'age de l'animal", animal.age,"ans")
print("\033[90m" + "# age de l'animal apres appel de la methode de vieillir" + "\033[0m")
animal.vieillir()
print("l'age de l'animal", animal.age,"ans")

class Nommer:
    def __init__(self,nom):
        self.nom=nom
    def prenom(self):
        print ("L'animal se nomme ",self.nom)


nommer=Nommer("Luna")

nommer.prenom()