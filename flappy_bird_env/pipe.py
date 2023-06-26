import os

import numpy as np
import pygame

from .bird import Bird
from .drawable import Drawable
from .movable import Movable


class Pipe(Drawable, Movable):
    def __init__(self, x: int, rng: np.random.Generator):
        self.x = x
        self.rng = rng

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            "images", "pipe.png")
        raw_image = pygame.image.load(path)
        self.pipe_image = pygame.transform.scale2x(raw_image)
        self.gap = 200
        self.velocity = 5

        self.height = 0
        self.top = 0
        self.bottom = 0

        self.pipe_top = pygame.transform.flip(self.pipe_image, False, True)
        self.pipe_bottom = self.pipe_image

        self.passed = False
        self.set_height()

    def set_height(self) -> None:
        self.height = self.rng.integers(low=50, high=450)
        self.top = self.height - self.pipe_top.get_height()
        self.bottom = self.height + self.gap

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.pipe_top, (self.x, self.top))
        surface.blit(self.pipe_bottom, (self.x, self.bottom))

    def move(self) -> None:
        self.x -= self.velocity

    def collide(self, bird: Bird) -> bool:
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.pipe_top)
        bottom_mask = pygame.mask.from_surface(self.pipe_bottom)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        top_collision = bird_mask.overlap(top_mask, top_offset)
        bottom_collision = bird_mask.overlap(bottom_mask, bottom_offset)

        return bool(top_collision or bottom_collision)
