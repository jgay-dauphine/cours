#!/usr/bin/python3
# coding: utf8

import time
import random

"""
Module contenant des fonctions relatives à la résolution et à la construction 
de grilles de sudoku
"""

"""
Representation de grilles:

A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5 
B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6 
--------+---------+---------    ------+------+-----     ------+------+-----
D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9 
E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2 
F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8 
--------+---------+---------    ------+------+-----     ------+------+-----
G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1 
H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4 
I1 I2 I3| I4 I5 I6| I7 I8 I9    1 . 4 |. . . |. . .     1 6 4 |8 7 5 |2 9 3
"""

"""
Notations:
    * Une grille se compose de 81 cases (square)
    * les colones (cols) sont numérotées de 1 à 9 et les lignes (rows) de A à I
    * un bloc est un ensemble de cases formant un tout
    * une unité (unit) est un ensemble de squares adjacents (ligne, colone, bloc)
    * les pairs d'une case sont l'ensemble des cases qui sont dans une unité
      avec la case considérée

Chaque square possède exactement 3 units et 20 pairs.
"""

"""
   A2   |        |                 |        |          A1 A2 A3|        |         
   B2   |        |                 |        |          B1 B2 B3|        |         
   C2   |        |         C1 C2 C3|C4 C5 C6|C7 C8 C9  C1 C2 C3|        |         
--------+--------+-------  --------+--------+--------  --------+--------+--------
   D2   |        |                 |        |                  |        |         
   E2   |        |                 |        |                  |        |         
   F2   |        |                 |        |                  |        |         
--------+--------+-------  --------+--------+--------  --------+--------+--------
   G2   |        |                 |        |                  |        |         
   H2   |        |                 |        |                  |        |         
   I2   |        |                 |        |                  |        |         
"""

"""
Un puzzle est résolu si et seulement si toutes ses unités se compose d'une 
permutation des chiffres 1 à 9.
"""

# Fonction de test :
def test():
    "A set of tests for our Sudoku fonctions."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print('All tests passed')

# Implémentation de la notion de square, unit et de grille
def cross(A, B):
    "Cross product of elements in A and B."
    return [a+b for a in A for b in B]

def grid_values(grid):
    """ Convertit une grille dans un dictionnaire {square: char} avec les '0'
    ou les '.' considérés comme des blancs.
    """
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81 # On vérifie que la taille est correcte
    return dict(zip(squares, chars))

# Méthode de lecture de la grille
def parse_grid(grid):
    """ Fonction permettant de convertir une grille en un dictionnaire des
    valeurs possible pour une case, {square: 'digits'} ou renvoit False
    si la grille n'est pas possible."""
    # print("inside parse_grid")
    # Au début toutes les cases peuvent contenir n'importe quel nombre
    values = dict((s, digits) for s in squares)
    # Maintenant on assigne les valeurs de la grille
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False # On renvoit False si on ne peut pas assigner d à s dans values
    return values

def assign(values, s, d):
    """ Elimine toutes les valeurs, sauf d, de values[s] et propage la
    contrainte aux autres éléments des pairs. Renvoit values, si une 
    incompatibilité est détectée, renvoit False."""
    #print("inside assign:", d, "=>",  s)
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        #display(values)
        #print()
        return values
    else:
        return False

def eliminate(values, s, d):
    """ Elimine d de values[s]; propage quand values <= 2.
    Renvoit values ou False si une incompatibilité est détectée."""
    # print('Inside eliminate:', d, 'not in', s)
    if d not in values[s]:
        # print(d, 'already not in', values[s])
        return values # le boulot est déjà fait
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        # print('Erreur, plus de possibilité pour', s) 
        return False # On vient d'éliminer la dernière possibilité => Erreur
    elif len(values[s]) == 1:
        # print('1 seule possibilité pour', s, ':', values[s])
        # print('Supression de', values[s], 'du set', peers[s])
        # Si values[s] est limité à une seule valeur, assigner cette valeur
        # et élminer cette valeur des pairs
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    # Si une valeur v est limité à une seule case possible dans une unité alors l'assigner :
    for u in units[s]:
        # on construit la liste des square ou la valeur d est possible
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False # la valeur d ne peut plus être placée
        elif len(dplaces) == 1 and len(values[dplaces[0]]) != 1:
            # print('Valeur possible pour la place', dplaces[0], ':', values[dplaces[0]])
            # d peut uniquement être placé là
            if not assign(values, dplaces[0], d):
                return False
    return values

def display(values):
    """ Affiche les values dans une grille 2D. """
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3+1)]*3)
    for r in rows:
        print(' ' + ''.join( (values[r+c] if values[r+c] in digits else '.').center(width) + 
                             ('| ' if c in '36' else '')
                for c in cols) )
        if r in 'CF': 
            print(line)

def solve(grid):
    return search(parse_grid(grid))

def search(values):
    """ Utilisation de la recherche en profondeur et de la propagation,
    on essaye toutes les valeurs possibles."""
    if values is False:
        return False # au cas où la grille ne soit pas possible
    if all(len(values[s]) == 1 for s in squares):
        return values # le problème est déjà résolu.
    # On choisit la case à modifier
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s] )

def some(seq):
    " Renvoit un élément de la liste qui est True. "
    for e in seq:
        if e: 
            return e
    return False

def isSolved(values):
    """ Une grille est complète si toutes les unités sont des permutations de 
    1 à 9. """
    def unitsolved(unit):
        return set(values[s] for s in unit) == set(digits)
    return values is not False and all(unitsolved(unit) for unit in unitlist)

def time_solve(grid):
    start = time.clock()
    values = solve(grid)
    t = time.clock() - start
    print('Solving:')
    display(grid_values(grid))
    print()
    if values :
        display(values)
    print('(%.2f secondes)' % t)
    print()
    return (t, isSolved(values))

# Création des variables internes
digits  = '123456789'
rows    = 'ABCDEFGHI'
cols    = digits

# Les squares sont le produit des lignes par les colones
squares = cross(rows, cols)

# Les unit sont :
# - les lignes  : cross(rows, c) pour tous les c
# - les colones : cross(r, cols) pour tous les r
# - les blocs   : cross(rs, cs)  pour rs dans 'ABC','DEF','GHI' et cs dans
#   '123', '456', '789'
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs)  for rs in ('ABC','DEF','GHI') for cs in ('123','456', '789')])

# Construction d'un dictionnaire qui pour chaque square donne les squares des
# units correspondantes
units = dict( (s, [u for u in unitlist if s in u]) for s in squares )

# Construction d'un dictionnaire pour les pairs d'une case :
peers = dict( (s, set(sum(units[s],[])) - set([s])) for s in squares )

test()

grid1 = '123456789...000000000000000000000000000000000000000000000000000000000000000000000'
grid2 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid3 = '000700800006000031040002000024070000010030080000060290000800070860000500002006000'
grid4 = '400053078852010039900000001080000624796304815205000700020071006310008950078500040'

time_solve(grid1)
time_solve(grid2)
time_solve(grid3)
time_solve(grid4)
