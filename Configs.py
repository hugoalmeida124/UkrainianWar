import pygame

pygame.init()


class Window:
    WIDTH = 1600
    HEIGHT = 800
    TITLE = "UkrainianWar"
    ICON = pygame.image.load("imgs/duck_soldier.png")


class Img:
    BACKGROUND = pygame.image.load("imgs/background.png")
    UKRAINIAN_RIGHT = pygame.image.load("imgs/up_soldier.png")
    UKRAINIAN_LEFT = pygame.image.load("imgs/up_soldier-left.png")
    UKRAINIAN_DOWN = pygame.image.load("imgs/duck_soldier.png")
    RUSSIAN = pygame.image.load("imgs/russian.png")
    HEART = pygame.image.load("imgs/heart.png")
    BULLET_RIGHT = pygame.image.load("imgs/bullet.png")
    BULLET_LEFT = pygame.transform.flip(BULLET_RIGHT, True, False)


class Sound:
    AMBIENCE = pygame.mixer.Sound("sounds/background_sound.wav")
    GUN_SHOT = pygame.mixer.Sound("sounds/gun_shoot.ogg")
    GAME_OVER = pygame.mixer.Sound("sounds/game_over.wav")


class Font:
    MAIN_FONT = pygame.font.Font("fonts/2d_font.otf")
