class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur

rect = Rectangle(10, 5)
print("Aire:", rect.aire())


