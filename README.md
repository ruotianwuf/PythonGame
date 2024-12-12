# 3D Pinball Game README

## Introduction

3D Pinball Game is a simple pinball game developed using Python and the Pygame library. In the game, players control a paddle to bounce a ball, aiming to break all the bricks. The game features multiple levels, each with different brick quantities and layouts.

## Requirements

- Python 3.11
- Pygame library

## Installation Guide

1. Ensure Python is installed on your system.
2. Install the Pygame library using pip:
   ```
   pip install pygame
   ```
3. Save the `GameFrame.py` file to your computer.

## Gameplay

- Use the left and right arrow keys to control the paddle's movement.
- Press the Enter key to start the game or restart after a game over.
- Press the Esc key to quit the game.
- Press the P key to pause the game.
- When all bricks are destroyed, press the Tab key to proceed to the next level.

## Game Features

- The game window size is 800x600 pixels.
- The ball starts in the center of the screen with an upward initial speed.
- The paddle starts at the bottom center of the screen.
- Bricks are generated randomly, and a certain number of bricks are removed at the start of the game.
- The game has multiple levels, with an increasing number of bricks in each level.

## Code Structure

- `GameFrame.py`: Contains all the game logic and rendering code.
- Utilizes Pygame's event handling system to manage user input.
- Uses Pygame's graphics rendering capabilities to draw the ball, paddle, and bricks.

## Game Flow

1. The game starts with a menu, waiting for the player to press Enter to begin.
2. Players control the paddle to bounce the ball and break all the bricks.
3. If the ball falls off the bottom of the screen, the game ends, displaying a game over screen.
4. Players can restart or exit the game.
5. When all bricks are destroyed, players proceed to the next level.
6. The game has a total of 12 levels, and upon completing all levels, a game complete screen is displayed.

## Notes

- Ensure the game is run in an environment that supports Pygame.
- Game performance may vary based on computer hardware capabilities.
- The game code may need adjustments based on your Pygame version.

## Contribution

Contributions to improve and optimize the code are welcome. You can submit your modifications via Pull Requests.

## License

This project is licensed under the MIT License. You are free to use, copy, modify, and distribute the code as long as you retain the original author's copyright notice and license statement.
