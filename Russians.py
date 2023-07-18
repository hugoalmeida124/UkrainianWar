import pygame
from Configs import *
from Bullet import Bullet
import random


class Russian:
    def __init__(self):
        self.__x = random.randint(1400, 1600)
        self.__y = 645
        self.__img = Img.RUSSIAN
        self.__deaths = 0
        self.__russians = []
        self.__speed = random.randint(1, 3)
        self.__total_frames = 0
        self.__walking = False

    @property
    def get_score(self):
        return self.__deaths

    def start_moving(self):  # quando ativada começa a andar
        self.__walking = True

    def move(self):
        for russian in self.__russians:
            if self.__walking:
                if self.__total_frames < 20:
                    self.__total_frames += 1
                    russian.__x -= self.__speed
                else:
                    # self.shoot()
                    self.frames_andados = 0
                    self.__walking = False

    def generate_russian(self):
        if self.__russians:  # se o valor da lista for maior que 0 é porque tem e então nao retorna nada
            return True

        for x in range(3):
            russian = Russian()
            self.__russians.append(russian)

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def draw_all(self, surface):
        for russian in self.__russians:
            russian.draw(surface)

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

        # Verificar colisão

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def took_shot(self, bullet):
        for russian in self.__russians:  # verificar cada russo na lista se colide com a bala
            if russian.colides_with(bullet):
                self.__russians.remove(russian)
                self.__deaths += 1
                print(self.__russians)

    def show_count(self, surface):
        text = Font.MAIN_FONT.render(F"Pontos: {self.__deaths}", True, [255, 255, 255], None)
        surface.blit(text, (10, 17))

    def reset(self):
        self.__deaths = 0
