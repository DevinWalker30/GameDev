from settings import *
from sprites import spriteSheet
import pygame as pg
import math
import random


def game_play():
    pg.init()
    screen = pg.display.set_mode([WIDTH, HEIGHT])
    clock = pg.time.Clock()
    playing = True

    tilemap = spriteSheet('RPG\imgs\tilemap.png')
    bow_img = tilemap.get_img(16*10, 16*11, 16, 16)
    explosion_sheet = spriteSheet('RPG\imgs\explosion.png')
    explosion_list = []

    for y in range(5):
        for x in range(5):
            loc_x = 64*x
            loc_y = 64*y
            image = explosion_sheet.get_img(loc_x, loc_y, 64, 64)

            image.set_colorkey(BLACK)
            explosion_list.append(image)


    while playing:
   
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        screen.fill(CAVE_GREY)
    

        screen.blit(explosion_list[0], (100, 500))

        pg.display.flip()

        clock.tick(FPS)

game_play()