import pygame as pg
import math
import random

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (31, 56, 102)
MOON_GREY = (143, 143, 143)
STEEL_GREY = (82, 82, 82)
STAR_WHITE = (250, 250, 250)
WINDOW_YELLOW = (217, 217, 46)
PLANE_GREY = (191, 191, 191)
PLANE_WINDOW = (1, 5, 51)
METEOR_GREY = (201, 201, 201)

FPS = 60
PI = math.pi

WIDTH = 1000
HEIGHT = 800

# set up
pg.init()

screen = pg.display.set_mode([WIDTH, HEIGHT])
clock = pg.time.Clock()

playing = True

x_coord = []
y_coord = []

for i in range(0,(WIDTH+HEIGHT)//25):
    x_coord.append(random.randint(10, WIDTH-10))
    y_coord.append(random.randint(10, HEIGHT//2))


# Create List
flakes = []
flake_spd = []
for i in range(150):
    loc = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
    flakes.append(loc)
    flake_spd.append(random.randint(1,3))

objects = []
obj_speed = []
for i in range(15):
    loc = [random.randint(WIDTH, WIDTH+50), random.randint(25, HEIGHT-25),50, 20]
    objects.append(loc)
    obj_speed.append(random.randint(2,5))



plane_coords = 0

x_speed = 0
y_speed = 0
mis_spd = 5

x_loc = 100
y_loc = HEIGHT*(1/3)
prop_height = [y_loc+7, y_loc+23]
click_pos = [0, 0]
points = 0
tot = 0
hit = 0
mx_loc = None
my_loc = None
mis_spd = 0
missles = []

font_score = pg.font.SysFont('georgia', 32)
font_restart = pg.font.SysFont('haettenschweiler', 98)
font_over = pg.font.SysFont('haettenschweiler', 246)
font_over_score = pg.font.SysFont('haettenschweiler', 128)

text_over = font_over.render('GAME OVER', True, RED)
text_restart = font_restart.render('PRESS RETURN TO RESTART', True, WHITE)

def draw_plane(x, y):
    pg.draw.line(screen, PLANE_GREY, (x-5, y-5), (x+15, y-5), width=3)
    pg.draw.line(screen, PLANE_GREY, (x+5, y+15), (x+5, y-5), width=5)
    pg.draw.line(screen, BLACK, (x+100, y+15), (x+105, y+15), width=3)
    pg.draw.line(screen, BLACK, (x+105, prop_height[0]), (x+105, prop_height[1]))
    pg.draw.ellipse(screen, PLANE_GREY, (x, y, 100, 30))
    pg.draw.rect(screen, BLACK, (x+60, y+40, 10, 5), border_top_right_radius=5, border_bottom_right_radius=5)
    pg.draw.ellipse(screen, PLANE_GREY, (x + 40, y, 25, 55))
    for i in range(5):
        pg.draw.circle(screen, PLANE_WINDOW, (x+(i*15)+25, y+12), 5)

def draw_block(x, y):
    pg.draw.rect(screen, BLACK, (x, y, 50, 50))

def draw_background():
    for i in range(WIDTH//2):
        pg.draw.rect(screen, BLACK, ((0 + (i*200)), HEIGHT*0.6875, 50, HEIGHT*0.4))
        pg.draw.rect(screen, WINDOW_YELLOW, ((10 + (i*200)), HEIGHT*0.725, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((26 + (i*200)), HEIGHT*0.7625, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((10 + (i*200)), HEIGHT*0.9125, 10, 10))
        pg.draw.rect(screen, BLACK, ((50 + (i*200)), HEIGHT*0.5625, 50, HEIGHT*0.45))
        pg.draw.rect(screen, WINDOW_YELLOW, ((60 + (i*200)), HEIGHT*0.6, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((76 + (i*200)), HEIGHT*0.6375, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((60 + (i*200)), HEIGHT*0.725, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((60 + (i*200)), HEIGHT*0.7875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((76 + (i*200)), HEIGHT*0.7875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((76 + (i*200)), HEIGHT*0.875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((60 + (i*200)), HEIGHT*0.9125, 10, 10))
        pg.draw.rect(screen, BLACK, ((100 + (i*200)), HEIGHT*0.625, 50, HEIGHT*0.4))
        pg.draw.rect(screen, WINDOW_YELLOW, ((110 + (i*200)), HEIGHT*0.65, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((126 + (i*200)), HEIGHT*0.6875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((126 + (i*200)), HEIGHT*0.7375, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((110 + (i*200)), HEIGHT*0.7875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((126 + (i*200)), HEIGHT*0.7875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((110 + (i*200)), HEIGHT*0.875, 10, 10))
        pg.draw.rect(screen, BLACK, ((150 + (i*200)), HEIGHT*0.75, 50, HEIGHT*0.3))
        pg.draw.rect(screen, WINDOW_YELLOW, ((160 + (i*200)), HEIGHT*0.7875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((176 + (i*200)), HEIGHT*0.7875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((176 + (i*200)), HEIGHT*0.875, 10, 10))
        pg.draw.rect(screen, WINDOW_YELLOW, ((160 + (i*200)), HEIGHT*0.9, 10, 10))
    pg.draw.arc(screen, STEEL_GREY, (WIDTH//3, HEIGHT//2, WIDTH//3, HEIGHT), 0, PI, width=20)

def draw_missle(x, y):
    pg.draw.rect(screen, BLACK, (x+62, y+41, 8, 4), border_top_right_radius=5, border_bottom_right_radius=5)

# main game loop
while playing:

    # event loop
    mouse_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                x_speed = -3
            elif event.key == pg.K_d:
                x_speed = 4
            elif event.key == pg.K_w:
                y_speed = -3
            elif event.key == pg.K_s:
                y_speed = 3
            if event.key == pg.K_SPACE:
                mis_spd = 5
                mx_loc = x_loc
                my_loc = y_loc
                missles.append([mx_loc, my_loc])
            if event.key == pg.K_RETURN and hit >= 3:
                    points = 0
                    hit = 0
                    x_loc = 100
                    y_loc = HEIGHT*(1/3)
                    prop_height = [y_loc+7, y_loc+23]
                    loc = []
                    objects = []
                    obj_speed = []
                    for i in range(15):
                        loc = [random.randint(WIDTH, WIDTH+50), random.randint(25, HEIGHT-25),50, 20]
                        objects.append(loc)
                        obj_speed.append(random.randint(2,5))
        elif event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_d:
                x_speed = 0
            elif event.key == pg.K_w or event.key == pg.K_s:
                y_speed = 0
        if event.type == pg.MOUSEBUTTONDOWN:
            click_pos = mouse_pos
    if x_loc >= WIDTH*(1/3)-50:
        x_speed = 0
        x_loc -= 1
    elif x_loc <= 10:
        x_speed = 0
        x_loc += 1
    if y_loc >= HEIGHT-50:
        y_speed = 0
        y_loc -= 1
        prop_height[0] -= 1
        prop_height[1] -= 1
    elif y_loc <= 25:
        y_speed = 0
        y_loc += 1
        prop_height[0] += 1
        prop_height[1] += 1
    for i in range(len(objects)):
        if (click_pos[0] > objects[i][0] and click_pos[0] < objects[i][0] + 50) and (click_pos[1] > objects[i][1] and click_pos[1] < objects[i][1] + 20):
            objects[i][0] = random.randint(WIDTH, WIDTH+50)
            objects[i][1] = random.randint(25, HEIGHT-25)
            points += 5
        if (((x_loc - 5 < objects[i][0] and x_loc + 105 > objects[i][0]) or (x_loc - 5 < objects[i][0] + 50 and x_loc + 105 > objects[i][0] + 50)) and ((y_loc - 5 < objects[i][1] and y_loc + 35 > objects[i][1]) or (y_loc - 5 < objects[i][1] + 20 and y_loc + 35 > objects[i][1] + 20))) or (((x_loc + 40 < objects[i][0] and x_loc + 65 > objects[i][0]) or (x_loc + 40 < objects[i][0] + 50 and x_loc + 65 > objects[i][0] + 50)) and ((y_loc + 35 < objects[i][1] and y_loc + 55 > objects[i][1]) or (y_loc + 35 < objects[i][1] + 20 and y_loc + 55 > objects[i][1] + 20))):
            objects[i][0] = random.randint(WIDTH, WIDTH+50)
            objects[i][1] = random.randint(25, HEIGHT-25)
            hit += 1
            if hit == 1:
                points = points//10 * 9
            elif hit == 2:
                points = points//10 * 7
            elif hit >= 3:
                for j in range(len(objects)):
                    obj_speed[j] = 0
                    objects[j][0] = WIDTH+50
        for j in range(len(missles)):
            if ((missles[j][0] > objects[i][0] and missles[j][0] < objects[i][0] + 50) or (missles[j][0] + 5 > objects[i][0] and missles[j][0] + 5 < objects[i][0] + 50)) and ((missles[j][1] > objects[i][1] and missles[j][1] < objects[i][1] + 20) or (missles[j][1] + 4 > objects[i][1] and missles[j][1] + 4 < objects[i][1] + 20)):
                objects[i][0] = random.randint(WIDTH, WIDTH+50)
                objects[i][1] = random.randint(25, HEIGHT-25)
                missles[j][0] = WIDTH + 150
                points += 5
    click_pos = [0, 0]

    pg.mouse.set_cursor(pg.cursors.broken_x)
    
    x_loc += x_speed
    y_loc += y_speed
    prop_height[0] += y_speed
    prop_height[1] += y_speed
    
    # game logic
    
    # clear screen
    screen.fill(DARK_BLUE)


    # draw code
    # pg.draw.line
    for i in range(0,len(x_coord)):
        pg.draw.circle(screen, STAR_WHITE, (x_coord[i], y_coord[i]), random.randint(2,3))
    pg.draw.circle(screen, MOON_GREY, (WIDTH//8, WIDTH//8), WIDTH*(7/80))
    draw_background()
    if missles:
        for missle in missles:
            missle[0] += mis_spd
            if missle[0] > WIDTH:
                missle[0] += 150
                missle[0] -= mis_spd
            draw_missle(missle[0], missle[1])
            

    draw_plane(x_loc, y_loc)
    # draw_block(mouse_pos[0], mouse_pos[1])
    # plane_coords += 3
    # if plane_coords > WIDTH:
    #     plane_coords -= (WIDTH+100)
    if prop_height[0] < y_loc+15:
        prop_height[0] += 1
        prop_height[1] -= 1
    elif prop_height[0] >= y_loc+15:
        for i in range(8):
            prop_height[0] -= 1
            prop_height[1] += 1

    for i in range(len(flakes)):
        pg.draw.circle(screen, WHITE, flakes[i], 1)
        flakes[i][1] += flake_spd[i]
        if flakes[i][1] > HEIGHT:
            flakes[i][0] = random.randint(0, WIDTH)
            flakes[i][1] -= HEIGHT

    for i in range(len(objects)):
        pg.draw.ellipse(screen, METEOR_GREY, objects[i])
        pg.draw.rect(screen, RED, (objects[i][0], objects[i][1], 10, 20), border_top_left_radius=15, border_bottom_left_radius=15)
        objects[i][0] -= obj_speed[i]
        if objects[i][0] <= -50:
            objects[i][0] = random.randint(WIDTH, WIDTH+50)
            objects[i][1] = random.randint(25, HEIGHT-25)
            tot += 1
    if tot >= 5:
        points += 1
        tot = 0
    text_score = font_score.render(f'Score: {points}', True, WHITE)
    text_hit = font_score.render(f'Times Been Hit: {hit}', True, WHITE)
    text_over_score = font_over_score.render(f'Score: {points}', True, WHITE)
    screen.blit(text_score, (WIDTH*(1/2), 20))
    screen.blit(text_hit, (WIDTH*(2/3), 20))
    if hit >= 3:
        screen.blit(text_restart, (WIDTH*(1/10), HEIGHT*(1/4)-100))
        screen.blit(text_over, (WIDTH*(1/10), HEIGHT*(1/4)))
        screen.blit(text_over_score, (WIDTH*(1/10)+60, HEIGHT*(1/4)+240))



    

    # update screen w/ drawings
    pg.display.flip()

    # lim to 'FPS' frames per
    clock.tick(FPS)

pg.quit()