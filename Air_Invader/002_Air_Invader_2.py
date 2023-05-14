import pygame as pg
import random

# Constant Variables :-
WIDTH,HEIGHT = 800,600
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 75,75
ENEMY_WIDTH,ENEMY_HEIGHT = 75,75
# VELOCITY = 5

# Initializing the pygame
pg.init()

# Screen setup
SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Space Invader')
icon = pg.image.load('Items/icon1.png')
pg.display.set_icon(icon)

# Background
background_img = pg.image.load('Items/space 6.jpg')
background = pg.transform.scale(background_img,(WIDTH,HEIGHT))

# Spaceship
spaceship_img = pg.image.load('Items/spaceship (11).png')
spaceship = pg.transform.scale(spaceship_img,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
spaceship_x = 370
spaceship_y = 480
spaceship_x_change = 0
spaceship_y_change = 0
speed = 0.8

# Enemy
enemy1_img = pg.image.load('Items/enemy (1).png')
enemy1 = pg.transform.rotate(pg.transform.scale(enemy1_img,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),180)
enemy1_x = random.randint(0,WIDTH-ENEMY_WIDTH)
enemy1_y = random.randint(10,80)
enemy_speed = 0.5
enemy1_x_change = enemy_speed
enemy1_y_change = 0

# Bullet
bullet_img = pg.image.load('Items/bullet (1).png')
bullet = pg.transform.rotate(pg.transform.scale(bullet_img,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),180)
bullet_x = random.randint(0,WIDTH-ENEMY_WIDTH)
bullet_y = random.randint(10,80)
bullet_speed = 1
bullet_x_change = 0
bullet_y_change = 0

def spaceship_control(x,y):
    SCREEN.blit(spaceship,(x,y))

def enemy_control(x,y):
    SCREEN.blit(enemy1,(x,y))


# Looping the screen
run = True
while run:

    # Filling the screen
    # SCREEN.fill('#030303')
    SCREEN.blit(background,(0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        # Spaceship Movement Control for LEFT and RIGHT
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                spaceship_x_change -= speed
            if event.key == pg.K_RIGHT:
                spaceship_x_change += speed
            if event.key == pg.K_UP:
                spaceship_y_change -= speed
            if event.key == pg.K_DOWN:
                spaceship_y_change += speed

        if event.type == pg.KEYUP:
            if event.key in [pg.K_LEFT,pg.K_RIGHT,pg.K_UP,pg.K_DOWN]:
                spaceship_x_change = 0
                spaceship_y_change = 0


    # Spaceship speed change
    spaceship_x += spaceship_x_change
    spaceship_y += spaceship_y_change

    # Enemy speed change
    enemy1_x += enemy1_x_change

    # Spaceship Boundary :-
    if spaceship_x <= 0:
        spaceship_x = 0
    elif spaceship_x >= 725:
        spaceship_x = 725
    if spaceship_y < 300:
        spaceship_y = 300
    elif spaceship_y > 500:
        spaceship_y = 500

    # enemy1 Boundary and Direction :-
    if enemy1_x <= 0:
        enemy1_x_change = enemy_speed
        enemy1_y += 8
    elif enemy1_x >= WIDTH-ENEMY_WIDTH:
        enemy1_x_change = -enemy_speed
        enemy1_y += 8
    elif enemy1_y >= HEIGHT - ENEMY_HEIGHT:
        enemy1_y = random.randint(10,80)

    spaceship_control(spaceship_x,spaceship_y)
    enemy_control(enemy1_x,enemy1_y)

    # Updating the Screen
    pg.display.update()


