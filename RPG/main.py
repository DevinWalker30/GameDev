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

    tilemap = spriteSheet('RPG\imgs\\tilemap.png')
    map_list = []

    for y in range(4):
        for x in range(3):
            xloc = 16*x + x
            yloc = 16*y + y
            map_img = tilemap.get_img(xloc, yloc, 16, 16, scalex=15, scaley=15)

            map_img.set_colorkey(BLACK)
            map_list.append(map_img)
    scale = 15

    explosion_sheet = spriteSheet('RPG\imgs\explosion.png')
    explosion_list = []

    for y in range(5):
        for x in range(5):
            loc_x = 64*x
            loc_y = 64*y
            image = explosion_sheet.get_img(loc_x, loc_y, 64, 64)

            image.set_colorkey(BLACK)
            explosion_list.append(image)



    char_sheet = spriteSheet('RPG\imgs\spritesheet_characters.png')
    char_uzi = char_sheet.get_img(0, 0, 57, 43)
    char_pistol = char_sheet.get_img(57*2, 0, 52, 43)
    char_rifle = char_sheet.get_img(57*2-4, 43*3+3, 53, 43)
    char_holding = char_sheet.get_img(53*5-1, 43, 43, 43)
    char_up = char_sheet.get_img(57*6+7, 0, 39, 43)
    char_down = char_sheet.get_img(57*6+11, 43*3+3, 33, 43)
    
    
    char_uzi.set_colorkey(BLACK)
    char_pistol.set_colorkey(BLACK)
    char_rifle.set_colorkey(BLACK)
    char_holding.set_colorkey(BLACK)
    char_up.set_colorkey(BLACK)
    char_down.set_colorkey(BLACK)



    while playing:
   
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        screen.fill(CAVE_GREY)
    

        # screen.blit(explosion_list[0], (100, 500))

        for i in range(len(map_list)):
            if i<3:
                screen.blit(map_list[i], (i*16*scale, 0))
            elif i<6:
                screen.blit(map_list[i], (i*16*scale - (3*16*scale), (scale*16)))
            elif i<9:
                screen.blit(map_list[i], (i*16*scale - (6*16*scale), (scale*32)))
            elif i<12:
                screen.blit(map_list[i], (i*16*scale - (9*16*scale), (scale*48)))

        screen.blit(char_uzi, (100, 100))
        screen.blit(char_pistol, (200, 100))
        screen.blit(char_rifle, (300, 100))
        screen.blit(char_holding, (400, 100))
        screen.blit(char_up, (500, 100))
        screen.blit(char_down, (600, 100))

        pg.display.flip()

        clock.tick(FPS)

game_play()