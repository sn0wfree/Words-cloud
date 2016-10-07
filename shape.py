
#input txt
from PIL import Image
import cv2.cv as cv




class initial_picture_para:
    def __init__(self):
        self.TAG_PADDING=5
        self.TAG_CLOUD_PADDING=5 # Margins added to the whole image
        self.STEP_SIZE = 2 # relative to base step size of each spiral function
        self.RADIUS = 1
        self.ECCENTRICITY = 1.5
        self.LOWER_START = 0.45
        self.UPPER_START = 0.55


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
    def __init__(self,img):
        self.picture=img
        self.greyscale=''
        self.size=img.size
    def image_reco_process(self,returnable=False):
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
        if returnable:
            return self






class picture_scan_bound:
    def __init__(self,txt, c,o,lang,h=False):
        self.text = txt
        self.color = c
        self.highlight= h
        self.textorientation= o
        self.language=lang



if __name__=='__main__':
    pass
