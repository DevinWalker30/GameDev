import pygame as pg
from settings import *
import math
import random

class spriteSheet():
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_img(self, x, y, width, height, scalex=None, scaley=None):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        if scalex and scaley:
            image = pg.transform.scale(image, (width*scalex, height*scaley))
        return image
    

class Player(pg.sprite.Sprite):
    def __init__(self, x_loc, y_loc, display, pos, game):
        pg.sprite.Sprite.__init__(self)

        self.game = game
        self.char_index = self.game.char_index
        self.pos = pos
        self.run_up = False
        self.run_down = False
        self.run_right = False
        self.run_left = False

        self.current_frame = 0
        self.delay = 50
        self.last = pg.time.get_ticks()

        self.image = self.pos[self.char_index]
        self.rect = self.image.get_rect()

        self.rect.x = x_loc
        self.rect.y = y_loc
        self.display = display
        self.x_velo = 2
        self.y_velo = 2

    def update(self):
        self.char_index = self.game.char_index
        self.face_right = pg.transform.rotate(self.pos[self.char_index], 0)
        self.face_up = pg.transform.rotate(self.pos[self.char_index], 90)
        self.face_left = pg.transform.rotate(self.pos[self.char_index], 180)
        self.face_down = pg.transform.rotate(self.pos[self.char_index], -90)
        self.y_change = 0
        self.x_change = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.x_change = -1*self.x_velo
            self.run_left = True
            self.run_right = False
            self.run_up = False
            self.run_down = False
            self.image = self.face_left
            
        elif keys[pg.K_d]:
            self.x_change = self.x_velo
            self.run_right = True
            self.run_left = False
            self.run_up = False
            self.run_down = False
            self.image = self.face_right

        elif keys[pg.K_w]:
            self.y_change = -1*self.y_velo
            self.run_up = True
            self.run_right = False
            self.run_left = False
            self.run_down = False
            self.image = self.face_up

        elif keys[pg.K_s]:
            self.y_change = self.y_velo
            self.run_down = True
            self.run_up = False
            self.run_right = False
            self.run_left = False
            self.image = self.face_down


        # else:
        #     self.x_change = 0
        #     if self.run_left:
        #         self.image = self.pos[0].rotate(180)
        #         self.run_left = False
        #     elif self.run_up:
        #         self.image = self.pos[0].rotate(90)
        #         self.run_up = False
        #     elif self.run_down:
        #         self.image = self.pos[0].rotate(-90)
        #         self.run_down = False
        #     elif self.run_right:
        #         self.image = self.pos[0]
        #         self.run_right = False

            
        self.rect.x += self.x_change
        self.collide_with_wall('x')
        self.rect.y += self.y_change
        self.collide_with_wall('y')


    def collide_with_wall(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.wall_sprites, False)

            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                self.x_change = 0
        

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.wall_sprites, False)

            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                self.y_change = 0

    def collide_with_token(self):
        hits = pg.sprite.spritecollide(self, self.game.token_group, True)



class Wall(pg.sprite.Sprite):
    def __init__(self, display, x, y, img):
        pg.sprite.Sprite.__init__(self)        

        self.display = display
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Token(pg.sprite.Sprite):
    def __init__(self, display, xloc, yloc, img, game):
        pg.sprite.Sprite.__init__(self)

        self.game = game
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = xloc
        self.rect.y = yloc
        self.display = display
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(img, (self.rect.width/self.game.scale*2, self.rect.height/self.game.scale*2))