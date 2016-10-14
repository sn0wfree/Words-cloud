# -*- coding: utf-8 -*-


import pygame
import initialfont




def load_font_process(multi_font_feature = True):
    y=initialfont.initial_font()
    y.initial_process(multi_font_feature)
    return y

def font_cache_process(y):
    font_list=[]
    font_list.append(y.DEFAULT_FONT)
    font_list=list(set(y.SECONDARY_FONT_LIST).union(set(font_list)))
    font_cache=[fonts_list for fonts_list in y.FONT_CACHE if fonts_list['name'] in font_list]
    return font_list,font_cache


class tag(pygame.sprite.Sprite):
    def __init__(self, tag, initial_position,fontname=):
    pygame.sprite.Sprite.__init__(self)





















if __name__=='__main__':
