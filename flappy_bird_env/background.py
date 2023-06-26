import os

import pygame

from .drawable import Drawable


class Background(Drawable):
    def __init__(self):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            "images", "background.png")
        raw_image = pygame.image.load(path)
        self.background_image = pygame.transform.scale2x(raw_image)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.background_image, (0, 0))
