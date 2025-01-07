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