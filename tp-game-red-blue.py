
from turtle import *
import math

# ______________________________Game Red vs Blue Line : 

# Utilisation de la bibliothèque turtle pour créer un jeu basé sur un tableau de points et des lignes reliant ces points. 
# Un jeu de stratégie où deux joueurs (rouge et bleu) sélectionnent des points sur le tableau pour former des combinaisons gagnantes. 
# _____________________________


# Configuration de l'écran
screen = Screen() # l'écran
screen.setup(600, 500)  # Taille de l'écran
screen.title("Game Red Line vs Blue Line")  # Titre de la fenêtre
screen.setworldcoordinates(-1.5, -1.5, 1.5, 1.5)  # Définition des coordonnées du monde
screen.tracer(0, 0)  
bgcolor('light yellow')
hideturtle()  


# Fonction pour dessiner un point (dot) à une position donnée avec une couleur spécifiée :
def dessinerPoint(x, y, couleur):
    up()  # Ne pas dessiner en se déplaçant
    goto(x, y)  # Se déplacer à la position (x, y)
    color(couleur)  # Changer la couleur de la tortue
    dot(15)  # Dessiner un point de taille 15


# Fonction pour générer des points autour d'un cercle :
def genererPoints():
    r = []
    for angle in range(0, 360, 60):  # Boucle sur les angles tous les 60 degrés
        r.append((math.cos(math.radians(angle)), math.sin(math.radians(angle))))  
        # Ajouter les coordonnées (x, y) au tableau
    return r


# Fonction pour dessiner une ligne entre deux points :
def dessinerLigne(p1, p2, couleur):
    up()  # Lever le stylo
    pensize(3)  # Définir la taille du stylo à 3
    goto(p1)  # Se déplacer au premier point
    down()  # Commencer à dessiner
    color(couleur)  # Changer la couleur de la tortue
    goto(p2)  # Dessiner jusqu'au deuxième point


# Fonction pour dessiner le tableau de points :
def dessinerTableau():
    global pointsSelectionnés  # Accéder à la variable globale 'pointsSelectionnés'
    
    for i in range(len(points)):  # Pour chaque point
        if i in pointsSelectionnés:  # Si le point est sélectionné
            dessinerPoint(points[i][0], points[i][1], tour)  # Dessiner avec la couleur du tour actuel
        else:  # Sinon
            dessinerPoint(points[i][0], points[i][1], 'light green')  # Dessiner en vert clair (points)

# Fonction principale de dessin :
def dessiner():
    dessinerTableau()  # Dessiner le tableau de points
    for i in range(len(red)):  # Dessiner les lignes rouges
        dessinerLigne((math.cos(math.radians(red[i][0] * 60)), math.sin(math.radians(red[i][0] * 60))),\
                  (math.cos(math.radians(red[i][1] * 60)), math.sin(math.radians(red[i][1] * 60))),\
                  'red')
    for i in range(len(blue)):  # Dessiner les lignes bleues
        dessinerLigne((math.cos(math.radians(blue[i][0] * 60)), math.sin(math.radians(blue[i][0] * 60))),\
                  (math.cos(math.radians(blue[i][1] * 60)), math.sin(math.radians(blue[i][1] * 60))),\
                  'blue')      
    screen.update()  # Mettre à jour l'écran pour afficher les dessins


