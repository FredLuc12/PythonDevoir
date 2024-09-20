"""
Écrire un script Python permettant de générer une liste de deux listes à partir d'une phrase
La première liste contient la liste des mots de la phrase
La deuxième liste contient les espaces et les virgules qui séparent les mots
"""

import re

def generer_listes(phrase):
    # Utiliser une regex pour capturer les mots et les séparateurs (espaces, virgules)
    mots = re.findall(r"\b\w+(?:'\w+)?", phrase)
    separateurs = re.findall(r"[ ,]+", phrase)

    return [mots, separateurs]

exemple_1 = generer_listes("J'ai découvert Python cette semaine")
exemple_2 = generer_listes("J'ai découvert Python, cette semaine")
exemple_3 = generer_listes("J'ai découvert, Python, cette semaine")

print(exemple_1)
print(exemple_2)
print(exemple_3)
