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
<img src="/img/menu.png">
2. Players control the paddle to bounce the ball and break all the bricks.
<img src="/img/game.png">
3. If the ball falls off the bottom of the screen, the game ends, displaying a game over screen.
<img src="/img/end.png">
4. Players can restart or exit the game.
5. When all bricks are destroyed, players proceed to the next level.
<img src="/img/win.png">
6. The game has a total of 12 levels, and upon completing all levels, a game complete screen is displayed.

## Notes

- Ensure the game is run in an environment that supports Pygame.
- Game performance may vary based on computer hardware capabilities.
- The game code may need adjustments based on your Pygame version.

## Contribution

**YIN ZHIWEI**
   - Responsible for the game's core logic implementation.
   - Handled the Pygame library integration and event handling system.
   - Managed the game's user interface and menu system.

**LIAO JIONGYI**
   - In charge of the game's graphics and rendering.
   - Designed and implemented the brick layout and ball physics.
   - Developed the game's level progression system.

**CHEN XINYU**
   - Focused on testing and debugging the game.
   - Ensured game performance optimization across different hardware.
   - Handled the documentation and README file updates.

## License

This project is licensed under the MIT License. You are free to use, copy, modify, and distribute the code as long as you retain the original author's copyright notice and license statement.
