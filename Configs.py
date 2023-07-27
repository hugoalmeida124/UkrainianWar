import pygame

pygame.init()


class Window:
    WIDTH = 1600
    HEIGHT = 800
    TITLE = "UkrainianWar"
    ICON = pygame.image.load("imgs/duck_soldier.png")


class Img:
    BACKGROUND_GAME = pygame.image.load("imgs/background.png")
    BACKGROUND_MAIN = pygame.image.load("imgs/background_main.png")
    UKRAINIAN_RIGHT = pygame.image.load("imgs/up_soldier.png")
    UKRAINIAN_LEFT = pygame.image.load("imgs/up_soldier-left.png")
    UKRAINIAN_DOWN = pygame.image.load("imgs/duck_soldier.png")
    RUSSIAN = pygame.image.load("imgs/russian.png")
    HEART = pygame.image.load("imgs/heart.png")
    BULLET_RECHARGE = pygame.image.load("imgs/bullet2.png")
    BULLET_RIGHT = pygame.image.load("imgs/bullet.png")
    BULLET_LEFT = pygame.transform.flip(BULLET_RIGHT, True, False)


class Sound:
    AMBIENCE = pygame.mixer.Sound("sounds/background_sound.mp3")
    GUN_SHOT = pygame.mixer.Sound("sounds/gun_shoot.ogg")
    GAME_OVER = pygame.mixer.Sound("sounds/game_over.wav")
    ROUND_ONE = pygame.mixer.Sound("sounds/round1.mp3")
    HIT = pygame.mixer.Sound("sounds/hit.flac")
    HIT_2 = pygame.mixer.Sound("sounds/hit2.mp3.flac")
    MENU_CLICK = pygame.mixer.Sound("sounds/menu_click.wav")
    LVL_UP = pygame.mixer.Sound("sounds/LVL_UP.mp3")
    RELOAD = pygame.mixer.Sound("sounds/RELOAD.ogg")


class Font:
    MAIN_FONT = pygame.font.Font("fonts/Capture.ttf", 70)
    SECOND_FONT = pygame.font.Font("fonts/Capture.ttf", 30)
