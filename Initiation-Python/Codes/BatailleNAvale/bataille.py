#!/usr/bin/python
# -*- coding: utf8 -*-

import platform
import os

def lancer_jeu():
    # Construire les grilles
    size_x = int(input("Quelle taille de la grille en abscisse : "))
    size_y = int(input("Quelle taille de la grille en ordonnée : "))
    game = build_game(size_x, size_y)

    place_ships(game, True)
    clean()
    place_ships(game, False)
    clean()
    # Gérer les tours de jeu
    tour = True # le premier joueur joue
    for i in range(6):
        display_new_turn(game,tour)
        display_game(game, tour)
        coords = ask_shoot(tour)
        display_shoot(game, tour, coords)
        display_game(game, tour)
        ask_end_turn(game, tour)
        tour = not tour
        clean()

def display_shoot(game, isP1, coords):
    g = game["grid_p1" if isP1 else "grid_p2"]
    adv = game["grid_p1_p2" if isP1 else "grid_p2_p1"]
    if g[coords[0]][coords[1]] == 1:
        print "Vous avez touché !"
        adv[coords[0]][coords[1]] = 1
    else:
        print "Coup dans l'eau."
        adv[coords[0]][coords[1]] = 2

def build_game(sx, sy):
    g1 = [ [0 for i in range(sx)] for j in range(sy)]
    g2 = [ [0 for i in range(sx)] for j in range(sy)]
    g3 = [ [0 for i in range(sx)] for j in range(sy)]
    g4 = [ [0 for i in range(sx)] for j in range(sy)]
    ret = dict()
    ret["size_x"] = sx
    ret["size_y"] = sy
    ret["grid_p1"] = g1
    ret["grid_p1_p2"] = g2
    ret["grid_p2"] = g3
    ret["grid_p2_p1"] = g4
    return ret

def display_game(game, isP1):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    g1 = game["grid_p1"]
    print "  " + alpha[:game["size_x"]] + "   " + "  " + alpha[:game["size_x"]]
    for j in range(game["size_y"]):
        if isP1 :
            sl1 = [ '.' if i == 0 else 'X' for i in game["grid_p1"][j] ]
            sl2 = [ '0' if i == 0 else '@' if i == 2 else 'X' for i in game["grid_p1_p2"][j] ]
        else :
            sl1 = [ '0' if i == 0 else '@' if i == 2 else 'X' for i in game["grid_p2_p1"][j] ]
            sl2 = [ '.' if i == 0 else 'X' for i in game["grid_p2"][j] ]
        print j+1, ''.join(sl1), " ", j+1, ''.join(sl2)

def place_ships(game, isP1):
    print "Entrez les coordonnées du bateau sous la forme : (x,y)"
    (x,y) = input()
    game["grid_p1" if isP1 else "grid_p2"][x][y] = 1

def ask_shoot(isP1):
    s = "Joueur 1" if isP1 else "Joueur 2"
    print s, "entrez les coordonnée à viser :"
    (x,y) = input()
    return (x,y)

def ask_end_turn(game, isP1):
    print("Appuyez sur une touche pour passer au tour du joueur suivant.")
    raw_input()

def display_new_turn(game, isP1):
    s = "Joueur 1" if isP1 else "Joueur 2"
    print s, "appuyez sur une touche pour commencer votre tour."
    raw_input()

def clean():
    clean_console(platform.system())

def clean_console(myos):
    """myos est le nom de mon OS"""
    commands = { "Windows": "cls", "Linux": "clear"}
    os.system(commands[myos])

if __name__ == "__main__":
    lancer_jeu()
