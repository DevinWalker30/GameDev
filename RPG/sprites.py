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
    def __init__(self, x_loc, y_loc, display, pos, game, map_list):
        pg.sprite.Sprite.__init__(self)

        self.game = game
        self.char_index = self.game.char_index
        self.pos = pos
        self.map_list = map_list
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
        self.collide_with_token()


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

        if hits:
            self.game.token = Token(self.display, random.randint(16*scale, (len(LAYOUTS[0][0])-1)*scale*16), random.randint(16*scale, (len(LAYOUTS[0])-1)*scale*16), self.map_list[93], self.game)
            self.game.token_group.add(self.game.token)
            self.game.all_sprites.add(self.game.token)
            self.game.score += 1


class Wall(pg.sprite.Sprite):
    def __init__(self, display, x, y, img):
        pg.sprite.Sprite.__init__(self)        

        self.display = display
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Background(pg.sprite.Sprite):
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

class Camera:

    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def get_view(self, sprite_object):
        return sprite_object.rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.x + WIDTH // 2
        y = -target.rect.y + HEIGHT // 2

        x = min(0, x)
        y = min(0, y)

        x = max(-1*(self.width - WIDTH), x)
        y = max(-1*(self.height - HEIGHT), y)

        self.camera = pg.Rect(x, y, self.width, self.height)

class Enemy(pg.sprite.Sprite):
    def __init__(self, x_loc, y_loc, display, img, game):
        pg.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.display = display
        self.game = game

        self.x_velo = 0
        self.y_velo = 0

    def update(self):
        self.face_right = pg.transform.rotate(self.image, 0)
        self.face_up = pg.transform.rotate(self.image, 90)
        self.face_left = pg.transform.rotate(self.image, 180)
        self.face_down = pg.transform.rotate(self.image, -90)

        self.n = 1

        def random_walk():
            self.n += 1
            rand_14 = random.randint(1,4)
            rand_120 = random.randint(1,20)
            if (rand_14 % 2) != 0:
                if rand_14 == 1:
                    self.x_velo = -1
                    self.image = self.face_left
                if rand_14 == 3:
                    self.x_velo = 1
                    self.image = self.face_right
                self.y_velo = 0
            if (rand_14 % 2) == 0:
                if rand_14 == 2:
                    self.y_velo = -1
                    self.image = self.face_up
                if rand_14 == 4:
                    self.y_velo = 1
                    self.image = self.face_down
                self.x_velo = 0
            if rand_120 == 5:
                self.x_velo = 0
                self.y_velo = 0

        pg.time.set_timer(random_walk(), 5000*self.n)

        self.rect.x += self.x_velo
        self.collide_with_wall('x')
        self.collides_with_player('x')
        self.rect.y += self.y_velo
        self.collide_with_wall('y')
        self.collides_with_player('y')

        # self.collides_with_player('x')
        # self.collides_with_player('y')


    def collides_with_player(self, dir):
        
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.player_group, True)

            if hits:
                self.game.player = Player(self.game.charx, self.game.chary, self.game.screen, self.game.char_list, self.game, self.game.map_list)
                self.game.player_group.add(self.game.player)
                self.game.all_sprites.add(self.game.player)
                self.game.deaths += 1

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.player_group, True)

            if hits:
                self.game.player = Player(self.game.charx, self.game.chary, self.game.screen, self.game.char_list, self.game, self.game.map_list)
                self.game.player_group.add(self.game.player)
                self.game.all_sprites.add(self.game.player)
                self.game.deaths += 1
    
    def collide_with_wall(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.wall_sprites, False)

            if hits:
                if self.x_velo > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.rect.x -= 5
                if self.x_velo < 0:
                    self.rect.x = hits[0].rect.right
                    self.rect.x += 5
                self.x_velo = 0
        

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.wall_sprites, False)

            if hits:
                if self.y_velo > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.rect.y -= 5
                if self.y_velo < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.rect.y += 5
                self.y_velo = 0