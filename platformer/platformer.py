from settings import *
from components import Player, Brick, Enemy, Door, Key, Barrier
import pygame as pg
import math
import random

screen = pg.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pg.time.Clock()

ground_img = pg.image.load('platformer/imgs/ground_dirt.png')
rock_img = pg.image.load('platformer/imgs/ground_rock.png')
player_img = pg.image.load('platformer/imgs/side.png')
enemy_img = pg.image.load('platformer/imgs/alien_plant.png')
key_img = pg.image.load('platformer/imgs/key_yellow.png')

brick_list = []
enemy_list = []
door_list = []
surfaces_list = []
esurfaces_list = []
for row in range(len(LAYOUT)):
    y_loc = row * BRICK_HEIGHT

    for col in range(len(LAYOUT[0])):
        x_loc = col * BRICK_WIDTH

        if LAYOUT[row][col] == '1':
            brick = Brick(screen, x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT, rock_img)
            brick_list.append(brick)
            surfaces_list.append(brick)
            esurfaces_list.append(brick)

        elif LAYOUT[row][col] == 'g':
            brick = Brick(screen, x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT, ground_img)
            brick_list.append(brick)
            surfaces_list.append(brick)
            esurfaces_list.append(brick)

        elif LAYOUT[row][col] == 'l':
            door = Door(screen, DOOR_BROWN, x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT)
            door_list.append(door)
            surfaces_list.append(door)
            esurfaces_list.append(door)

        elif LAYOUT[row][col] == 'v':
            barrier = Barrier(screen, x_loc, y_loc)
            esurfaces_list.append(barrier)

        elif LAYOUT[row][col] == 'p':
            player = Player(x_loc, y_loc, PLAYER_WIDTH, PLAYER_HEIGHT, screen, player_img)
        
        elif LAYOUT[row][col] == 'e':
            enemy_list.append(Enemy(screen, x_loc + BRICK_WIDTH - ENEMY_WIDTH, y_loc + BRICK_HEIGHT - ENEMY_WIDTH, ENEMY_WIDTH, ENEMY_HEIGHT, enemy_img))

        elif LAYOUT[row][col] == 'k':
            key = Key(screen, x_loc + ENEMY_WIDTH, y_loc, ENEMY_WIDTH, ENEMY_HEIGHT, key_img)
            


playing = True

while playing:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            playing = False

    player.update(surfaces_list)
    player.get_key(key, door_list)
    for enemy in enemy_list:
        enemy.update(esurfaces_list)
        enemy.hit(player)

    if player.rect.x >= ((len(LAYOUT2[1]))*BRICK_WIDTH)-PLAYER_WIDTH:
        player.rect.y = (len(LAYOUT)-1)*BRICK_HEIGHT
        player.rect.x = 2*BRICK_WIDTH
        brick_list = []
        enemy_list = []
        door_list = []
        surfaces_list = []
        esurfaces_list = []
        for row in range(len(LAYOUT2)):
            y_loc = row * BRICK_HEIGHT

            for col in range(len(LAYOUT2[0])):
                x_loc = col * BRICK_WIDTH

                if LAYOUT2[row][col] == '1':
                    brick = Brick(screen, x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT, rock_img)
                    brick_list.append(brick)
                    surfaces_list.append(brick)
                    esurfaces_list.append(brick)

                elif LAYOUT2[row][col] == 'g':
                    brick = Brick(screen, x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT, ground_img)
                    brick_list.append(brick)
                    surfaces_list.append(brick)
                    esurfaces_list.append(brick)

                elif LAYOUT2[row][col] == 'l':
                    door = Door(screen, DOOR_BROWN, x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT)
                    door_list.append(door)
                    surfaces_list.append(door)
                    esurfaces_list.append(door)

                elif LAYOUT[row][col] == 'v':
                    barrier = Barrier(screen, x_loc, y_loc)
                    esurfaces_list.append(barrier)

                elif LAYOUT2[row][col] == 'p':
                    player = Player(x_loc, y_loc, PLAYER_WIDTH, PLAYER_HEIGHT, screen, player_img)
                
                elif LAYOUT2[row][col] == 'e':
                    enemy_list.append(Enemy(screen, x_loc + BRICK_WIDTH - ENEMY_WIDTH, y_loc + BRICK_HEIGHT - ENEMY_WIDTH, ENEMY_WIDTH, ENEMY_HEIGHT, enemy_img))

                elif LAYOUT2[row][col] == 'k':
                    key = Key(screen, x_loc + ENEMY_WIDTH, y_loc, ENEMY_WIDTH, ENEMY_HEIGHT, key_img)
    elif player.rect.x < 0:
        print("ggs")

    screen.fill(MOON_GREY)

    for brick in brick_list:
        brick.draw_brick()

    for door in door_list:
        door.draw_door()
    key.draw()

    player.draw_player()
    for enemy in enemy_list:
        enemy.draw()

    pg.display.flip()

    clock.tick(FPS)

pg.quit()
