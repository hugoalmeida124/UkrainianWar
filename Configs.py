import pygame

pygame.init()


class Window:
    WIDTH = 1600
    HEIGHT = 800
    TITLE = "UkrainianWar"
    ICON = pygame.image.load("imgs/duck_soldier.png")


pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))


class Img:
    BACKGROUND_GAME_1 = pygame.image.load("imgs/background.png").convert()
    BACKGROUND_GAME_2 = pygame.image.load("imgs/background2.png").convert()
    BACKGROUND_GAME_3 = pygame.image.load("imgs/background4.png").convert()
    BACKGROUND_GAME_4 = pygame.image.load("imgs/background3.png").convert()
    BACKGROUND_MAIN = pygame.image.load("imgs/background_main.png").convert()
    UKRAINIAN_RIGHT = pygame.image.load("imgs/up_soldier.png").convert_alpha()
    UKRAINIAN_LEFT = pygame.image.load("imgs/up_soldier-left.png").convert_alpha()
    UKRAINIAN_DOWN = pygame.image.load("imgs/duck_soldier.png").convert_alpha()
    RUSSIAN = pygame.image.load("imgs/russian.png").convert_alpha()
    HEART = pygame.image.load("imgs/heart.png").convert_alpha()
    BULLET_RECHARGE = pygame.image.load("imgs/bullet2.png").convert_alpha()
    BULLET_RIGHT = pygame.image.load("imgs/bullet.png").convert_alpha()
    BULLET_LEFT = pygame.transform.flip(BULLET_RIGHT, True, False).convert_alpha()


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
    WIN = pygame.mixer.Sound("sounds/Winner.mp3")


class Font:
    MAIN_FONT = pygame.font.Font("fonts/Capture.ttf", 70)
    SECOND_FONT = pygame.font.Font("fonts/Capture.ttf", 30)
    TEXT_FONT = pygame.font.Font("fonts/Capture.ttf", 20)
