"""
Écrire une class Python s'appelant Exo disposant d'une méthode appelée puissance implémentant la
fonction pow(x,n)
"""

class Exo:
    def puissance(self, x, n):
        # Cas de base
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.puissance(x, -n)
        else:
            return x * self.puissance(x, n - 1)

exo = Exo()
print(exo.puissance(2, 3))
print(exo.puissance(2, 1))
print(exo.puissance(2, 0))
print(exo.puissance(2, -3))
