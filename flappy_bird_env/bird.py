import os

import pygame

from .drawable import Drawable
from .movable import Movable


class Bird(Drawable, Movable):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        upflap_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "images", "upflap.png")
        midflap_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "images", "midflap.png")
        downflap_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "images", "downflap.png")

        sprites = [upflap_path, midflap_path, downflap_path]

        raw_images = [pygame.image.load(sprite) for sprite in sprites]
        self.bird_images = [pygame.transform.scale2x(image)
                            for image in raw_images]

        self.images = self.bird_images
        self.max_rotation = 25
        self.rotation_velocity = 20
        self.animation_time = 5

        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y

        self.image_count = 0

        self.image = self.images[0]

    def jump(self) -> None:
        self.velocity = -10.5
        self.tick_count = 0
        self.height = self.y

    def draw(self, surface: pygame.Surface) -> None:
        self.image_count += 1

        if self.image_count < self.animation_time:
            self.image = self.images[0]
        elif self.image_count < self.animation_time * 2:
            self.image = self.images[1]
        elif self.image_count < self.animation_time * 3:
            self.image = self.images[2]
        elif self.image_count < self.animation_time * 4:
            self.image = self.images[1]
        elif self.image_count < self.animation_time * 4 + 1:
            self.image = self.images[0]
            self.image_count = 0

        if self.tilt <= -80:
            self.image = self.images[1]
            self.image_count = self.animation_time * 2

        rotated_image = pygame.transform.rotate(self.image, self.tilt)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center)
        surface.blit(rotated_image, new_rect.topleft)

    def move(self) -> None:
        self.tick_count += 1
        displacement = self.velocity * self.tick_count + 1.5 * \
                       self.tick_count ** 2

        if displacement > 16:
            displacement = (displacement / abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y += displacement

        if displacement < 0:
            self.tilt = max(self.tilt, self.max_rotation)
        elif self.tilt > -90:
            self.tilt -= self.rotation_velocity

    def get_mask(self) -> pygame.Mask:
        return pygame.mask.from_surface(self.image)
