import pygame as pg

# Initializing pygame methods
pg.font.init()
pg.mixer.init()

# Constant Variables
WIDTH,HEIGHT = 1100,600          # For Screen named "surface"
MIDDLE_BORDER = pg.Rect(WIDTH//2 -5,0 , 10,HEIGHT)
HEALTH_FONT = pg.font.SysFont('comicsans',40)
WINNER_FONT = pg.font.SysFont('comicsans',100)
BULET_FIRE_SOUND = pg.mixer.Sound('Items/Gun+Silencer.mp3')
BULET_HIT_SOUND = pg.mixer.Sound('Items/Grenade+1.mp3')
FPS = 60
MAX_BULLETS = 10
VELOCITY = 7
BULLET_VELOCITY = 9
SPACESHIP_HEALTH = 15
YELLOW_HIT = pg.USEREVENT + 1
RED_HIT = pg.USEREVENT + 2
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 65,55
BACKGROUND = pg.transform.scale(pg.image.load('Items/space 7.jpg'),(WIDTH,HEIGHT))
YELLOW_SPACESHIP_IMAGE = pg.image.load('Items/spaceship (11).png')
YELLOW_SPACESHIP = pg.transform.rotate(pg.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),-90)
RED_SPACESHIP_IMAGE = pg.image.load('Items/spaceship (7).png')
RED_SPACESHIP = pg.transform.rotate(pg.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
scroll = 0
tiles = 3

# Surface Setup
SURFACE = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Air Invader')


def draw_window(yellow,red,red_bullets,yellow_bullets,red_health,yellow_health):
    global scroll
    # SURFACE.fill('#ffffff')
    for i in range(0,tiles):
        SURFACE.blit(BACKGROUND,(0,i*(-HEIGHT)+scroll))
    scroll += 1
    if abs(scroll) > HEIGHT:
        scroll = 0
    pg.draw.rect(SURFACE,'#0052a4',MIDDLE_BORDER)

    SURFACE.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    SURFACE.blit(RED_SPACESHIP,(red.x,red.y))
    
    red_health_text = HEALTH_FONT.render("Health : "+str(red_health),1,'#ffffff')
    yellow_health_text = HEALTH_FONT.render("Health : "+str(yellow_health),1,'#ffffff')
    SURFACE.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10 ,10))
    SURFACE.blit(yellow_health_text, (10,10))
    for bullet in red_bullets:
        pg.draw.rect(SURFACE,'#ff0000',bullet)
    for bullet in yellow_bullets:
        pg.draw.rect(SURFACE,'#d2d200',bullet)
    pg.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,'#ffffff')
    SURFACE.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2,HEIGHT//2 - draw_text.get_height()//2))
    pg.display.update()
    pg.time.delay(5000)

def yellow_movement_control(keys_pressed,yellow):
    if keys_pressed[pg.K_a] and yellow.x - VELOCITY > 0:          # LEFT
        yellow.x -= VELOCITY
    if keys_pressed[pg.K_d] and yellow.x + VELOCITY + yellow.width < MIDDLE_BORDER.x:  # RIGHT
        yellow.x += VELOCITY
    if keys_pressed[pg.K_w] and yellow.y - VELOCITY > 0:          # UP
        yellow.y -= VELOCITY
    if keys_pressed[pg.K_s] and yellow.y + VELOCITY < MIDDLE_BORDER.x:          # DOWN
        yellow.y += VELOCITY

def red_movement_control(keys_pressed,red):
    if keys_pressed[pg.K_LEFT] and red.x + VELOCITY > MIDDLE_BORDER.x+35:  # LEFT
        red.x -= VELOCITY
    if keys_pressed[pg.K_RIGHT] and red.x + VELOCITY < WIDTH-40:      # RIGHT
        red.x += VELOCITY
    if keys_pressed[pg.K_UP] and red.y - VELOCITY > 0:            # UP
        red.y -= VELOCITY
    if keys_pressed[pg.K_DOWN] and red.y + VELOCITY < MIDDLE_BORDER.x:          # DOWN
        red.y += VELOCITY

def bullet_control(yellow_bullets,red_bullets,yellow,red):
    global rbullet
    for ybullet in yellow_bullets:
        ybullet.x += BULLET_VELOCITY
        if red.colliderect(ybullet):
            pg.event.post(pg.event.Event(RED_HIT))
            yellow_bullets.remove(ybullet)
        elif ybullet.x > WIDTH:
            yellow_bullets.remove(ybullet)
        # try:                                             # Don't Uncomment this ladder.
        #     if ybullet.colliderect(rbullet):             # In case of uncomment, comment out the 'try-except' ladder
        #         yellow_bullets.remove(ybullet)           # of below for loop.
        #         red_bullets.remove(rbullet)
        # except:
        #     pass

    for rbullet in red_bullets:
        rbullet.x -= BULLET_VELOCITY
        if yellow.colliderect(rbullet):
            pg.event.post(pg.event.Event(YELLOW_HIT))
            red_bullets.remove(rbullet)
        elif rbullet.x < 0:
            red_bullets.remove(rbullet)
        try:
            if rbullet.colliderect(ybullet):
                yellow_bullets.remove(ybullet)
                red_bullets.remove(rbullet)
        except:
            pass


# Main Window
def main():
    yellow = pg.Rect(100,260,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pg.Rect(935,260,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pg.time.Clock()
    yellow_bullets = []
    red_bullets = []
    red_health = SPACESHIP_HEALTH
    yellow_health = SPACESHIP_HEALTH
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(yellow.x + yellow.width,yellow.y + yellow.height//2+5 , 10,5)
                    yellow_bullets.append(bullet)
                    BULET_FIRE_SOUND.play()
                if event.key == pg.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(red.x,red.y + red.height//2+5 , 10,5)
                    red_bullets.append(bullet)
                    BULET_FIRE_SOUND.play()
                if event.key == pg.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(yellow.x + yellow.width,yellow.y + yellow.height//2+5 , 10,5)
                    yellow_bullets.append(bullet)
                    BULET_FIRE_SOUND.play()
                if event.key == pg.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(red.x,red.y + red.height//2+5 , 10,5)
                    red_bullets.append(bullet)
                    BULET_FIRE_SOUND.play()
                if event.key == pg.K_r:
                    run = False
                if event.key == pg.K_ESCAPE:
                    run = False
                    rquit()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULET_HIT_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULET_HIT_SOUND.play()

        draw_window(yellow,red,red_bullets,yellow_bullets,red_health,yellow_health)
        keys_pressed = pg.key.get_pressed()
        yellow_movement_control(keys_pressed,yellow)
        red_movement_control(keys_pressed,red)
        bullet_control(yellow_bullets,red_bullets,yellow,red)

        winner_text = ""
        if red_health <= 0:
            winner_text = "Arthur Wins!"
        if yellow_health <= 0:
            winner_text = "Madara Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

    # pg.quit()
    main()

def rquit():
    pg.quit()

if __name__ == "__main__":
    main()
