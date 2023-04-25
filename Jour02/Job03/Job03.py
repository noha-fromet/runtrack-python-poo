class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def perimetre(self):
        return (2 * (self.__longueur + self.__largeur))
        
    
    def surface(self):
        return(self.__largeur*self.__longueur)

class Parallélépipède(Rectangle):
        def __init__(self, longueur, largeur,hauteur):
            self.__longueur = longueur
            self.__largeur = largeur
            self.__hauteur = hauteur

        def get_longueur(self):
            return self.__longueur
        
        def set_longueur(self, longueur):
            self.__longueur = longueur
            
        def get_largeur(self):
            return self.__largeur
        
        def set_largeur(self, largeur):
            self.__largeur = largeur
        
        def get_heuteur(self):
                return self.__hauteur
            
        def set_hauteur(self, hauteur):
            self.__hauteur = hauteur


        def perimetre(self):
            return (2 * (self.__longueur + self.__largeur))
                                    
        def surface(self):
            return(self.__largeur*self.__longueur)
        
        def volume(self):
            return (self.__largeur*self.__longueur*self.__hauteur)


rect = Rectangle(10, 5)
para = Parallélépipède(10,5,15)

print("Longueur:", rect.get_longueur())
print("Largeur:", rect.get_largeur())
print("perimetre:",rect.perimetre())
print("surface:",rect.surface())
print("Volume:",para.volume())