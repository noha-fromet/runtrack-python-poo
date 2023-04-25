class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


operation=Operation()
resultat = operation.nombre1 +operation.nombre2

print ("le resultat est",resultat)
