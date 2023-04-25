class Livre:
    def __init__(self,titre,auteur,nombre_de_page):
        self.__titre=titre
        self.__auteur=auteur
        self.__nombre_de_page=nombre_de_page
    


    def info(self):
        print("titre:",self.__titre)
        print("auteur:", self.__auteur)
        print("nombre de page::", self.__nombre_de_page)

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
        
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_page(self):
        if self.__nombre_de_page<= 0:
            print ("Erreur.")
        else:
            return self.__nombre_de_page
    
    def set_nombre_de_page(self, nombre_de_page):
        self.__nombre_de_page = nombre_de_page
    
livre=Livre("La Plateforme","Paul",78)

print ("Le titre est :",livre.get_titre())
print ("L'auteur est:",livre.get_auteur())
print ("Le nombre de pages est :",livre.get_nombre_de_page())
