import pygame as pg
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
    


class Player():
    def __init__(self, x_loc, y_loc, display, pos):
        self.pos = pos
        self.run_up = False
        self.run_down = False
        self.run_right = False
        self.run_left = False

        self.current_frame = 0
        self.delay = 50
        self.last = pg.time.get_ticks()

        self.img = self.pos[0]
        self.rect = self.img.get_rect()

        self.rect.x = x_loc
        self.rect.y = y_loc
        self.display = display
        self.x_velo = 2
        self.y_velo = 2

    def draw_player(self):
        self.display.blit(self.img, self.rect)

    def update(self):
        self.y_change = 0
        self.x_change = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.x_change = -1*self.x_velo
            self.run_left = True
            
        if keys[pg.K_d]:
            self.x_change = self.x_velo
            self.run_right = True

        if keys[pg.K_w]:
            self.y_change = -1*self.y_velo
            self.run_up = True

        if keys[pg.K_s]:
            self.y_change = self.y_velo
            self.run_down = True
            
        # else:
        #     self.x_change = 0
        #     if self.run_left:
        #         self.img = self.pos[0].rotate(180)
        #         self.run_left = False
        #     elif self.run_up:
        #         self.img = self.pos[0].rotate(90)
        #         self.run_up = False
        #     elif self.run_down:
        #         self.img = self.pos[0].rotate(-90)
        #         self.run_down = False
        #     elif self.run_right:
        #         self.img = self.pos[0]
        #         self.run_right = False


        # for surface in surface_list:
        #     if surface.rect.colliderect(self.rect.x + self.x_change, self.rect.y, self.rect.width, self.rect.height):
        #         self.x_change = 0

        #     if surface.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
        #         if self.y_velo >= 0:
        #             y_change = surface.rect.top - self.rect.bottom
        #             self.landed = True
        #             self.y_velo = 0
        #         elif self.y_velo < 0:
        #             y_change = surface.rect.bottom - self.rect.top
        #             self.y_velo = 0

            
        self.rect.x += self.x_change
        self.rect.y += self.y_change