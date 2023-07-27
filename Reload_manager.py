from Reload import Reload
from Configs import *
import pygame
import random


class Reload_manager:
    def __init__(self):
        self.__bullets = []
        self.__score = 0
        self.new_bullets()

    def get_score(self):
        return self.__score

    def lose_score(self):
        self.__score -= 1

        if self.__score < 0:
            self.__score = 0

    def draw_all(self, surface):
        for bullet in self.__bullets:
            bullet.draw(surface)
            bullet.float()

    def feed(self, ukrainian):
        for bullet in self.__bullets:
            if bullet.colides_with(ukrainian):
                self.__bullets.remove(bullet)
                self.__score += 1

    def new_bullets(self):
        if self.__bullets:
            return

        for x in range(3):
            reload = Reload()
            self.__bullets.append(reload)

    def show_count(self, surface):
        text = Font.SECOND_FONT.render(F"Bullets:", True, [255, 255, 255], None)
        surface.blit(text, (10, 80))

        img = Img.BULLET_RECHARGE
        if self.__score == 3:
            surface.blit(img, (250, 60))
            surface.blit(img, (260, 60))
            surface.blit(img, (270, 60))
        elif self.__score == 2:
            surface.blit(img, (250, 60))
            surface.blit(img, (260, 60))
        elif self.__score == 1:
            surface.blit(img, (250, 60))

    def reset(self):
        self.__score = 0
