FPS = 60

scale = 4

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
CAVE_GREY = (120, 115, 115)

GRAVITY = 1


LAYOUTS = [['1111111111111111111',
            '1gp ww g    g    g1',
            '1   g w f         1',
            '1  g   w  g   f   1',
            '1    ff wwww g   g1',
            '1 g  f   g   wf   1',
            '1  g   g    g wg  1',
            '1   g   g    g  w 1',
            '1 g  g     f    w 1',
            '1 g     g      gw 1',
            '1   g       g  w  1',
            '1111111111111111111']]

WIDTH = (len(LAYOUTS[0][0])-3)*scale*16
HEIGHT = (len(LAYOUTS[0])-3)*scale*16