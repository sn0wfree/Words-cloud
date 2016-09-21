
#input txt
from PIL import Image



class inputsingletext:
    text=''
    color = 0
    highlight = False
    textorientation='L2R'
    language='English'

    def __init__(self,txt,c,o,lang,h=False):
        self.text = txt
        self.color = c
        self.highlight= h
        self.textorientation= o
        self.language=lang

class shapepicture:
    picture=''
    greyscale='grey'
    size=0

    def __init__(self,img,g,s):
        self.picture=img
        self.greyscale=g
        self.size=s
