import pygame
from pygame.locals import *
import time
import random

pygame.init()

black = (0, 0, 0)
white = (51, 153, 255)
green = (51, 102, 0)
red = (201, 18, 18)
yellow = (239, 250, 32)

win_width = 600
win_height = 400

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Bachpan Ka Game")
time.sleep(5)

clock = pygame.time.Clock()

snake = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri", 25)
score_font = pygame.font.SysFont("comicsans", 20)  # Corrected font name

def user_score(score):
    number = score_font.render("Score: " + str(score), True, yellow)
    window.blit(number, [0, 0])

def draw_food(foodx, foody, radius):
    pygame.draw.circle(window, red, (foodx + radius, foody + radius), radius)

  
def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])

def message(msg, color):
    bold_font = pygame.font.SysFont("calibri", 25, bold=True)  # Set bold=True
    mssg = bold_font.render(msg, True, color)
    window.blit(mssg, [win_width / 16, win_height / 2])

def game_loop():
    gameover = False
    gameclose = False
    
    x1 = win_width / 2
    y1 = win_height / 2
    
    x1_change = 0
    y1_change = 0

    snake_length_list = []  # List to keep track of the snake's position
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not gameover:
        while gameclose:
            window.fill(white)
            message("you lost! press p to play again and Q to quit the game", black)
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        gameclose = False
                    elif event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:    
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                elif event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake

        # Screen wrapping logic
        if x1 >= win_width:  # Right edge
            x1 = 0
        elif x1 < 0:  # Left edge
            x1 = win_width
        
        if y1 >= win_height:  # Bottom edge
            y1 = 0
        elif y1 < 0:  # Top edge
            y1 = win_height      
        
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        
        
        pygame.draw.rect(window, red, [foodx, foody, snake, snake])
        snake_size = [x1, y1]
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        # Check for collision with itself
        for segment in snake_length_list[:-1]:  # Compare against all but the last segment
            if x1 == segment[0] and y1 == segment[1]:
                gameclose = True
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

