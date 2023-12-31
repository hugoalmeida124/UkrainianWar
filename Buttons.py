import pygame
from Configs import *

BUTTON_RED = pygame.image.load("imgs/red_button.png")
BUTTON_HOME = pygame.image.load("imgs/green_button.png")
BUTTON_ABOUT = pygame.image.load("imgs/green_button.png")
BUTTON_BLUE = pygame.image.load("imgs/blue_button.png")
BUTTON_GREEN = pygame.image.load("imgs/green_button.png")


class Button:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.img = image
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    @property
    def actual_img(self):
        return self.img

    @actual_img.setter
    def actual_img(self, value):
        if value.lower == "blue":
            self.img = BUTTON_BLUE

    def draw(self, janela):
        janela.blit(self.img, (self.x, self.y))
        if self.img == BUTTON_GREEN:
            text = Font.MAIN_FONT.render(F"PLAY", True, [255, 255, 255], None)
            janela.blit(text, (715, 310))
        elif self.img == BUTTON_ABOUT:
            text = Font.MAIN_FONT.render(F"ABOUT", True, [255, 255, 255], None)
            janela.blit(text, (685, 460))
        elif self.img == BUTTON_RED:
            text = Font.MAIN_FONT.render(F"EXIT", True, [255, 255, 255], None)
            janela.blit(text, (728, 600))
        elif self.img == BUTTON_BLUE:
            text = Font.MAIN_FONT.render(F"RESTART", True, [255, 255, 255], None)
            janela.blit(text, (680, 410))
        elif self.img == BUTTON_HOME:
            text = Font.MAIN_FONT.render(F"HOME", True, [255, 255, 255], None)
            janela.blit(text, (1300, 610))

    def collide(self, pos):
        return self.rect.collidepoint(pos)
