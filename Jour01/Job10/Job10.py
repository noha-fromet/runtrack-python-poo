class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    def verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__en_marche == False and self.__reservoir > 5:
            self.__en_marche = True
            print("La voiture démarre")
        elif self.__en_marche == True:
            print("La voiture est déjà en marche")
        else:
            print("Le réservoir est trop faible pour démarrer")

    def arreter(self):
        if self.__en_marche == True:
            self.__en_marche = False
            print("La voiture s'arrête")
        else:
            print("La voiture est déjà arrêtée")

voiture = Voiture("Peugeot", "308", 2015, 80000)
print("Marque :", voiture.get_marque())
print("Modèle :", voiture.get_modele())
print("Année :", voiture.get_annee())
print("Kilométrage :", voiture.get_kilometrage())

voiture.set_marque("Renault")
voiture.set_modele("Clio")
voiture.set_annee(2020)
voiture.set_kilometrage(30000)

print("Nouvelle marque :", voiture.get_marque())
print("Nouveau modèle :", voiture.get_modele())
print("Nouvelle année :", voiture.get_annee())
print("Nouveau kilométrage :", voiture.get_kilometrage())

voiture.demarrer()
voiture.set_reservoir(10)
voiture.demarrer()
voiture.demarrer()
voiture.arreter()
voiture.arreter()
voiture.demarrer()
voiture.set_reservoir(2)
voiture.demarrer()
voiture.arreter()
