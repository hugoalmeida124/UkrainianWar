import pygame
from pygame.locals import *

import Buttons
import time
from Configs import *
from Buttons import Button
from Ukrainians import Ukrainian
from Russians import Russian
from Bullet import Bullet
from Reload_manager import Reload_manager

pygame.init()
screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()

Sound.AMBIENCE.play(loops=-1)
Sound.AMBIENCE.set_volume(0.10)

button_play = Button(600, 300, Buttons.BUTTON_GREEN)
button_exit = Button(605, 450, Buttons.BUTTON_RED)
button_restart = Button(520, 400, Buttons.BUTTON_BLUE)
button_home = Button(1210, 600, Buttons.BUTTON_HOME)
ukrainian = Ukrainian(100, 645)
ukrainian_shoot = False
lvl_up = False
russians = Russian()
reload = Reload_manager()

view = 1  # Tela de jogo

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
                    view = 2
                    Sound.MENU_CLICK.play(loops=0)
                    Sound.MENU_CLICK.set_volume(0.30)

                    Sound.ROUND_ONE.play(loops=0)
                    Sound.ROUND_ONE.set_volume(0.70)
                if button_exit.rect.collidepoint(mouse_pos):
                    # Código para mudar para sair do jogo quando o botão Exit for clicado
                    run = False
                    print("Botão Exit clicado!")
                    Sound.MENU_CLICK.play(loops=0)
                    Sound.MENU_CLICK.set_volume(0.30)
                    break
                if button_restart.rect.collidepoint(mouse_pos):
                    # COLOCAR OS RESET
                    print("restart cliclado")
                    ukrainian.reset()
                    russians.reset()
                    reload.reset()

                    Sound.MENU_CLICK.play(loops=0)
                    Sound.MENU_CLICK.set_volume(0.30)
                    view = 2
                if button_home.rect.collidepoint(mouse_pos):
                    view = 1
                    ukrainian.reset()
                    russians.reset()
                    reload.reset()

        elif event.type == KEYDOWN:
            score = reload.get_score()
            if event.key == K_SPACE and score > 0:
                ukrainian.shoot()

                direction = ukrainian.direction()  # verificar a posição para não cliclar no espaço e gastar as balas sem as usar
                if direction == "right" or direction == "up":
                    reload.lose_score()

    if view == 1:
        button_play.draw(screen)
        button_exit.draw(screen)
        text = Font.MAIN_FONT.render(F"UKRAINIAN WAR", True, [255, 255, 255], None)
        screen.blit(text, (560, 100))

    elif view == 2:
        screen.blit(Img.BACKGROUND_GAME_1, [0, 0])  # BACKGROUND

        hearts = ukrainian.hearts
        deaths = russians.get_score()
        if deaths < 5:  # lvl1
            text = Font.MAIN_FONT.render(F"Level 1", True, [255, 255, 255], None)
            screen.blit(text, (650, 50))
            russians.generate_russian(1)

        elif deaths < 10:  # lvl2
            #screen.blit(Img.BACKGROUND_GAME_2, [0, 0])  # BACKGROUND lvl2
            text = Font.MAIN_FONT.render(F"LEVEL 2", True, [255, 255, 255], None)
            screen.blit(text, (650, 50))
            russians.generate_russian(2)
            if deaths == 9:
                lvl_up = False #reiniciar a variavel que controla o som de lvl up

        elif deaths < 20:  # lvl3
            #screen.blit(Img.BACKGROUND_GAME_3, [0, 0])  # BACKGROUND lvl3
            text = Font.MAIN_FONT.render(F"LEVEL 3", True, [255, 255, 255], None)
            screen.blit(text, (650, 50))
            russians.generate_russian(3)
            if hearts == 15:
                if hearts < 3:
                    ukrainian.get_hearts()

            if deaths == 19:
                lvl_up = False

        elif deaths < 30:  # lvl4
            #screen.blit(Img.BACKGROUND_GAME_4, [0, 0])  # BACKGROUND lvl4
            text = Font.MAIN_FONT.render(F"LEVEL 4", True, [255, 255, 255], None)
            screen.blit(text, (650, 50))
            russians.generate_russian(4)

            if hearts == 25:
                if hearts < 3:
                    ukrainian.get_hearts()

            if deaths == 29:
                lvl_up = False

        elif deaths < 50:  # lvl5
            text = Font.MAIN_FONT.render(F"LEVEL 4", True, [255, 255, 255], None)
            screen.blit(text, (650, 50))
            russians.generate_russian(5)

            if hearts == 40:
                if hearts < 3:
                    ukrainian.get_hearts()

        if deaths == 50:
            Sound.WIN.play()
            Sound.LVL_UP.set_volume(0.20)
            view = 4  # view de vencedor

        if not lvl_up and russians.level_up():  # tocar som de lvlup
            Sound.LVL_UP.play(maxtime=3000)
            Sound.LVL_UP.set_volume(0.20)
            lvl_up = True

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            ukrainian.move('left')
        elif key[pygame.K_RIGHT]:
            ukrainian.move('right')
        elif key[pygame.K_DOWN]:
            ukrainian.move('down')
        elif key[pygame.K_UP]:
            ukrainian.move('up')

        # russians
        russians.move()
        russians.shoot()
        russians.draw_all(screen)
        russians.limit_boundaries()
        russians.is_out()
        russians.show_count(screen)

        # ukrainians
        ukrainian.limit_boundaries()
        ukrainian.draw(screen)
        ukrainian.is_out()

        # reload_manager
        reload.draw_all(screen)
        reload.feed(ukrainian)
        reload.show_count(screen)

        score = reload.get_score()
        if score == 0:  # reload nas balas apos disparar as 3
            reload.new_bullets()

        if russians.hits(ukrainian):
            ukrainian.lose_hearts()
            Sound.HIT.play(loops=0)
            Sound.HIT.set_volume(0.10)

        if ukrainian.hits(russians):
            russians.took_shot()
            Sound.HIT_2.play(loops=0)
            Sound.HIT_2.set_volume(0.10)

        if ukrainian.no_more_hearts():
            view = 3
            Sound.GAME_OVER.play(loops=0)
            Sound.GAME_OVER.set_volume(0.10)

        pygame.display.update()

    elif view == 3:
        text = Font.MAIN_FONT.render(F"GAMEOVER", True, [255, 255, 255], None)
        screen.blit(text, (640, 200))
        text2 = Font.SECOND_FONT.render(F"HIGHEST SCORE: {russians.get_score()}", True, [255, 255, 255], None)
        screen.blit(text2, (700, 350))
        button_restart.draw(screen)

    elif view == 4:
        text = Font.MAIN_FONT.render(F"WINNER!", True, [255, 255, 255], None)
        screen.blit(text, (680, 200))
        text2 = Font.SECOND_FONT.render(F"Slava Ukraini!", True, [255, 255, 255], None)
        screen.blit(text2, (710, 350))
        button_home.draw(screen)


    pygame.display.update()

pygame.quit()
