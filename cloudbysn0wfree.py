
#input txt
from PIL import Image



class inputsingletext:
    #text=''
    #color = 0
    #highlight = False
    #textorientation='L2R'
    #language='English'
    kind='text'
    def __init__(self,txt,c,o,lang,h=False):
        self.text = txt
        self.color = c
        self.highlight= h
        self.textorientation= o
        self.language=lang

class shapepicture:
    #picture=''
    #greyscale='grey'
    #size=0
    def __init__(self,img,g,s):
        self.picture=img
        self.greyscale=g
        self.size=s
    def shapeprocess(self):
        if self.greyscale !='grey':
            if self.picture.mode not in ('1','L','RGB','CMYK'):
                raise Exception('That is not a recogized image mode')
            elif self.picture.mode == 'L':
                self.greyscale ='grey'
                pass
            else:
                self.picture=self.picture.convert('L')
                self.greyscale ='grey'
                pass
        else:
            pass
        return self


class picture_scan_bound:
    def __init__(self,txt, c,o,lang,h=False):
        self.text = txt
        self.color = c
        self.highlight= h
        self.textorientation= o
        self.language=lang
