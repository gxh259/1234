import pygame
import random

# 初始化游戏
pygame.init()

# 游戏窗口的宽度和高度
window_width = 800
window_height = 600

# 定义颜色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇')

# 设置游戏时钟
clock = pygame.time.Clock()

# 蛇的初始位置和大小
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# 食物的初始位置
food_position = [random.randrange(1, (window_width // 10)) * 10,
                 random.randrange(1, (window_height // 10)) * 10]
food_spawn = True

# 蛇的初始移动方向
direction = 'RIGHT'
change_to = direction

# 定义游戏结束函数
def game_over():
    font = pygame.font.SysFont('Arial', 40)
    text = font.render('游戏结束!', True, red)
    text_rect = text.get_rect()
    text_rect.center = (window_width // 2, window_height // 2)
    window.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'

    # 确保蛇不会反向移动
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # 根据移动方向更新蛇的位置
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    # 增加蛇的长度
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
    else:
        snake_body.pop()

    # 重新生成食物
    if not food_spawn:
        food_position = [random.randrange(1, (window_width // 10)) * 10,
                         random.randrange(1, (window_height // 10)) * 10]
    food_spawn = True

    # 绘制游戏窗口
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # 判断游戏结束条件
    if snake_position[0] < 0 or snake_position[0] > window_width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_height - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # 刷新游戏窗口
    pygame.display.update()
    clock.tick(20)
