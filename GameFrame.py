import time

import pygame
import sys
import random
from pygame.locals import *
from pygame.math import Vector2

# 初始化pygame
pygame.init()

winnum = 1

# 设置屏幕大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 设置标题
pygame.display.set_caption("3D Pinball Game")

# 设置颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BRICK_COLORS = [(200, 50, 50), (50, 200, 50), (50, 50, 200), (200, 200, 50), (50, 200, 200)]

# 设置球的初始位置和速度
ball_pos = Vector2(WIDTH // 2, HEIGHT // 2)
ball_speed = Vector2(0, -5)  # 初始速度向上
ball_direction = 0

# 设置球的半径
ball_radius = 10

level_situation = []

# 设置弹跳板的初始位置和大小
paddle_pos_x = WIDTH // 2 - 30
paddle_pos_y = HEIGHT - 50
paddle_width = 60
paddle_height = 10
paddle_direction = 0

# 设置砖块
bricks = []
brick_width = 40
brick_height = 20
num_bricks_x = WIDTH // brick_width
num_bricks_y = 1

for i in range(num_bricks_x):
    for j in range(num_bricks_y):
        brick_pos_x = i * brick_width + brick_width // 2
        brick_pos_y = j * brick_height + brick_height // 2
        bricks.append((brick_pos_x, brick_pos_y, random.choice(BRICK_COLORS)))


# 生成20个0到64之间不重复的随机数（包括0但不包括64）
random_numbers = random.sample(range(len(bricks) + 1), (len(bricks) + 1) // 4)

# print(random_numbers)
num = 0
for brick_have in bricks:
    num = num + 1
    if num in random_numbers:
        bricks.remove(brick_have)

# print(num)

# 定义菜单函数
def show_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Menu", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(text, text_rect)

        play_text = font.render("Press Enter to Play", True, GREEN)
        play_text_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(play_text, play_text_rect)

        quit_text = font.render("Press Esc to Quit", True, BLUE)
        quit_text_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
        screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(15)
# 定义暂停界面函数
def show_pause_menu():
    global paused
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_p:  # 按下P键继续游戏
                    paused = False
                elif event.key == pygame.K_ESCAPE:  # 按下Esc键退出游戏
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Paused", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(text, text_rect)

        continue_text = font.render("Press P to Continue", True, GREEN)
        continue_text_rect = continue_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(continue_text, continue_text_rect)

        quit_text = font.render("Press Esc to Quit", True, BLUE)
        quit_text_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
        screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(15)

# 显示菜单
show_menu()

# 游戏主循环
running = True
game_over = False
game_win = False
AllWin = False


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_TAB and game_win:
                # 下一关
                winnum += 1
                ball_pos = Vector2(paddle_pos_x + paddle_width // 2, paddle_pos_y - ball_radius)
                ball_speed = Vector2(0, -5)  # 初始速度向上
                paddle_pos_x = WIDTH // 2 - 30
                bricks = []
                num_bricks_y = num_bricks_y + 2
                for i in range(num_bricks_x):
                    for j in range(num_bricks_y):
                        brick_pos_x = i * brick_width + brick_width // 2
                        brick_pos_y = j * brick_height + brick_height // 2
                        bricks.append((brick_pos_x, brick_pos_y, random.choice(BRICK_COLORS)))
                # print(len(bricks))

                random_numbers = random.sample(range(len(bricks) + 1), (len(bricks) + 1) // 4)

                # print(random_numbers)
                num = 0
                for brick_have in bricks:
                    num = num + 1
                    if num in random_numbers:
                        bricks.remove(brick_have)

                # print(num)
                game_win = False
            if event.key == pygame.K_RETURN and game_over:
                # 重置游戏状态
                ball_pos = Vector2(paddle_pos_x + paddle_width // 2, paddle_pos_y - ball_radius)
                ball_speed = Vector2(0, -5)  # 初始速度向上
                paddle_pos_x = WIDTH // 2 - 30
                bricks = []
                for i in range(num_bricks_x):
                    for j in range(num_bricks_y):
                        brick_pos_x = i * brick_width + brick_width // 2
                        brick_pos_y = j * brick_height + brick_height // 2
                        bricks.append((brick_pos_x, brick_pos_y, random.choice(BRICK_COLORS)))
                # print(len(bricks))

                random_numbers = random.sample(range(len(bricks) + 1), (len(bricks) + 1) // 4)

                # print(random_numbers)
                num = 0
                for brick_have in bricks:
                    num = num + 1
                    if num in random_numbers:
                        bricks.remove(brick_have)

                # print(num)
                game_over = False
            if event.key == pygame.K_p:  # 检测P键是否被按下，用于暂停游戏
                show_pause_menu()  # 显示暂停菜单

    # 清屏
    screen.fill(WHITE)

    if not game_over:
        # 移动球
        ball_pos += ball_speed

        # 检测边界碰撞
        if ball_pos.x - ball_radius < 0 or ball_pos.x + ball_radius > WIDTH:
            ball_speed.x = -ball_speed.x
        if ball_pos.y - ball_radius < 0:
            ball_speed.y = -ball_speed.y

        # 检测砖块碰撞
        for brick in bricks[:]:
            brick_rect = pygame.Rect(brick[0] - brick_width // 2, brick[1] - brick_height // 2, brick_width, brick_height)
            ball_rect = pygame.Rect(ball_pos.x - ball_radius, ball_pos.y - ball_radius, ball_radius * 2, ball_radius * 2)
            if brick_rect.colliderect(ball_rect):
                ball_speed.y = -ball_speed.y
                # 添加水平速度分量
                if ball_direction == -1:
                    ball_speed.x = -3  # 随机选择-3或3作为水平速度
                    paddle_direction = 0
                elif ball_direction == 1:
                    ball_speed.x = 3
                    paddle_direction = 0
                bricks.remove(brick)
                # print(brick)
                break

        # 检测弹跳板碰撞
        paddle_rect = pygame.Rect(paddle_pos_x, paddle_pos_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_pos.x - ball_radius, ball_pos.y - ball_radius, ball_radius * 2, ball_radius * 2)
        if paddle_rect.colliderect(ball_rect):
            ball_speed.y = -ball_speed.y
            # 添加水平速度分量
            if paddle_direction == -1:
                ball_speed.x = -3  # 随机选择-3或3作为水平速度
                paddle_direction = 0
                ball_direction = -1
            elif paddle_direction == 1:
                ball_speed.x = 3
                paddle_direction = 0
                ball_direction = 1

        # 绘制球
        pygame.draw.circle(screen, RED, (int(ball_pos.x), int(ball_pos.y)), ball_radius)

        # 绘制砖块
        for brick in bricks:
            pygame.draw.rect(screen, brick[2], pygame.Rect(brick[0] - brick_width // 2, brick[1] - brick_height // 2, brick_width, brick_height))

        # 绘制弹跳板
        pygame.draw.rect(screen, BLUE, pygame.Rect(paddle_pos_x, paddle_pos_y, paddle_width, paddle_height))

        # 玩家控制弹跳板
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_pos_x > 0:
            paddle_direction = -1
            # print("Moving left")
            paddle_pos_x -= 5
        if keys[pygame.K_RIGHT] and paddle_pos_x < WIDTH - paddle_width:
            paddle_direction = 1
            # print("Moving right")
            paddle_pos_x += 5

        # 检测游戏结束
        if ball_pos.y + ball_radius > HEIGHT:
            game_over = True
    else:
        # 绘制游戏结束文本
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press Enter to Restart", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    # print(bricks)
    if not bricks and not AllWin:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Win! Press Tab to next Level", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        game_win = True
        print(winnum)


    if winnum == 12:
        AllWin = True

    if AllWin:
        print("1")
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Game Complete!", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        time.sleep(5)
        num_bricks_y = 1
        show_menu()


    # 更新屏幕
    pygame.display.flip()

    # 控制游戏刷新速度
    pygame.time.Clock().tick(100)

    ball_direction = 0

# 退出pygame
pygame.quit()
sys.exit()