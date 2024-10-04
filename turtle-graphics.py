# _____________________________________________________Une Étoile

import turtle
etoile = turtle.Turtle()

nombreCotes = 5  # Le nombre de côtés
longueurCotes = 150  # La longueur des côtés
lesAngles = 720.0 / nombreCotes # Les angles / Le nombre de côtés

for i in range(nombreCotes):
    etoile.forward(longueurCotes)
    etoile.right(lesAngles)

etoile.hideturtle()
turtle.done()


# ____________________________________________________ Hexagone :

from turtle import *  # Importer tout depuis le module (turtle)


hexagone = Turtle() # Créer une tortue pour dessiner : Turtle()
taille = 50  # Pour définir la taille de l'hexagone manuellement

# Dessiner l'hexagone : 
for _ in range(6):
    hexagone.pensize('3')
    hexagone.pencolor('red')
    hexagone.forward(taille)
    hexagone.right(60)


# Masquer la tortue et garder la fenêtre ouverte avec "done()" 
hexagone.hideturtle()
done() 


# ______________________________________________________8 Étoiles Avec Un Fill(Jaune)

import turtle

# Créer une tortue pour dessiner
etoile = turtle.Turtle()

nombreCotes = 5  # Le nombre de côtés de l'étoile
longueurCotes = 100  # Longueur des côtés
lesAngles = 720.0 / nombreCotes  # Les angles / Le nombre de côtés


etoile.penup()  # Ne pas dessiner pendant le déplacement
etoile.goto(-75, 180)  # Positionner la tortue (commencer plus haut)
etoile.pendown()  # Dessiner

