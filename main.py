import pygame import Surface
import gc
from math import sin, cos, ceil
import simplejson


class initialparameter:
    def __init__(self):
        self.TAG_PADDING=5
        self.TAG_CLOUD_PADDING=5 # Margins added to the whole image
        self.STEP_SIZE = 2 # relative to base step size of each spiral function
        self.RADIUS = 1
        self.ECCENTRICITY = 1.5
        self.LOWER_START = 0.45
        self.UPPER_START = 0.55
    def initial(fonts='fonts.json', fonts_dir='fonts',DEFAULT_FONT = 'Droid Sans',DEFAULT_PALETTE = 'default'):
        FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), fonts_dir)


        FONT_CACHE = simplejson.load(open(os.path.join(FONT_DIR, fonts), 'r'))

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










FONTS = {}
