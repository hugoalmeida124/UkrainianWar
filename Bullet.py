from Configs import *


class Bullet:
    def __init__(self, x, y, location):
        self.__x = x
        self.__y = y
        self.__location = location
        if location == 'right':
            self.__img = Img.BULLET_RIGHT
        else:
            self.__img = Img.BULLET_LEFT

    @property
    def x_position(self):
        return self.__x

    @x_position.setter
    def x_position(self, value):
        self.__x = value

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move(self):
        if self.__location == 'right':
            self.__x += 20
        else:
            self.__x -= 20

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

        # Verificar colisão

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0