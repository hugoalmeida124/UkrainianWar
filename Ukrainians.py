import pygame
from Configs import *
from Bullet import Bullet


class Ukrainian:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__initial_y = y
        self.__speed = 5
        self.__img = Img.UKRAINIAN_RIGHT
        self.__bullets = []
        self.__direction = 'right'

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
        print(self.__direction)
        if self.__direction == 'right' or self.__direction == 'up':
            bullet = Bullet(self.__x + 118, self.__y + 24, "right")
            self.__bullets.append(bullet)
            Sound.GUN_SHOT.play(loops=0)
            Sound.GUN_SHOT.set_volume(0.30)

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

        for bullet in self.__bullets:
            bullet.move()
            bullet.draw(surface)

    def reset(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = Img.UKRAINIAN_RIGHT

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
