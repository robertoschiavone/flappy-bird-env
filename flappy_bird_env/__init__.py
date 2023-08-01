from .flappy_bird_env import FlappyBirdEnv

from gymnasium.envs.registration import register

__all__ = [FlappyBirdEnv]

register(id="FlappyBird-v0", entry_point="flappy_bird_env:FlappyBirdEnv")
