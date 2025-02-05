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


LAYOUTS = [['111111111111111111111111111',
            '1gg ww g    g    g   gg  f1',
            '1   g w f  w   w  w   w gg1',
            '1  g   w  g   f   gg w g f1',
            '1    ff wwww g      gf w g1',
            '1 g  f   g   wf   ff  g w 1',
            '1  g   g    g wg  ggf  wg 1',
            '1   g   g    g  w   gg f g1',
            '1 g  g     f    w  g  w fg1',
            '1 g f   g      gw w g     1',
            '1   g   f   g    fwg w ww 1',
            '111111111111111111111111111']]

WIDTH = (len(LAYOUTS[0][0])-10)*scale*16
HEIGHT = (len(LAYOUTS[0])-3)*scale*16

MAP_WIDTH = len(LAYOUTS[0][0])*scale*16
MAP_HEIGHT = len(LAYOUTS[0])*scale*16