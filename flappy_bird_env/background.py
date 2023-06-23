import os

import pygame

from .drawable import Drawable


class Background(Drawable):
    def __init__(self):
        raw_image = pygame.image.load(os.path.join("images", "background.png"))
        self.background_image = pygame.transform.scale2x(raw_image)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.background_image, (0, 0))
