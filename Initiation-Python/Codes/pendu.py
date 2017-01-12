#!/usr/bin/python3

# coding: utf-8

import random
import sys
import string

def chooseWord():
    word='swordfish'
    return word

def displayWord(word, letters):
    """
    Fonction permettant d'afficher le mot word
    en n'affichant que les lettres contenues dans
    le tableau letters
    Renvoit True si le mot est totalement découvert
    False sinon.
    """
    covered = True
    for i in range(len(word)):
        if letters.__contains__(word[i]):
            print(word[i], end='')
        else:
            print('*', end='')
            covered = False
    print()
    return covered

def extractLetter(line):
    line = line.lower()
    ret = None
    for i in range(len(line)):
        if string.ascii_lowercase.__contains__(line[i]):
            ret = line[i]
            break
    return ret

# Initialisation des variables :
compteur = 6 # Nombre de chance restantes
letters = []

secretWord = chooseWord()
print('#Debug:', secretWord)
found = displayWord(secretWord, letters)


while (not found) and compteur > 0:
    # On affiche le score actuel
    print('Il vous reste', compteur, 'mauvaises réponses.')
    # Un tour de jeu
    print('Entrer une lettre:', end=' ', flush=True)
    # On lit une lettre de l'input clavier
    # letter = input()[0]
    line = sys.stdin.readline()
    letter = extractLetter(line)
    letters.append(letter)
    if secretWord.__contains__(letter):
        # Si la lettre est là
        compteur += 0
    else:
        # Sinon
        compteur -= 1
    found = displayWord(secretWord, letters)

if compteur > 0:
    print('Bien joué !')
else:
    print('Perdu, pendu !')


