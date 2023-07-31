from Configs import *
import pygame
import random


class Reload:
    def __init__(self):
        self.__x = 0
        self.__y = 720
        self.__img = Img.BULLET_RECHARGE
        self.__is_up = True
        self.random_position()

    def random_position(self):
        self.__x = random.randint(250, 1000)

    def float(self):
        if self.__is_up:
            self.__y -= 2
            if self.__y == 700:
                self.__is_up = False
        else:
            self.__y += 2
            if self.__y == 740:
                self.__is_up = True

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

        # Verificar colisão

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0
