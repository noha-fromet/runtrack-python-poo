import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        for couleur in couleurs:
            for valeur in valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_carte(self):
        return self.paquet.pop()

def valeur_carte(carte):
    if carte.valeur == "As":
        return 11
    elif carte.valeur in ["Valet", "Dame", "Roi"]:
        return 10
    else:
        return int(carte.valeur)

def valeur_main(main):
    valeur = 0
    as_present = False
    for carte in main:
        valeur += valeur_carte(carte)
        if carte.valeur == "As":
            as_present = True
    if as_present and valeur > 21:
        valeur -= 10
    return valeur

def blackjack():
    jeu = Jeu()
    jeu.melanger_paquet()

    main_joueur = [jeu.distribuer_carte(), jeu.distribuer_carte()]
    main_croupier = [jeu.distribuer_carte(), jeu.distribuer_carte()]

    print(f"Main du joueur: {main_joueur[0]}, {main_joueur[1]}")
    print(f"Main du croupier: {main_croupier[0]}, X")

    while True:
        choix = input("Voulez-vous prendre une carte (O/N)? ")
        if choix.lower() == "o":
            carte = jeu.distribuer_carte()
            main_joueur.append(carte)
            print(f"Vous recevez: {carte}")
            print(f"Main du joueur: {main_joueur}")
            if valeur_main(main_joueur) > 21:
                print("Vous avez dépassé 21. Vous perdez.")
                return
        else:
            break

    while valeur_main(main_croupier) < 17:
        carte = jeu.distribuer_carte()
        main_croupier.append(carte)

    print(f"Main du croupier: {main_croupier}")

    if valeur_main(main_joueur) > valeur_main(main_croupier):
        print("Vous gagnez!")
    else:
        print("Le croupier gagne.")

blackjack()