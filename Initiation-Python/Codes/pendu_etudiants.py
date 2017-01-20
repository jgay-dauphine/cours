# -*- coding: utf-8 -*-
"""
Code d'un petit jeu du pendu en python
"""

# imports
import random

def display(mot, lettres):
    for i in range(len(mot)):
        if mot[i] in lettres:
            print(mot[i], sep='', end='')
        else:
            print('*', sep='', end='')
    print('')

def choixMot( liste_mots ):
    # Tirage d'un nombre aléatoire r
    r = random.randint(0, len(liste_mots)-1)
    # renvoi du mot numéro r
    return liste_mots[r]

# Déclaration des variables
mots = ['pythagore', 'wasabi', 'pamplemousse']
compteur = 8
l = []

# Choisir un mot
motSecret = choixMot(mots)
# print("Mot Secret: " + motSecret)

# tant qu'il reste un tour
while compteur > 0:
    # Afficher le mot
    display(motSecret, l)
    
    # demander une lettre
    lettre = input("Donnez une lettre : ").lower()
    print("lettre: #", lettre, "#", sep='')
    print("len(lettre):", len(lettre))
    if len(lettre) > 1:
        print("Veuillez ne taper qu'une seule lettre. Recommencez.")
        continue
    
    # test de la lettre
    if lettre in motSecret:
        print(lettre, "est dans le mot", motSecret)
        l.append(lettre)
    else:
        # incrémentation
        compteur -= 1
    """
    Version qui fonctionne mais moins jolie que celle au dessus.
    isLettreInMotSecret = False
    for i in range(len(motSecret)):
        if motSecret[i] == lettre:
            isLettreInMotSecret = True
            print(lettre, "est dans le mot", motSecret)
            break
    """

    # test victoire
    if set(motSecret) == set(l):
        print("Victoire ! Le mot était", motSecret)
        break

if compteur <= 0:
    print("Vous n'avez pas été assez rapide, vous avez perdu !")
