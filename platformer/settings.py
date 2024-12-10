WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (31, 56, 102)
MOON_GREY = (143, 143, 143)
STEEL_GREY = (82, 82, 82)
STAR_WHITE = (250, 250, 250)
WINDOW_YELLOW = (217, 217, 46)
PLANE_GREY = (191, 191, 191)
PLANE_WINDOW = (1, 5, 51)
METEOR_GREY = (201, 201, 201)
DOOR_BROWN = (71, 30, 0)


FPS = 60

GRAVITY = 1

LAYOUT = ['111111111111111111111',
          '1                   l',
          '1                   l',
          '1                   l',
          '1k                  l',
          '111    11  111   1111',
          '1                   1',
          '1    1      111   e 1',
          '1 e             111 1',
          '111    111 11   e   1',
          '1   1          11   1',
          '1                   1',
          '1  111   e    11    1',
          '1       111         1',
          '1            111    1',
          '1 p v              e1',
          'ggggggggggggggggggggg']


LAYOUT2 = ['111111111111111111111',
           'l                   1',
           'l                   1',
           'l                   1',
           'l                   1',
           '111e             1111',
           '1       111         1',
           '1   1e       111   k1',
           '1                 e11',
           '111     11   1111   1',
           '1   1e            111',
           '1      11           1',
           '1e         111      1',
           '1111    11    111   1',
           '1                  g1',
           '1   v            egg1',
           'ggggggggggggggggggggg']

BRICK_WIDTH, BRICK_HEIGHT = 50, 40

PLAYER_WIDTH, PLAYER_HEIGHT = 30, 30

ENEMY_WIDTH, ENEMY_HEIGHT = 25, 25

DISPLAY_WIDTH = BRICK_WIDTH * len(LAYOUT[0])
DISPLAY_HEIGHT = BRICK_HEIGHT * len(LAYOUT)