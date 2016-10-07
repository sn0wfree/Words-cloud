import initialfont


from pygame import Surface
import gc,os
from math import sin, cos, ceil
import simplejson




pygame.init()
convsurf = Surface((2 * TAG_PADDING, 2 * TAG_PADDING))
convsurf.fill((255, 0, 255))
convsurf.set_colorkey((255, 0, 255))
draw.circle(convsurf, (0, 0, 0), (TAG_PADDING, TAG_PADDING), TAG_PADDING)
CONVMASK = mask.from_surface(convsurf)

LAYOUT_HORIZONTAL = 0
LAYOUT_VERTICAL = 1
LAYOUT_MOST_HORIZONTAL = 2
LAYOUT_MOST_VERTICAL = 3
LAYOUT_MIX = 4
LAYOUTS = (
           LAYOUT_HORIZONTAL,
           LAYOUT_VERTICAL,
           LAYOUT_MOST_HORIZONTAL,
           LAYOUT_MOST_VERTICAL,
           LAYOUT_MIX
           )

LAST_COLLISON_HIT = None





def main:
    pass
if __name__=='__main__':
    y=initialfont()
    FONTS = {}

    FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), y.fonts_dir)
    print os.path.isdir( FONT_DIR)
