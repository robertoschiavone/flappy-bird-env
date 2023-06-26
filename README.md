# Flappy Bird Env

<p align="center">
    <img src="https://raw.githubusercontent.com/robertoschiavone/flappy-bird-env/main/flappy-bird.gif"
        alt="flappy bird"/>
</p>

<table>
    <tbody>
        <tr>
            <td>Action Space</td>
            <td>Discrete(2)</td>
        </tr>
        <tr>
            <td>Observation Shape</td>
            <td>(800, 576, 3)</td>
        </tr>
        <tr>
            <td>Observation High</td>
            <td>255</td>
        </tr>
        <tr>
            <td>Observation Low</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Import</td>
            <td>import flappy_bird_env  # noqa<br/>gymnasium.make("FlappyBird-v0")</td>
        </tr>
    </tbody>
</table>

## Description

Flappy Bird as a Farama Gymnasium environment.

### Installation

```bash
pip install flappy-bird-env
```

### Usage

1. Play it by running

```bash
python -m flappy_bird_env
```

Press `space` to flap the wings.

2. Import it to train your RL model

```python
import flappy_bird_env  # noqa
env = gymnasium.make("FlappyBird-v0")
```

The package relies on ```import``` side-effects to register the environment
name so, even though the package is never explicitly used, its import is
necessary to access the environment.

## Action Space

Flappy Bird has the action space `Discrete(2)`.

| Value | Meaning    |
|-------|------------|
| 0     | NOOP       |
| 1     | flap wings |

## Observation Space

The observation will be the RGB image that is displayed to a human player with
observation space `Box(low=0, high=255, shape=(800, 576, 3), dtype=np.uint8)`.

### Rewards

You get `+1` every time you pass a pipe, otherwise `+0.001` for each frame where you
don't collide against the top and bottom bounds, or against a pipe.

## Version History

- v0: initial version release
