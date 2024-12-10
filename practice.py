import pygame as pg
import math

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
PI = math.pi

# set up
pg.init()

screen = pg.display.set_mode([600, 400])
clock = pg.time.Clock()

playing = True

# main game loop
while playing:

    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    # game logic
    
    # clear screen
    screen.fill(RED)

    # draw code
    pg.draw.rect(screen, BLUE, [20, 20, 560, 360])
    pg.draw.ellipse(screen, WHITE, [40, 40, 520, 320])
    pg.draw.arc(screen, GREEN, [60, 60, 480, 280], 0, 2*PI, width=10)

    # update screen w/ drawings
    pg.display.flip()

    # lim to 'FPS' frames per
    clock.tick(FPS)

pg.quit()