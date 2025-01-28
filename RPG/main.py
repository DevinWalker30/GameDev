from settings import *
from sprites import spriteSheet, Player, Wall, Token
import pygame as pg
import math
import random

level_num = 0

pg.font.init()
font_score = pg.font.SysFont('georgia', 32)

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.char_index = 0

        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        self.running = True

        self.tilemap = spriteSheet('RPG\imgs\\tilemap.png')
        self.map_list = []

        self.char_speedx = 0
        self.char_speedy = 0

        self.charx = 16*scale+16
        self.chary = 16*scale+16

        self.tokx = random.randint(16*scale, (len(LAYOUTS[0][0])-4)*scale*16)
        self.toky = random.randint(16*scale, (len(LAYOUTS[0])-4)*scale*16)

        self.score = 0

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

    
        self.wall_sprites = pg.sprite.Group()
        self.token_group = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self.player = Player(self.charx, self.chary, self.screen, self.char_list, self, self.map_list)
        self.all_sprites.add(self.player)

        self.token = Token(self.screen, self.tokx, self.toky, self.map_list[93], self)
        self.token_group.add(self.token)
        self.all_sprites.add(self.token)


        for row in range(len(LAYOUTS[0])):
            y_loc = row*16*scale

            for col in range(len(LAYOUTS[0][1])):
                x_loc = col*16*scale

                if LAYOUTS[level_num][row][col] == '1':
                            brick = Wall(self.screen, x_loc, y_loc, self.map_list[126])
                            self.wall_sprites.add(brick)
                            self.all_sprites.add(brick)

        self.run()

    def update(self):
        # run all updates

        self.player.update()

    def draw(self):
        # fill screen, draw objects, and flip
        self.screen.fill(BLACK)


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

                if LAYOUTS[level_num][row][col] == ' ':
                    self.screen.blit(self.map_list[0], (x_loc, y_loc))

                if LAYOUTS[level_num][row][col] == 'g':
                    self.screen.blit(self.map_list[1], (x_loc, y_loc))
            
                if LAYOUTS[level_num][row][col] == 'f':
                    self.screen.blit(self.map_list[2], (x_loc, y_loc))

                if LAYOUTS[level_num][row][col] == 'w':
                    self.screen.blit(self.map_list[43], (x_loc, y_loc))


        # for i in range(len(self.char_list)):
        #     self.screen.blit(self.char_list[i], (100, 100+(i*100)))

        # text_score = font_score.render(f'Score: {self.score}', True, WHITE)
        # self.screen.blit(text_score, (WIDTH/2, HEIGHT/2))
        self.screen.blit(self.char_uzi, (WIDTH/2, HEIGHT/2))
        self.all_sprites.draw(self.screen)

        pg.display.flip()

        self.update()

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