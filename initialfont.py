# -*- coding: utf-8 -*-

import os,simplejson,copy



class initial_font:
    SECONDARY_FONT_LIST=[]
    FONT_NAME_LIST=[]
    DEFAULT_FONT = 'Droid Sans'
    DEFAULT_PALETTE = 'default'
    FONT_CACHE=''
    FONT_DIR=''

    def __ini__(self):
        self.DEFAULT_FONT = DEFAULT_FONT
        self.DEFAULT_PALETTE = DEFAULT_PALETTE
        self.FONT_CACHE=FONT_CACHE
        self.FONT_DIR=FONT_DIR
        self.FONT_NAME_LIST=FONT_NAME_LIST
        self.SECONDARY_FONT_LIST=SECONDARY_FONT_LIST

    def load_font_dir(self,fonts='fonts.json', fonts_dir='fonts'):
        self.FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),fonts_dir)
        if os.path.isdir(self.FONT_DIR):
            self.FONT_CACHE = simplejson.load(open(os.path.join(self.FONT_DIR, fonts), 'r'))
        else:
            raise Exception('Font folder can not be revealed in the current folder')

    def print_list(self,font_name,font_list = True ,all_list= False):
        (rows,columns)=os.popen('stty size', 'r').read().split()
        if font_list == True or font_list == 1:
            d=1
            print '*'*int(columns)
            for f in font_name:
                if f != self.DEFAULT_FONT:
                    print '%d) %s '%(d,f)
                elif f == self.DEFAULT_FONT:
                    print '%d) %s   <--'%(d,f)
                d+=1
            print '*'*int(columns)
        #return (rows,columns)
        if all_list == True or all_list == 1:
            print '*'*int(columns)
            print 'FONT LIST include :\n  %s  <--DEFAULT_FONT' %self.DEFAULT_FONT
            for s in self.SECONDARY_FONT_LIST:
                print '  %s'%s
            print '*'*int(columns)

    def change_font(self):
        self.load_font_dir()
        print ('If you want to look the list of fonts please type: list')
        font_from_input = raw_input('''please enter the specific font as the DEFAULT_FONT,if would not change the default setting please type False or No:''')
        font_name=[fonts_list['name'] for fonts_list in self.FONT_CACHE ]
        self.FONT_NAME_LIST = copy.copy(font_name)
        while 1:
            if font_from_input in ['False' ,'No','no','false','NO','FASLE'] :
                return 0
            elif font_from_input == 'list':

                self.print_list(font_name)
                #d=1
                #print '*'*int(columns)
                #for f in font_name:
                #    if f != self.DEFAULT_FONT:
                #        print '%d) %s '%(d,f)
                #    elif f == self.DEFAULT_FONT:
                #        print '%d) %s   <--'%(d,f)
                #    d+=1
                #print '*'*int(columns)
            elif font_from_input in font_name:
                self.DEFAULT_FONT=font_from_input
                self.DEFAULT_PALETTE = 'changed'
                return 0
            print ('Unrecogised Font(s) or Wrong Input detected, please choose another Font Name or re-type the Font Name!')
            print ('If you want to look the list of fonts please type: list')
            font_from_input = raw_input('(Primary) Font Name (DEFAULT_FONT: %s): '%self.DEFAULT_FONT)


    def initial_process(self,multi_font_feature = False):
        self.change_font()
        if multi_font_feature == False or multi_font_feature == 0:
            pass
        else:
            multi_fonts_name_list=[]
            self.DEFAULT_PALETTE = 'multi_font'
            multi_fonts=raw_input('Secondary Font Name (≠ %s, divided by ","): '%self.DEFAULT_FONT)
            (rows,columns)=os.popen('stty size', 'r').read().split()

            font_name=[fonts_list['name'] for fonts_list in self.FONT_CACHE ]
            while 1:
                if multi_fonts == 'list':# print out the list of Fonts

                    self.print_list(font_name)

                elif multi_fonts != 'list':
                    font_list4multi_recognised=[]
                    font_list4multi_unrecognised=[]
                    if ',' in multi_fonts:
                        multi_fonts_name_list=multi_fonts.split(',')
                        for multi_fonts_name in multi_fonts_name_list:
                            if multi_fonts_name in self.FONT_NAME_LIST:
                                font_list4multi_recognised.append(multi_fonts_name)
                            else:
                                font_list4multi_unrecognised.append(multi_fonts_name)
                    else:
                        multi_fonts_name=multi_fonts
                        if multi_fonts_name in self.FONT_NAME_LIST:
                            font_list4multi_recognised.append(multi_fonts_name)
                        else:
                            font_list4multi_unrecognised.append(multi_fonts_name)
                    self.SECONDARY_FONT_LIST=list(set(self.SECONDARY_FONT_LIST).union(set(font_list4multi_recognised)))
                    lenfont_list4multi_unrecognised=len(font_list4multi_unrecognised)
                    if lenfont_list4multi_unrecognised == 0:
                        return 0
                    else:
                        print '*'*int(columns)
                        if lenfont_list4multi_unrecognised > 1:
                            print 'Unrecognised Fonts: '
                            for unrecognised_font in font_list4multi_unrecognised:
                                if unrecognised_font == 'list':
                                    pass
                                else:
                                    print unrecognised_font
                        elif lenfont_list4multi_unrecognised == 1:
                            unrecognised_font=font_list4multi_unrecognised
                            if unrecognised_font == 'list':
                                pass
                            else:
                                print 'Unrecognised Font: '
                                print unrecognised_font

                        else:
                            raise Exception('The unknown length of Unrecognised Font(s) list')
                        print '*'*int(columns)
                print ('If you want to look the list of fonts please type: list')
                multi_fonts= raw_input('please re-type the Secondary Font Name (divided by ","): ')


if __name__=='__main__':

    y=initial_font()
    y.initial_process(multi_font_feature = True)
    #fontss_name=[fonts_list['ttf'] for fonts_list in y.FONT_CACHE ]

    #print y.FONT_CACHE
    font_name=[fonts_list['name'] for fonts_list in y.FONT_CACHE ]
    y.print_list(font_name,font_list=False ,all_list=True)
