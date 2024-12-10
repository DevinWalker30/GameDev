from settings import *
import pygame as pg
import math
import random


class Player():
    def __init__(self, x_loc, y_loc, width, height, display, img):
        self.img = pg.transform.scale(img, (width-5, height+5))
        self.rect = self.img.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.width = width
        self.height = height
        self.display = display
        self.x_velo = 5

        self.y_velo = 0
        self.jumping = False
        self.jump_height = 15
        self.landed = True

    def draw_player(self):
        self.display.blit(self.img, self.rect)

    def update(self, surface_list):
        y_change = 0
        self.x_change = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.x_change = -1*self.x_velo
        if keys[pg.K_d]:
            self.x_change = self.x_velo

        if (keys[pg.K_SPACE] or keys[pg.K_w]) and not self.jumping and self.landed:
            self.jumping = True
            self.landed = False
            self.y_velo = -15
            

        if not keys[pg.K_SPACE]:
            self.jumping = False

        self.y_velo += GRAVITY

        if self.y_velo > 10:
            self.velo = 10
        y_change += self.y_velo

        if y_change > 0:
            self.landed = False

        for surface in surface_list:
            if surface.rect.colliderect(self.rect.x + self.x_change, self.rect.y, self.rect.width, self.rect.height):
                self.x_change = 0

            if surface.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                if self.y_velo >= 0:
                    y_change = surface.rect.top - self.rect.bottom
                    self.landed = True
                    self.y_velo = 0
                elif self.y_velo < 0:
                    y_change = surface.rect.bottom - self.rect.top
                    self.y_velo = 0

            
        self.rect.x += self.x_change
        self.rect.y += y_change

    
    def get_key(self, key, door_list):
        if key.rect.colliderect(self.rect.x + self.x_change, self.rect.y, self.rect.width, self.rect.height):
            key.rect.x = -40*BRICK_WIDTH
            for door in door_list:
                door.rect.x += 40*BRICK_WIDTH
        


class Brick:
    def __init__(self, display, x, y, width, height, img):
        self.img = pg.transform.scale(img, (width, height))
        self.rect = self.img.get_rect()

        self.display = display
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw_brick(self):
        self.display.blit(self.img, self.rect)


class Enemy:
    def __init__(self, display, xloc, yloc, width, height, img):
        self.img = pg.transform.scale(img, (width, height))
        self.rect = self.img.get_rect()
        self.display = display
        self.rect.x = xloc
        self.rect.y = yloc
        self.x_velo = 3

    def draw(self):
        self.display.blit(self.img, self.rect)

    def update(self, surface_list):
        self.rect.x -= self.x_velo

        for surface in surface_list:
            if surface.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height) and self.x_velo > 0:
                self.x_velo = -3
            elif surface.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height) and self.x_velo < 0:
                self.x_velo = 3

    def hit(self, char):
        if char.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
            char.rect.y = (len(LAYOUT)-3)*BRICK_HEIGHT
            char.rect.x = 2*BRICK_WIDTH


class Door:
    def __init__(self, display, color, x, y, width, height):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw_door(self):
        pg.draw.rect(self.display, self.color, self.rect)

class Key:
    def __init__(self, display, xloc, yloc, width, height, img):
        self.img = pg.transform.scale(img, (width + 5, height - 10))
        self.rect = self.img.get_rect()
        self.rect.x = xloc
        self.rect.y = yloc
        self.display = display

    def draw(self):
        self.display.blit(self.img, self.rect)

class Barrier:
    def __init__ (self, display, xloc, yloc):
        self.rect = pg.Rect(xloc, yloc, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.display = display