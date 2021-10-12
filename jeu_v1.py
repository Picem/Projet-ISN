from tkinter import *

# V1 : Le plateau

# Définition des fonctions
def liste_decors(fichier):
    """
    Fonction qui construit la liste du décors en lisant un fichier texte représentant un niveau
    """
    with open(fichier,'r') as f:
        res = [list(ligne.strip()) for ligne in f]
    return res

def construit_plateau(decors2D):
    """
    Fonction qui dessine le plateau de jeu avec les données de la liste decors2D
    """
    for i in range(len(decors2D)):
        for j in range(len(decors2D[i])):
            if decors2D[i][j] == 'X' :
                plateau.create_image(j*40, i*40, image=img_X, anchor=NW)
            if decors2D[i][j] == 'T' :
                plateau.create_image(j*40, i*40, image=img_T, anchor=NW)
            if decors2D[i][j] == 'H' :
                plateau.create_image(j*40, i*40, image=img_H, anchor=NW)
            if decors2D[i][j] =='P' :
                plateau.create_image(j*40, i*40, image=img_P, anchor=NW)

# Programme principal
fenetre=Tk()

# Configuration de la fenêtre
fenetre.resizable(width=False, height=False)
fenetre.title("Mon jeu")
fenetre.geometry("1200x680")

# Chargement des fichiers images :
img_T = PhotoImage(file="images/bloc_T.gif")
img_H = PhotoImage(file="images/bloc_H.gif")
img_X = PhotoImage(file="images/bloc_X.gif")
img_P = PhotoImage(file="images/gateau.gif")

# Création et positionnement du Canvas
plateau = Canvas(fenetre, width=1200, height=680, bg="#5736A6")
plateau.grid(row=0, column=0)
plateau.create_rectangle(1000, 0, 1200, 680, fill="grey", width=5, outline="white")
plateau.create_image(1100, 225 , image=img_P)
txt_score = plateau.create_text(1100, 275, text="0 gâteau(x) sur 5", font=("comic sans ms","12"), fill="#5736A6")


# Lecture du décors. On conserve les infos dans une liste afin de tester si on chute, si on peut monter, ...
decors2D = liste_decors('niveaux/niv1.txt')
construit_plateau(decors2D)

fenetre.mainloop()
