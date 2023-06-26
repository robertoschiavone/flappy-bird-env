import gymnasium as gym
import numpy as np
import pygame

import flappy_bird_env  # noqa

from gymnasium.utils.play import play

env = gym.make("FlappyBird-v0", render_mode="rgb_array")
play(env, keys_to_action={(pygame.K_SPACE,): np.array([1])}, noop=np.array([0]),
     fps=24)
