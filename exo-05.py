"""
Le jeu "plus petit/plus grand" est un exercice de base de l'informatique. Le script génère un nombre
aléatoire et le joueur essaye de le retrouver. À chaque étape, le script indique si le nombre proposé
par le joueur est plus petit ou plus grand que le nombre qu'il a « choisi ».
Ici, l'objectif est de programmer la position inverse : le joueur choisit un nombre (dans sa tête) et le
script essaye de le retrouver. La difficulté du script est de détecter la tricherie du joueur :
"""

def plus_petit_plus_grand():
    print("Mémorisez un nombre entier entre 1 et 100, script va essayer de le retrouver. Ne trichez pas!")

    Min = 1
    Max = 100
    coups = 0
    dernier_propose = None

    while Min <= Max:
        coups += 1
        proposition = (Min + Max) // 2
        print(f"Script propose {proposition}... +, - ou G ?")
        reponse = input().strip()

        if dernier_propose is not None:
            if reponse == "-" and proposition <= dernier_propose:
                print(f"Tricheur !!! Vous avez dit '-' après avoir dit '+' pour {dernier_propose}.")
                print(f"J'ai gagné par forfait en {coups} coups !!")
                return

            if reponse == "+" and proposition >= dernier_propose:
                print(f"Tricheur !!! Vous avez dit '+' après avoir dit '-' pour {dernier_propose}.")
                print(f"J'ai gagné par forfait en {coups} coups !!")
                return

        if reponse == "+":
            Min = proposition + 1

        elif reponse == "-":
            Max = proposition - 1

        elif reponse == "G":
            print(f"Script a trouvé {proposition} en {coups} coups !!!")
            return

        else:
            print("Réponse non valide, veuillez répondre par +, - ou G.")
            coups -= 1  # Ne pas compter ce coup

        dernier_propose = proposition

    print("Le nombre n'a pas été trouvé... Peut-être une triche ?")

plus_petit_plus_grand()
