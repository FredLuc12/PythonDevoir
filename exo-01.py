"""
Écrire un script Python permettant de trouver les groupes de 3 éléments dans une liste dont la 
somme est égal à 0
"""

tableau = [-1, 0, 1, 2, -1, -4]

def sommeTroisElement(tableau):
    tableau.sort() #trier
    triplets = []
    n = len(tableau)

    for i in range(n - 2):
        if i > 0 and tableau[i] == tableau[i - 1]:
            continue
        gauche, droite = i + 1, n - 1
        while gauche < droite:
            somme = tableau[i] + tableau[gauche] + tableau[droite]
            if somme == 0:
                triplets.append((tableau[i], tableau[gauche], tableau[droite]))

                while gauche < droite and tableau[gauche] == tableau[gauche + 1]:
                    gauche += 1
                while gauche < droite and tableau[droite] == tableau[droite - 1]:
                    droite -= 1

                gauche += 1
                droite -= 1
            elif somme < 0:
                gauche += 1
            else:
                droite -= 1
    return triplets

resultats = sommeTroisElement(tableau)
print("Les triplets dont la somme est égale à 0 sont :")
for triplet in resultats:
    print(triplet)
