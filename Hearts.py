from Configs import *


class Lives:
    def __init__(self):
        self.__hearts = 3
        self.__img = Img.HEART

        if self.__hearts < 0:
            self.__hearts = 0

    @property
    def hearts(self):
        return self.__hearts

    def lose(self):
        self.__hearts -= 1

    def draw(self, surface):
        if self.__hearts >= 1:
            surface.blit(self.__img, [1500, 20]) #1

            if self.__hearts >= 2:
                surface.blit(self.__img, [1520, 20]) #2

                if self.__hearts == 3:
                    surface.blit(self.__img, [1540, 20]) #3

        #for x in range(self.__hearts):
            #surface.blit(self.__img, [450 + (20 * x), 20])

    def reset(self):
        self.__hearts = 3

    def no_more(self):
        return self.__hearts == 0
