import pygame
from pygame.locals import *

import Buttons
from Configs import *
from Buttons import Button
from Ukrainians import Ukrainian
from Russians import Russian

pygame.init()
screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()

Sound.AMBIENCE.play(loops=-1)
Sound.AMBIENCE.set_volume(0.10)

button_play = Button(100, 200, Buttons.BUTTON_GREEN)
button_exit = Button(300, 200, Buttons.BUTTON_RED)
button_restart = Button(380, 307, Buttons.BUTTON_GREEN)
ukrainian = Ukrainian(100, 645)
russians = Russian()

view = "inicial"  # Tela de jogo

run = True
while run:
    dt = clock.tick(60)
    screen.blit(Img.BACKGROUND, [0, 0])  # BACKGROUND

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Botã
                # o esquerdo do mouse
                mouse_pos = pygame.mouse.get_pos()
                if button_play.rect.collidepoint(mouse_pos):
                    # Código para mudar para a tela de jogo quando o botão Play for clicado
                    print("Botão Play clicado!")
                    view = "jogo"
                elif button_exit.rect.collidepoint(mouse_pos):
                    # Código para mudar para sair do jogo quando o botão Exit for clicado
                    run = False
                    print("Botão Exit clicado!")
                    break
                elif button_restart.rect.collidepoint(mouse_pos):
                    # COLOCAR OS RESET
                    view = "jogo"
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                ukrainian.shoot(screen)

    if view == "inicial":
        button_play.draw(screen)
        button_exit.draw(screen)
        text = Font.MAIN_FONT.render(F"UKRAINIAN WAR", True, [255, 255, 255], None)
        screen.blit(text, (200, 100))
    elif view == "jogo":

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            ukrainian.move('left')
        elif key[pygame.K_RIGHT]:
            ukrainian.move('right')
        elif key[pygame.K_DOWN]:
            ukrainian.move('down')

        russians.generate_russian()
        russians.draw_all(screen)
        russians.move()

        ukrainian.draw(screen)

        if ukrainian.hits(russians):
            russians.took_shot(russians)

        ukrainian.is_out()
        russians.show_count(screen)

    pygame.display.update()

pygame.quit()
