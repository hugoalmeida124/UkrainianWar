import pygame
from Configs import *
from Bullet import Bullet
import time
from Reload_manager import Reload_manager


class Ukrainian:
    def __init__(self, x, y):
        self.__x = x
        self.__initial_x = x
        self.__y = y
        self.__initial_y = y
        self.__speed = 5
        self.__img = Img.UKRAINIAN_RIGHT
        self.__bullets = []
        #total_ammunition = 3
        self.__direction = 'right'
        self.__hearts = 3

    def direction(self):
        return self.__direction

    def move(self, direction):
        self.__direction = direction

        if self.__direction == 'right':
            self.__y = self.__initial_y
            self.__x += self.__speed
            self.__img = Img.UKRAINIAN_RIGHT
        elif direction == 'left':
            self.__y = self.__initial_y
            self.__x -= self.__speed
            self.__img = Img.UKRAINIAN_LEFT
        elif direction == 'down':
            self.__y = 690
            self.__img = Img.UKRAINIAN_DOWN
        elif direction == 'up':
            self.__y = self.__initial_y
            self.__img = Img.UKRAINIAN_RIGHT

    def shoot(self):
        if self.__direction == 'right' or self.__direction == 'up':
            bullet = Bullet(self.__x + 118, self.__y + 24, "right")
            self.__bullets.append(bullet)
            Sound.GUN_SHOT.play(loops=0)
            Sound.GUN_SHOT.set_volume(0.30)

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

        if self.__hearts >= 1:
            surface.blit(Img.HEART, [1500, 20])  # 1
            if self.__hearts >= 2:
                surface.blit(Img.HEART, [1520, 20])  # 2
                if self.__hearts == 3:
                    surface.blit(Img.HEART, [1540, 20])  # 3

        for bullet in self.__bullets:
            bullet.move()
            bullet.draw(surface)

    def reset(self):
        self.__x = self.__initial_x
        self.__y = self.__initial_y
        self.__img = Img.UKRAINIAN_RIGHT
        self.__hearts = 3
        self.__bullets.clear()

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

        # Verificar colisão

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def is_out(self):  # feito bala a sair
        for bullet in self.__bullets:
            if bullet.x_position < 0 or bullet.x_position > Window.WIDTH:
                self.__bullets.remove(bullet)
                print(self.__bullets)

    def hits(self, russian):
        for bullet in self.__bullets:
            if bullet.colides_with(russian):
                self.__bullets.remove(bullet)
                return True

    def limit_boundaries(self):
        if self.__x < 0:
            self.__x = 0

        if self.__x > Window.WIDTH:
            self.__x = Window.WIDTH

    # hearts
    @property
    def hearts(self):
        return self.__hearts

    def get_hearts(self):
        self.__hearts += 1

    def lose_hearts(self):
        self.__hearts -= 1

    def lose_all_hearts(self):
        self.__hearts = 0

    def no_more_hearts(self):
        return self.__hearts == 0


