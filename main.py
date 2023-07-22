import pygame
from pygame.locals import *

import Buttons
from Configs import *
from Buttons import Button
from Ukrainians import Ukrainian
from Russians import Russian
from Bullet import Bullet
from Hearts import Lives

pygame.init()
screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()

Sound.AMBIENCE.play(loops=-1)
Sound.AMBIENCE.set_volume(0.10)

button_play = Button(600, 300, Buttons.BUTTON_GREEN)
button_exit = Button(605, 450, Buttons.BUTTON_RED)
button_restart = Button(650, 400, Buttons.BUTTON_BLUE)
ukrainian = Ukrainian(100, 645)
russians = Russian()
hearts = Lives()

view = "jogo"  # Tela de jogo

run = True
while run:
    dt = clock.tick(60)

    screen.blit(Img.BACKGROUND_MAIN, [0, 0])  # BACKGROUND

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
                    Sound.MENU_CLICK.play(loops=0)
                    Sound.MENU_CLICK.set_volume(0.30)

                    Sound.ROUND_ONE.play(loops=0)
                    Sound.ROUND_ONE.set_volume(0.70)
                elif button_exit.rect.collidepoint(mouse_pos):
                    # Código para mudar para sair do jogo quando o botão Exit for clicado
                    run = False
                    print("Botão Exit clicado!")
                    Sound.MENU_CLICK.play(loops=0)
                    Sound.MENU_CLICK.set_volume(0.30)
                    break
                elif button_restart.rect.collidepoint(mouse_pos):
                    # COLOCAR OS RESET
                    ukrainian.reset()
                    russians.reset()
                    hearts.reset()

                    Sound.MENU_CLICK.play(loops=0)
                    Sound.MENU_CLICK.set_volume(0.30)
                    view = "jogo"
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                ukrainian.shoot()

    if view == "inicial":
        button_play.draw(screen)
        button_exit.draw(screen)
        text = Font.MAIN_FONT.render(F"UKRAINIAN WAR", True, [255, 255, 255], None)
        screen.blit(text, (560, 100))

    elif view == "jogo":
        screen.blit(Img.BACKGROUND_GAME, [0, 0])  # BACKGROUND

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            ukrainian.move('left')
        elif key[pygame.K_RIGHT]:
            ukrainian.move('right')
        elif key[pygame.K_DOWN]:
            ukrainian.move('down')
        elif key[pygame.K_UP]:
            ukrainian.move('up')

        russians.generate_russian()
        # russians.start_moving()  # true começar a andar

        russians.move()
        russians.shoot()
        russians.draw_all(screen)

        russians.limit_boundaries()
        russians.is_out()
        russians.show_count(screen)

        ukrainian.limit_boundaries()
        ukrainian.draw(screen)
        ukrainian.is_out()

        hearts.draw(screen)

        if russians.hits(ukrainian):
            hearts.lose()
            Sound.HIT.play(loops=0)
            Sound.HIT.set_volume(0.10)

        if ukrainian.hits(russians):
            russians.took_shot()
            Sound.HIT_2.play(loops=0)
            Sound.HIT_2.set_volume(0.10)
            print("Colisao")

        if hearts.no_more():
            view = "gameover"
            Sound.GAME_OVER.play(loops=0)
            Sound.GAME_OVER.set_volume(0.10)

    elif view == "gameover":
        text = Font.MAIN_FONT.render(F"GAMEOVER", True, [255, 255, 255], None)
        screen.blit(text, (600, 200))
        button_restart.draw(screen)

    pygame.display.update()

pygame.quit()
