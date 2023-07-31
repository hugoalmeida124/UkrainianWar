import pygame
from pygame.locals import *
from Configs import *


def pause(screen):
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    paused = False

    text = Font.MAIN_FONT.render(F"Game is PAUSED", True, [255, 255, 255], None)
    screen.blit(text, (560, 100))

    pygame.display.update()