# Fonction appelée lorsqu'un clic est détecté sur l'écran :
def jouer(x, y):
    global pointsSelectionnés, tour, red, blue  # Accéder aux variables globales
    
    for i in range(len(points)):  # Pour chaque point
        dist = (points[i][0] - x) ** 2 + (points[i][1] - y) ** 2  # Calculer la distance au clic
        if dist < 0.001:  # Si la distance est suffisamment petite (clic sur le point)
            if i in pointsSelectionnés:  # Si le point est déjà sélectionné
                pointsSelectionnés.remove(i)  # Désélectionner le point
            else:  # Sinon
                pointsSelectionnés.append(i)  # Ajouter le point à la sélection
            break
    if len(pointsSelectionnés) == 2:  # Si deux points sont sélectionnés
        pointsSelectionnés = (min(pointsSelectionnés), max(pointsSelectionnés)) # Conserver l'ordre des points
        if pointsSelectionnés not in red and pointsSelectionnés not in blue:  # Si la sélection n'est pas déjà dans les lignes rouges ou bleues
            if tour == 'red':  # Si c'est le tour du rouge
                red.append(pointsSelectionnés)  # Ajouter la sélection aux lignes rouges
            else:  # Sinon
                blue.append(pointsSelectionnés)  # Ajouter la sélection aux lignes bleues
            tour = 'red' if tour == 'blue' else 'blue'  # Changer de tour
        pointsSelectionnés = []  # Réinitialiser la sélection
    dessiner()  # Dessiner les mises à jour
    r = verifierFinDePartie(red, blue)  # Vérifier si le jeu est terminé
    if r != 0:  # Si oui
        screen.textinput('Jeu Terminé!', r + ' Gagne!')  # Afficher le gagnant
        bye()  # Quitter le programme


# Fonction pour vérifier si le jeu est terminé : 
def verifierFinDePartie(r, b):
    if len(r) < 3: return 0  # Si le rouge a moins de 3 lignes, le jeu continue
    r.sort()  # Trier les lignes rouges
    for i in range(len(r) - 2):  # Boucle pour vérifier les combinaisons
        for j in range(i + 1, len(r) - 1):
            for k in range(j + 1, len(r)):
                # Vérifier si une combinaison gagnante est formée
                if r[i][0] == r[j][0] and r[i][1] == r[k][0] and r[j][1] == r[k][1]: 
                    return 'blue'  # Si oui, le bleu gagne
    if len(b) < 3: return 0  # Si le bleu a moins de 3 lignes, le jeu continue
    b.sort()  # Trier les lignes bleues
    for i in range(len(b) - 2):  # Boucle pour vérifier les combinaisons
        for j in range(i + 1, len(b) - 1):
            for k in range(j + 1, len(b)):
                # Vérifier si une combinaison gagnante est formée
                if b[i][0] == b[j][0] and b[i][1] == b[k][0] and b[j][1] == b[k][1]: 
                    return 'red'  # Si oui, le rouge gagne
    return 0  # Aucun gagnant


# Variables globales : 
pointsSelectionnés = []  # Liste pour stocker les points sélectionnés
tour = 'red'  # Tour actuel, commence par 'rouge'
points = genererPoints()  # Générer les points
red = []  # Liste pour stocker les lignes 'rouges'
blue = []  # Liste pour stocker les lignes 'bleues'

dessiner()  # Dessiner le tableau initial
screen.onclick(jouer)  # Détecter les clics de souris pour jouer
mainloop()  # Lancer la boucle principale



# ------------------------------------------- Résumé du fonctionnement du jeu : 

# Écran : Un écran est créé où le jeu sera affiché, avec un fond noir et une taille de 600x500 pixels.
# Points : Les points sont générés autour d'un cercle, et les joueurs sélectionnent des paires de points.
# Lignes : Les lignes sont dessinées entre les points sélectionnés pour chaque joueur (rouge ou bleu).
# Tour : Le jeu alterne entre les joueurs rouge et bleu à chaque sélection de deux points.


# Conditions de victoire : Le jeu vérifie à chaque tour si l'un des joueurs a formé une combinaison gagnante. Si c'est le cas, le jeu se termine et un message indique le gagnant.

# Le message indiquant le gagnant est généré dans la fonction jouer() et plus précisément dans la section où la fonction verifierFinDePartie() est appelée pour vérifier si le jeu est terminé. 
# Les étapes qui mènent à l'affichage du message de fin de jeu :

# def jouer(x, y):
#     global pointsSelectionnés, tour, red, blue    # Accéder aux variables globales
    
#     # (Code pour sélectionner des points)

#     dessiner()  # Dessiner les mises à jour
#     r = verifierFinDePartie(red, blue)        # Vérifier si le jeu est terminé
#     if r != 0:  # Si oui
#         screen.textinput('Jeu Terminé!', r + ' Gagne!')          # Afficher le gagnant
#         bye()          # Quitter le programme
