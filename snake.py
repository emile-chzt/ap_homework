# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

from random import randint
import pygame as pg
l_case=20
pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
nbr_case=30
noir=(0, 0, 0)
blanc=(255, 255, 255)
vert= (0, 255, 0)
rouge=(255, 0, 0)
direction_tete = [1,0]
sens='droite'
snake = [(10 , 10), (11, 10)] 
fruit= (15, 15)
for i in range(nbr_case):
    for j in range(nbr_case):

        x = l_case*i # coordonnée x (colonnes) en pixels
        y = l_case*j # coordonnée y (lignes) en pixels
        
        if (-1)**(i+j)<0:

            rect = pg.Rect(x, y, l_case, l_case)
            # appel à la méthode draw.rect()
            pg.draw.rect(screen, noir, rect)
        else:
            rect = pg.Rect(x, y, l_case, l_case)
            # appel à la méthode draw.rect()
            pg.draw.rect(screen, blanc, rect)


pg.display.update()
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:
    clock.tick(2)
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP and sens != 'bas':
                direction_tete = (0,-1)
                sens= 'haut'
            elif event.key ==pg.K_DOWN and sens != 'haut':
                direction_tete = (0,1)
                sens= 'bas'
            elif event.key == pg.K_RIGHT and sens != 'gauche':
                direction_tete = (1,0)
                sens='droit'
            elif event.key ==pg.K_LEFT and sens !='droit':
                direction_tete = (-1, 0)
                sens= 'gauche'
        
    

    def effacer_queue(i,j):
        rect = pg.Rect(i*l_case , j*l_case, l_case, l_case)
        if (-1)**(i+j)<0:
            pg.draw.rect(screen, noir, rect)
        else: 
            pg.draw.rect(screen, blanc, rect)


    ligne_tete, col_tete=snake[-1][0], snake[-1][1]
    ligne_tete += direction_tete[0]
    col_tete += direction_tete[1]
    snake.append((ligne_tete, col_tete))

    if (ligne_tete, col_tete) !=fruit :
        effacer_queue(snake[0][0], snake[0][1])
        snake=snake[1:]
    elif ligne_tete>=30 or col_tete>=30 or ligne_tete<=0 or col_tete<=0 :

        snake=[(10,10), (11,10)]
    else:
        n=False
        while not n:
            a,b=randint(0,29), randint(0,29)
            if (a,b) not in snake:
                fruit=(a,b)
                n=True

    print(f'{ligne_tete=} {col_tete=} {fruit=}')

    rect_fruit = pg.Rect(fruit[0]*l_case, fruit[1]*l_case, l_case, l_case)
    pg.draw.rect(screen, vert, rect_fruit)


    
    for (i,j) in snake :
        x= i*l_case
        y= j*l_case
        rect = pg.Rect(x, y, l_case, l_case)
        pg.draw.rect(screen, rouge, rect)

    
    
    pg.display.update()
# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()