# Boucle pour dessiner mes 8 étoiles
for i in range(8):
    # Commencer le remplissage
    etoile.fillcolor('yellow')  
    etoile.begin_fill()  

    # Dessiner l'étoile
    for _ in range(nombreCotes):
        etoile.pencolor('blue')  # Couleur contours
        etoile.pensize('5')  # Épaisseur contour
        etoile.forward(longueurCotes)
        etoile.right(lesAngles)

    # Finir le remplissage (Yellow)
    etoile.end_fill()

    # Déplacer la tortue pour la prochaine étoile
    etoile.penup()  
    if i % 2 == 0:  # Si   (de la première étoile de la rangée)
        etoile.forward(120)  # Espacement pour la prochaine étoile
    else:  # Sinon   (de la deuxième étoile de la rangée)
        etoile.goto(-75, 180 - ((i // 2 + 1) * 100))  # Déplacer vers la ligne suivante
    etoile.pendown()  # Commencer à dessiner la prochaine étoile

# Masquer la tortue et garder la fenêtre ouverte avec  turtle.done()
etoile.hideturtle()
turtle.done()


# ____________________________________________________ Spirale De Couleurs :

from turtle import *

colors = ['red', 'blue', 'yellow', 'green']


for x in range(100): # Limiter le nombre d'itérations à (100)
    pencolor(colors[x % 4])
    width(x / 5 + 1)
    forward(x)
    left(20)

# Masquer la tortue et garder la fenêtre ouverte avec "done()"
hideturtle()
done()



# ____________________________________________________Spirale Carrée

from turtle import*

def square(T, S):
  for k in range(0,4):
    T.forward(S)
    T.left(90)

def repeat(T, f, N, A, S, k):
  for j in range(0, N):
    f(T, S)
    T.left(A)
    S = k*S


fred = Turtle()
fred.speed("fastest")     
repeat(fred, square, 108, 10, 200, 0.97)


done()


# __________________________________________________Spirale Pentagone RGB

from turtle import *
TL = Turtle()  # Crée un objet Turtle (Variable = TL)
TL.speed(0) # La vitesse de ma tortue(Avec la Variable = TL)
colormode(255)  # Pour utiliser les valeurs RGB

# Couleur de fond : 
bgcolor("black")

def pentagon(turtle):
    for k in range(0, 5):
        turtle.forward(150)
        turtle.left(72)

def repeat(figure, turtle, n, angle):
    for k in range(0, n):
        # Utiliser des couleurs RGB dynamiques pour chaque pentagone
        turtle.pencolor((k * 33 % 255, k * 66 % 255, k * 222 % 255)) 
        figure(turtle)
        turtle.left(angle)
    turtle.penup()
    turtle.forward(1000)

# Directement la fonction repeat() sans passer par run()
repeat(pentagon, TL, 20, 360/20)

done()


# ________________________________________________Un Flocon De Neige

from turtle import *

bgcolor('darkgrey')

def etoile(turtle, n, r):
    for k in range(0, n):
        turtle.pencolor('white')
        turtle.pendown()
        turtle.forward(r)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360 / n)

f = 0.3  # Facteur de redimensionnement

def recursive_etoile(turtle, n, r, depth):
    turtle.pencolor('white')
    global f
    if depth == 0:
        etoile(turtle, n, f * 10)
    else:
        for k in range(0, n):
            turtle.pendown()
            turtle.forward(r)
            recursive_etoile(turtle, n, f * r, depth - 1)
            turtle.penup()
            turtle.backward(r)
            turtle.left(360 / n)

# Créer une tortue et configurer la vitesse
T = Turtle()
T.speed("fastest")
# Pour recentrer la tortue avant de dessiner
T.penup()
T.pendown()

# Mes paramètres pour le nombre de branches et la profondeur récursive
n = 6  # Une étoile à 5 branches
r = 50  # Rayon initial de l'étoile
depth = 3  # Profondeur de la récursivité

# Appel de la fonction recursive_star()
recursive_etoile(T, n, r, depth)


T.hideturtle()


done()



# ________________________________________________6 Flocons De Neige


from turtle import *

bgcolor('darkgrey')

def etoile(turtle, n, r):
    for k in range(0, n):
        turtle.pencolor('white')
        turtle.pendown()
        turtle.forward(r)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360 / n)

f = 0.3  # facteur de redimensionnement

def recursive_etoile(turtle, n, r, depth):
    global f
    turtle.pencolor('white')
    if depth == 0:
        etoile(turtle, n, f * 10)
    else:
        for k in range(0, n):
            turtle.pendown()
            turtle.forward(r)
            recursive_etoile(turtle, n, f * r, depth - 1)
            turtle.penup()
            turtle.backward(r)
            turtle.left(360 / n)

# ----------------------[Optionnel]
# Désactiver le traçage :
tracer(0, 0)
# Cela désactive l'animation pendant que la tortue trace les étoiles, ce qui permet au programme de calculer et dessiner rapidement sans avoir à actualiser à chaque étape.
# ----------------------

# Créer une tortue et configurez la vitesse
T = Turtle()
T.speed("fastest")
T.penup()

                #  --- Positionnement : ---
# Positions pour 6 étoiles (sur 2 lignes et 3 colonnes)
# positions = [(-200, 100), (0, 100), (200, 100), (-200, -100), (0, -100), (200, -100)]

# Positions pour 6 étoiles (sur 3 lignes et 2 colonnes)
positions = [(-150, 150), (150, 150),  # Ligne du haut
             (-150, 0), (150, 0),      # Ligne du milieu
             (-150, -150), (150, -150)]  # Ligne du bas


# Les paramètres pour le nombre de branches et la profondeur récursive
n = 6  # Nombre de branches
r = 50  # Rayon initial de l'étoile
depth = 3  # Profondeur de la récursivité

# Dessiner 6 étoiles à différentes positions
for pos in positions:
    T.goto(pos)
    T.pendown()
    recursive_etoile(T, n, r, depth)
    T.penup()

# Masquer la tortue à la fin
T.hideturtle()

# -----------------[Optionnel]
# Une fois le dessin terminé, mettre à jour l'affichage en une seule fois.
update()
# -----------------


done()



# ________________________________________________Forme-Abstraite RGB (1)

from turtle import *
import colorsys


bgcolor("indigo")
pensize(3)
speed(0)

# Taille des étapes et initialisation des couleurs
n = 100
h = 0


penup()
goto(80, 20)  # Ajustement pour mieux centrer
pendown()

# Boucle du dessin
for i in range(90):
    c = colorsys.hsv_to_rgb(h, 1, 1.0)
    h += 1 / n
    color(c)
    left(250)
    forward(i * 2)
    right(40)
    backward(i * 3)
    circle(60, 90)



hideturtle()

done()




# ________________________________________________Un Arbre avec shape() & circle()

from turtle import *


# Configuration initiale :
bgcolor('black')
pensize(2)
color('green')  # Le tronc de l'arbre sera vert
left(90)
backward(100)
speed(200)
shape('turtle')

# Séquence de couleurs pour les cercles (feuilles/fleurs)
colors = ['lightgreen', 'lightgreen', 'yellow', 'lightgreen']

def arbre(i, color_index=0):
    if i < 10:
        return
    else:
        forward(i)
        
        
        color(colors[color_index % 3]) # Alterner les couleurs des cercles pour les feuilles/fleurs
        circle(3)
        
        
        color('green') # Remettre la couleur à vert pour le tronc et les branches
        
        # Appel récursif avec changement d'orientation : 
        left(30)
        arbre(3 * i / 4, color_index + 1)
        
        right(60)
        arbre(3 * i / 4, color_index + 1)
        
        left(30)
        backward(i)

# Dessiner l'arbre : "fonction = arbre()"
arbre(100)


hideturtle()

done()


# ________________________________________________Arbre Fractal (RGB)

from turtle import *

# Configurer la tortue : 
bgcolor('black')  # Couleur de fond
tracer(0, 0) # [Optionnel]
speed(0)
hideturtle()

# Fonction récursive pour dessiner l'arbre fractal incliné
def arbreRGB(x, y, length, direction):
    if length < 2:  # Condition d'arrêt de la récursion
        return
    up()
    goto(x, y)  # Aller à la position de départ
    down()
    seth(direction)  # Orienter la tortue dans la bonne direction
    pensize(length / 20)  # Ajuster la taille du trait
    color((0.5 - length / L * 0.5, 1 - length / L, 0.5))  # Couleur dégradée
    
    # Dessiner la branche
    fd(length)
    px, py = xcor(), ycor()  # Récupérer la position de la fin de la branche
    
    # Appels récursifs pour les deux sous-arbres
    arbreRGB(px, py, length * 0.7, direction + 30)
    arbreRGB(px, py, length * 0.7, direction - 30)


L = 100  # Taille plus petite pour s'adapter à des fenêtres plus petites
arbreRGB(0, -140, L, 90)  # Ajuster la position de l'arbre

# Mettre à jour l'affichage [Optionnel]
update()

# Mettre à jour l'affichage et terminer
done()




# ________________________________________________Arbre Marron

from turtle import *


bgcolor('black') 

# -----------------[Optionnel]
tracer(0, 0)

speed(0)
hideturtle()

# Fonction récursive pour dessiner l'arbre fractal (90deg)
def arbreMarron(x, y, length, direction, is_leaf=False):
    if length < 2:  # Condition d'arrêt de la récursion
        return
    up()
    goto(x, y)  # Aller à la position de départ
    down()
    
   
    if is_leaf:  # Si c'est une feuille colorer en Vert
        color("forestgreen")  # 
    else:  # Sinon colorer le tronc et les branches en Marron
        color("saddlebrown")  # 
    
    seth(direction)  # Orienter la tortue dans la bonne direction
    pensize(length / 20)  # Ajuster la taille du trait
    
    # Dessiner la branche
    fd(length)
    px, py = xcor(), ycor()  # Pour récupérer la position de la fin de la branche
    
    # Appels récursifs pour les deux sous-arbres
    arbreMarron(px, py, length * 0.7, direction + 30, is_leaf=(length < 5))
    arbreMarron(px, py, length * 0.7, direction - 30, is_leaf=(length < 5))

# Taille de l'arbre et position ajustée
L = 100  
arbreMarron(0, -150, L, 90) 

# -----------------[Optionnel]
update()


done()



# ________________________________________________Arbre Marron 2 (Plus De Feuilles)

from turtle import *


bgcolor('black')

# -----------------[Optionnel]
tracer(0, 0)

speed(0)
hideturtle()


def arbreMarron2(x, y, length, direction):
    if length < 5: 
        return
    up()
    goto(x, y)  
    down()
    
    
    color("saddlebrown")  
    seth(direction)  
    pensize(length / 20)  
    
    
    fd(length)
    px, py = xcor(), ycor()  
    
    
    arbreMarron2(px, py, length * 0.7, direction + 30)
    arbreMarron2(px, py, length * 0.7, direction - 30)
    
    # Dessiner les feuilles 
    if length < 15:  # Condition pour dessiner : (Plus De Feuilles)
        up()
        goto(px, py)  # Revenir à la position de la fin de la branche
        down()
        color("forestgreen")  
        circle(3)  # Dessiner une feuille


L = 100  
arbreMarron2(0, -150, L, 90)  

# -----------------[Optionnel]
update()


done()





# ______________________________________________Base De Flocon

from turtle import *

bgcolor('black')
 
def line(length):
    if length <= 5:
        forward(length)
        return
    for angle in (60, -120, 60, 0):
        line(length / 3)
        left(angle)
 
begin_fill()
color('firebrick3', 'wheat')
for _ in range(3):
    line(90)
    right(120)
end_fill()

hideturtle()

done()




# __________________________________15 Flocons (Avec Base De Flocon)

from turtle import *


def line(length):
    if length <= 5:
        forward(length)
        return
    for angle in (60, -120, 60, 0):
        line(length / 3)
        left(angle)

def snowflake(x, y, size):
    penup()  
    goto(x, y)  
    pendown()  

    begin_fill()
    color('white', 'white')  
    for _ in range(3):
        line(size)  # Utiliser la taille fournie
        right(120)
    end_fill()


bgcolor('black')  
speed(0)  # Vitesse maximale pour dessiner rapidement



# Définir les tailles des 15 flocons 
sizes = [35, 45, 55, 40, 30, 35, 40, 45, 50, 70, 35, 40, 55, 55, 45]  

# Positions fixes pour les flocons (ajustées pour éviter les chevauchements)
fixed_positions = [
    (100, 200),   # Flocon 1
    (-210, 180),  # Flocon 2
    (-80, 230),   # Flocon 3
    (0, 160),     # Flocon 4
    (50, 250),    # Flocon 5
    (180, 100),   # Flocon 6
    (70, 10),     # Flocon 7
    (-60, 60),    # Flocon 8
    (-190, 40),   # Flocon 9
    (160, -80),   # Flocon 10
    (-80, -70),   # Flocon 11
    (20, -160),    # Flocon 12
    (-240, -110),   # Flocon 13
    (-140, -200),    # Flocon 14
    (150, -210),  # Flocon 15
]

# Dessiner les 15 flocons de neige à des positions fixes
for i in range(len(fixed_positions)):
    size = sizes[i % len(sizes)]  # Prendre la taille correspondante (cycle à travers les tailles)
    x, y = fixed_positions[i]  # Prendre la position correspondante
    snowflake(x, y, size)  # Dessiner le flocon


hideturtle()

done()
