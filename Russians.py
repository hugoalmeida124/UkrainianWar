import pygame
from Configs import *
from Bullet import Bullet
import random
import time
import math


class Russian:
    def __init__(self):
        self.__x = random.randint(1400, 1500)
        self.__y = 645
        self.__img = Img.RUSSIAN
        self.__deaths = 0
        self.__russians = []
        self.__speed = random.randint(1, 3)
        self.__total_frames = 0
        self.__walking = True
        self.__bullets = []
        self.__shooted_bullets = 0
        self.time_next_shot = 0

    def get_score(self):
        return self.__deaths

    def start_moving(self):  # quando ativada começa a andar
        self.__walking = True

    def move(self):
        for russian in self.__russians:
            if self.__walking:
                if self.__total_frames < 100:
                    self.__total_frames += 1
                    russian.__x -= self.__speed
                else:
                    self.__walking = False
                    self.__total_frames = 0

    def shoot(self):
        # fazer com que disparem um numero random de tiros entre 5 a 10 tiros e depois de dispararem,
        # passar o self.__walking para True
        for russian in self.__russians:
            if not self.__walking:  # se nao estiver a andar não avançar
                actual_time = time.time()  # função tempo
                if self.__shooted_bullets < 5:  # se forem disparadas menos de 5 balas continuar a disparar
                    if actual_time >= self.time_next_shot:
                        shoot_interval = random.uniform(0, 2)  # intervalo aleatorio
                        self.time_next_shot = actual_time + shoot_interval
                        self.__shooted_bullets += 1
                        bullet = Bullet(russian.__x - 5, russian.__y + 24, "left")
                        self.__bullets.append(bullet)
                        Sound.GUN_SHOT.play(loops=0)
                        Sound.GUN_SHOT.set_volume(0.30)
                        print(self.__shooted_bullets)
                else:  # se ja forem disparadas as 5 balas
                    self.__shooted_bullets = 0
                    self.__walking = True

    def is_out(self):  # feito bala a sair
        for bullet in self.__bullets:
            if bullet.x_position < 0 or bullet.x_position > Window.WIDTH:
                self.__bullets.remove(bullet)
                print(self.__bullets)

    def hits(self, ukrainian):  # bala colidir com o ukranian remove a bala da lista
        for bullet in self.__bullets:
            if bullet.colides_with(ukrainian):
                self.__bullets.remove(bullet)
                return True

    def generate_russian(self, lvl):
        if self.__russians:  # se o valor da lista for maior que 0 é porque tem e então nao retorna nada
            return True

        for x in range(lvl):
            russian = Russian()
            self.__russians.append(russian)

    def level_up(self):
        if self.__deaths == 5:
            return int(time.time()) % 5 == 0
        if self.__deaths == 10:
            return int(time.time()) % 5 == 0
        if self.__deaths == 20:
            return int(time.time()) % 5 == 0
        if self.__deaths == 30:
            return int(time.time()) % 5 == 0
        if self.__deaths == 40:
            return int(time.time()) % 5 == 0
        if self.__deaths == 50:
            return int(time.time()) % 5 == 0

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def draw_all(self, surface):
        for russian in self.__russians:
            russian.draw(surface)

        for bullet in self.__bullets:
            bullet.move()
            bullet.draw(surface)

    def get_overlaping_area(self, image, offset_x, offset_y):
        for russian in self.__russians:
            self_mask = pygame.mask.from_surface(russian.__img)
            who_mask = pygame.mask.from_surface(image)
            return who_mask.overlap_area(self_mask, [russian.__x - offset_x, russian.__y - offset_y])

        # Verificar colisão

    def colides_with(self, who):
        for russian in self.__russians:
            return who.get_overlaping_area(russian.__img, russian.__x, russian.__y) > 0

    def took_shot(self):
        for russian in self.__russians:  # verificar cada russo na lista se colide com a bala
            self.__russians.remove(russian)
            self.__deaths += 1

    def show_count(self, surface):
        text = Font.SECOND_FONT.render(F"Pontos: {self.__deaths}", True, [255, 255, 255], None)
        surface.blit(text, (10, 17))

    def reset(self):
        self.__deaths = 0
        self.__russians.clear()
        self.generate_russian(1)

    def limit_boundaries(self):
        if self.__x < 0:
            self.__x = 0
        elif self.__x > Window.WIDTH:
            self.__x = Window.WIDTH
