import initialfont,shape_pic
import pygame
from pygame import transform, font, mask, Surface, Rect, SRCALPHA, draw
import gc,os
from math import sin, cos, ceil
import simplejson



def load_font_process(font_name):
    y=initialfont.initial_font().initial_process()
    for font in y.FONT_CACHE:
        if font['name'] == font_name:
            return font
    raise AttributeError('Invalid font name. Should be one of %s' %
                         ", ".join([f['name'] for f in FONT_CACHE]))







def main:
    pass
if __name__=='__main__':
    y=initial_font().initial_process()

    pygame.init()

    TAG_PADDING = shape.initial_picture_para().TAG_PADDING


    convsurf = pygame.Surface((2 * TAG_PADDING, 2 * TAG_PADDING))
    convsurf.fill((255, 0, 255))
    convsurf.set_colorkey((255, 0, 255))
    draw.circle(convsurf, (0, 0, 0), (TAG_PADDING, TAG_PADDING), TAG_PADDING)
    CONVMASK = pygame.mask.from_surface(convsurf)

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
