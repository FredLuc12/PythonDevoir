"""
Addition avec des listes
 Soit deux listes n1 et n2 permettant de coder deux nombre entiers positifs .
 n1 = [1,2,3]
 n2 = [7]
"""

def total(n1, n2):
    def liste_A_nombre(liste):
        total = 0
        puissance = len(liste) - 1
        for chiffre in liste:
            total += chiffre * (10 ** puissance)
            puissance -= 1
        return total

    nombre1 = liste_A_nombre(n1)
    nombre2 = liste_A_nombre(n2)

    somme = nombre1 + nombre2

    resultat = []
    while somme > 0:
        resultat.insert(0, somme % 10)
        somme //= 10

    return resultat or [0]

print(total([8, 4, 0], [8, 3]))
print(total([1, 8, 3], [7]))
print(total([1, 2, 3], [7]))