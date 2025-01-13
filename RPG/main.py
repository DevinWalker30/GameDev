from settings import *
from sprites import spriteSheet
import pygame as pg
import math
import random

level_num = 0

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        self.running = True

        self.tilemap = spriteSheet('RPG\imgs\\tilemap.png')
        self.map_list = []

        self.load_imgs()


    def load_imgs(self):

        self.scale = scale
        for y in range(12):
            for x in range(12):
                xloc = 16*x + x
                yloc = 16*y + y
                map_img = self.tilemap.get_img(xloc, yloc, 16, 16, scalex=self.scale, scaley=self.scale)

                # map_img.set_colorkey(BLACK)
                self.map_list.append(map_img)


        explosion_sheet = spriteSheet('RPG\imgs\explosion.png')
        self.explosion_list = []

        for y in range(5):
            for x in range(5):
                loc_x = 64*x
                loc_y = 64*y
                image = explosion_sheet.get_img(loc_x, loc_y, 64, 64)

                image.set_colorkey(BLACK)
                self.explosion_list.append(image)


        char_sheet = spriteSheet('RPG\imgs\spritesheet_characters.png')
        self.char_list = []
        self.char_uzi = char_sheet.get_img(0, 0, 57, 43)
        self.char_pistol = char_sheet.get_img(57*2, 0, 52, 43)
        self.char_rifle = char_sheet.get_img(57*2-4, 43*3+3, 53, 43)
        self.char_holding = char_sheet.get_img(53*5-1, 43, 43, 43)
        self.char_up = char_sheet.get_img(57*6+7, 0, 39, 43)
        self.char_down = char_sheet.get_img(57*6+11, 43*3+3, 33, 43)
        
        
        self.char_uzi.set_colorkey(BLACK)
        self.char_pistol.set_colorkey(BLACK)
        self.char_rifle.set_colorkey(BLACK)
        self.char_holding.set_colorkey(BLACK)
        self.char_up.set_colorkey(BLACK)
        self.char_down.set_colorkey(BLACK)

        self.char_list.append(self.char_down)
        self.char_list.append(self.char_up)
        self.char_list.append(self.char_holding)
        self.char_list.append(self.char_pistol)
        self.char_list.append(self.char_rifle)
        self.char_list.append(self.char_uzi)


    def new(self):
        # create all game objects (sprites, groups)
        # call run() method
        
        self.run()

    def update(self):
        # run all updates
        pass

    def draw(self):
        # fill screen, draw objects, and flip
        self.screen.fill(CAVE_GREY)


        # for i in range(len(self.map_list)):
        #     if i<3:
        #         self.screen.blit(self.map_list[i], (i*16*self.scale, 0))
        #     elif i<6:
        #         self.screen.blit(self.map_list[i], (i*16*self.scale - (3*16*self.scale), (self.scale*16)))
        #     elif i<9:
        #         self.screen.blit(self.map_list[i], (i*16*self.scale - (6*16*self.scale), (self.scale*32)))
        #     elif i<12:
        #         self.screen.blit(self.map_list[i], (i*16*self.scale - (9*16*self.scale), (self.scale*48)))

        for row in range(len(LAYOUTS[0])):
            y_loc = row*16*scale

            for col in range(len(LAYOUTS[0][1])):
                x_loc = col*16*scale

                if LAYOUTS[level_num][row][col] == '1':
                    self.screen.blit(self.map_list[126], (x_loc, y_loc))

                if LAYOUTS[level_num][row][col] == ' ':
                    self.screen.blit(self.map_list[0], (x_loc, y_loc))

                if LAYOUTS[level_num][row][col] == 'g':
                    self.screen.blit(self.map_list[1], (x_loc, y_loc))
            
                if LAYOUTS[level_num][row][col] == 'f':
                    self.screen.blit(self.map_list[2], (x_loc, y_loc))

                if LAYOUTS[level_num][row][col] == 'w':
                    self.screen.blit(self.map_list[43], (x_loc, y_loc))

                if LAYOUTS[level_num][row][col] == 'p':
                    self.screen.blit(self.char_list[0], (x_loc, y_loc))


        # for i in range(len(self.char_list)):
        #     self.screen.blit(self.char_list[i], (100, 100+(i*100)))


        pg.display.flip()

    def events(self):
        # game loop events
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                if self.playing:
                    self.playing = False
                self.running = False

    def run(self):

        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


    def show_start_screen(self):
        # the screen to start the game
        pass

    def game_over_screen(self):
        # game over screen
        pass

game = Game()

game.show_start_screen()

while game.running:
    game.new()
    game.game_over_screen()

pg.quit()