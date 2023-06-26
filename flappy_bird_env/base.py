import os

import pygame

from .drawable import Drawable
from .movable import Movable


class Base(Drawable, Movable):
    def __init__(self, y: int):
        self.y = y

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            "images", "base.png")
        raw_image = pygame.image.load(path)
        self.base_image = pygame.transform.scale2x(raw_image)

        self.velocity = 5
        self.width = self.base_image.get_width()
        self.image = self.base_image

        self.x1 = 0
        self.x2 = self.width

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.x1, self.y))
        surface.blit(self.image, (self.x2, self.y))

    def move(self) -> None:
        self.x1 -= self.velocity
        self.x2 -= self.velocity

        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width
