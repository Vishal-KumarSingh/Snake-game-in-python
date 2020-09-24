import pygame
from pygame import mixer
import time
import random
pygame.init()
mixer.init()

direction = 2
screen_width = 600
screen_height = 500
exit_game = False
snake_x = 20
snake_y = 20
snake_width = 10
snake_height = 10
food_x = random.randint(50, screen_width-50)
food_y = random.randint(50, screen_height-50)
food_width = 10
food_height = 10
speed = 10
velocity_x = speed
velocity_y = 0
score = 10
snk_pos=[]
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

while not exit_game:
    for event in pygame.event.get():
        if event.type == 12:
            direction=3
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if direction != 1:
                    velocity_y = speed
                    velocity_x = 0
                    direction = 3
            if event.key == pygame.K_UP:
                if direction != 3:
                    velocity_y = -speed
                    velocity_x = 0
                    direction = 1
            if event.key == pygame.K_LEFT:
                if direction != 2:
                    velocity_x = -speed
                    velocity_y = 0
                    direction = 4
            if event.key == pygame.K_RIGHT:
                if direction != 4:
                    velocity_x = speed
                    velocity_y = 0
                    direction = 2
    if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
        score = score + 10
        food_x = random.randint(50, screen_width-50)
        food_y = random.randint(50, screen_height-50)
        snk_pos.append([snake_x,snake_y])
        mixer.music.load("sms.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
    snake_y += velocity_y
    snake_x += velocity_x
    if snake_x > screen_width or snake_x < 0 or snake_y > screen_height or snake_y < 0:
        mixer.music.load("game_over.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        time.sleep(1)
        exit_game=True

    snk_pos.append([snake_x,snake_y])
    gamewindow.fill((255, 255, 255))
    text_screen(str(score), (0, 0, 0), 5, 5)
    i=0
    for i in range(int(score/10)):
         pygame.draw.rect(gamewindow, (0, 0, 0), [snk_pos[i][0], snk_pos[i][1], snake_width, snake_height])

    del snk_pos[0]
    pygame.draw.rect(gamewindow, (255, 0, 0), [food_x, food_y, food_width, food_height])
    pygame.display.update()
    clock.tick(20)
