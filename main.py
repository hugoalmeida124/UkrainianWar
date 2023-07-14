import pygame
from pygame.locals import *

import Buttons
from configs import *
from Buttons import Button

pygame.init()
screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()

Sound.AMBIENCE.play(loops=-1)
Sound.AMBIENCE.set_volume(0.10)

button_play = Button(100, 200, Buttons.BUTTON_GREEN)
button_exit = Button(300, 200, Buttons.BUTTON_RED)
button_restart = Button(380, 307, Buttons.BUTTON_GREEN)
view = "inicial"

run = True
while run:
    dt = clock.tick(60)
    screen.blit(Img.BACKGROUND, [0, 0])  # BACKGROUND

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                mouse_pos = pygame.mouse.get_pos()
                if button_play.rect.collidepoint(mouse_pos):
                    # Código para mudar para a tela de jogo quando o botão Play for clicado
                    print("Botão Play clicado!")
                    tela = "jogo"
                elif button_exit.rect.collidepoint(mouse_pos):
                    # Código para mudar para sair do jogo quando o botão Exit for clicado
                    run = False
                    print("Botão Exit clicado!")
                    break
                elif button_restart.rect.collidepoint(mouse_pos):
                    #COLOCAR OS RESET
                    tela = "jogo"

    if view == "inicial":
        button_play.draw(screen)
        button_exit.draw(screen)
        text = Font.MAIN_FONT.render(F"UKRAINIAN WAR", True, [255, 255, 255], None)
        screen.blit(text, (200, 100))
    elif view == "jogo":

    pygame.display.update()

pygame.quit()
