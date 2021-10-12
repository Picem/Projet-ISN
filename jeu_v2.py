# coding=utf-8
from tkinter import *


# V1 : Le plateau
# V2 : Déplacement de la bestiole

# Définition des fonctions
def liste_decors(fichier):
    """Fonction qui construit la liste du décor en lisant un fichier texte représentant un niveau"""
    with open(fichier, 'r') as f:
        res = [list(ligne.strip()) for ligne in f]
    return res


def construit_plateau(decors2D):
    """Fonction qui dessine le plateau de jeu avec les données de la liste decors2D"""
    for i in range(len(decors2D)):
        for j in range(len(decors2D[i])):
            if decors2D[i][j] == 'X':
                x = plateau.create_image(j * 40, i * 40, image=img_X, anchor=NW, tags="x")
            if decors2D[i][j] == 'T':
                t = plateau.create_image(j * 40, i * 40, image=img_T, anchor=NW, tags="t")
            if decors2D[i][j] == 'H':
                h = plateau.create_image(j * 40, i * 40, image=img_H, anchor=NW, tags="h")
            if decors2D[i][j] == 'P':
                p = plateau.create_image(j * 40, i * 40, image=img_P, anchor=NW, tags="p")


def press_key(evt):
    """Quand on appuie sur une touche, on lajoute à la liste"""
    if evt.keysym not in touches:
        touches.append(evt.keysym)


def release_key(evt):
    """Quand on relâche la touche, on l"'"a retire"""
    if evt.keysym in touches:
        touches.remove(evt.keysym)


def position_1():
    """Retourne la case en NW"""
    listcase = plateau.find_overlapping((plateau.coords(bestiole)[0] - 2), (plateau.coords(bestiole)[1] + 5),
                                        (plateau.coords(bestiole)[0] - 2), (plateau.coords(bestiole)[1] + 5))

    if len(listcase) > 0:
        res = plateau.gettags(listcase[0])[0]
    else:
        res = "v"
    return res


def position_2():
    """Retourne la case en NE"""
    listcase = plateau.find_overlapping((plateau.coords(bestiole)[0] + 32), (plateau.coords(bestiole)[1] + 5),
                                        (plateau.coords(bestiole)[0] + 32), (plateau.coords(bestiole)[1] + 5))

    if len(listcase) > 0:
        res = plateau.gettags(listcase[0])[0]
    else:
        res = "v"
    return res


def position_3():
    """Retourne la case en SW"""
    listcase = plateau.find_overlapping((plateau.coords(bestiole)[0] - 2), (plateau.coords(bestiole)[1] + 42),
                                        (plateau.coords(bestiole)[0] - 2), (plateau.coords(bestiole)[1] + 42))

    if len(listcase) > 0:
        res = plateau.gettags(listcase[0])[0]
    else:
        res = "v"
    return res


def position_4():
    """Retourne la case en SE"""
    listcase = plateau.find_overlapping((plateau.coords(bestiole)[0] + 32), (plateau.coords(bestiole)[1] + 42),
                                        (plateau.coords(bestiole)[0] + 32), (plateau.coords(bestiole)[1] + 42))

    if len(listcase) > 0:
        res = plateau.gettags(listcase[0])[0]
    else:
        res = "v"
    return res

def boucle_jeu():
    """boucle de jeu principale"""
    global x_b, y_b
    
    print("pos1:"+ position_1())
    print("pos2:"+ position_2())
    print("pos3:"+ position_3())
    print("pos4:"+ position_4())

    

    if position_1() == "v" and position_2() == "v" and position_3() == "v" and position_4() == "v":
        y_b = y_b + 6
    if position_1() == "x" and position_2() == "v" and position_3() == "x" and position_4() == "v":
        y_b = y_b + 6
    if position_1() == "v" and position_2() == "x" and position_3() == "v" and position_4() == "x":
        y_b = y_b + 6

    if "Up" in touches:
        if position_1() != "t" and position_2() != "t" and position_1() != "x" and position_2() != "x" and \
                position_3() != "t" and position_4() != "t":
            y_b = y_b - 3

    if "Down" in touches:
        if position_3() != "t" and position_4() != "t" and position_3() != "x" and position_4() != "x":
            y_b = y_b + 3
            
    if "Left" in touches:
        if position_3() != "t" and position_1() != "t" and position_1() != "x":
            x_b = x_b - 3
        if position_3() == "t" and position_4() == "t":
            x_b = x_b - 3
        if position_3() == "t" and position_4() == "v":
            x_b = x_b - 3
        
    if "Right" in touches:
        if position_2() != "t" and position_4() != "t" and position_2() != "x":
            x_b = x_b + 3
        if position_3() == "t" and position_4() == "t":
            x_b = x_b + 3
        if position_3() == "x" and position_4() == "t":
            x_b = x_b + 3
        if position_3() == "v" and position_4() == "t":
            x_b = x_b + 3
        
    plateau.coords(bestiole, x_b, y_b)
    fenetre.after(20, boucle_jeu)


# Programme principal
fenetre = Tk()

# Configuration de la fenêtre
fenetre.resizable(width=False, height=False)
fenetre.title("Mon jeu")
fenetre.geometry("1000x680")

# Chargement des fichiers images :
img_T = PhotoImage(file="images/bloc_T.gif")
img_H = PhotoImage(file="images/bloc_H.gif")
img_X = PhotoImage(file="images/bloc_X.gif")
img_P = PhotoImage(file="images/gateau.gif")

img_bestioleG0 = PhotoImage(file="images/bestioleG0.gif")  # image bestiole position 0
img_bestioleG1 = PhotoImage(file="images/bestioleG1.gif")  # image bestiole position 1
img_bestioleD0 = PhotoImage(file="images/bestioleD0.gif")
img_bestioleD1 = PhotoImage(file="images/bestioleD1.gif")
img_bestioleM0 = PhotoImage(file="images/bestioleM0.gif")
img_bestioleM1 = PhotoImage(file="images/bestioleM1.gif")
img_bestioleT0 = PhotoImage(file="images/bestioleT0.gif")
img_bestioleT1 = PhotoImage(file="images/bestioleT1.gif")

# Création et positionnement du Canvas
plateau = Canvas(fenetre, width=1000, height=680, bg="#5736A6")
plateau.grid(row=0, column=0)
plateau.addtag_withtag("c", 186)


# Lecture du décor. On conserve les infos dans une liste afin de tester si on chute, si on peut monter, ...
decors2D = liste_decors('niveaux/niv1.txt')
construit_plateau(decors2D)

# On crée la bestiole :
x_b, y_b = 164, 604  # Position de la bestiole
bestiole = plateau.create_image(x_b, y_b, image=img_bestioleG0, anchor=NW)

# Surveillance des touches
touches = []
fenetre.bind_all("<KeyPress>", press_key)
fenetre.bind_all("<KeyRelease>", release_key)

boucle_jeu()

fenetre.mainloop()
