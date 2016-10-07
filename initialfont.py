import os,simplejson



class initial_font:

    DEFAULT_FONT = 'Droid Sans'
    DEFAULT_PALETTE = 'default'
    def __ini__(self):
        self.DEFAULT_FONT = DEFAULT_FONT
        self.DEFAULT_PALETTE = DEFAULT_PALETTE
        self.FONT_CACHE=''
        self.FONT_DIR=''

    def load_font_dir(self,fonts='fonts.json', fonts_dir='fonts'):
        self.FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),fonts_dir)
        if os.path.isdir(self.FONT_DIR):
            self.FONT_CACHE = simplejson.load(open(os.path.join(self.FONT_DIR, fonts), 'r'))

        else:
            raise Exception('Font folder can not be revealed in the current folder')



    def change_font(self):
        font_from_input = raw_input('''please enter the specific font as the DEFAULT_FONT,if would not change the default setting please type in False:''')
        if font_from_input =='False':
            print 'pass'
            pass

        else:
            self.load_font_dir()
            if font_from_input in self.FONT_CACHE:
                self.DEFAULT_FONT=font_from_input
                self.DEFAULT_PALETTE = 'changed'
            else:
                while 1:
                    print ('if want to look the list of font please type: list')
                    font= raw_input('unrecogised font, please choose another font and re-type font name:')
                    if font == 'list':
                        font_name=[fonts_list['name'] for fonts_list in self.FONT_CACHE ]

                            #font_name.append()
                        print font_name
                    elif font in  self.FONT_CACHE:
                        break



    def preprocess (self):

        self.change_font()
        return self


if __name__=='__main__':
    y=initial_font()
    print y.preprocess().FONT_CACHE
