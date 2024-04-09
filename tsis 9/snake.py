import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Snake")
gameon = True

FPS = pygame.time.Clock()
direction = "UP"

mx = 400
my = 300


def body(mx,my):
    return pygame.draw.rect(screen, (0, 0, 255), (mx,my,10,10))

speed = 10
snake = [(400, 300), (390, 300), (380, 300)]

def randomapple():
    while True:
        applex = random.randint(1,79)*10
        appley = random.randint(1,59)*10
        apple_rect = pygame.Rect(applex, appley, 10, 10)
        if not any(apple_rect.colliderect(pygame.Rect(*segment, 10, 10)) for segment in snake):
            return applex, appley

applex,appley = randomapple()

counter = 0
level = 0

font = pygame.font.SysFont("Score", 30)
font2 = pygame.font.SysFont("Level", 30)

minus = 0
myevent = pygame.USEREVENT + 1
while gameon:
    FPS.tick(60)
    pygame.time.delay(100-int(minus))
    screen.fill((0, 255, 0))

    scorecnt = font.render("Score: " + str(counter), True, (0, 0, 0))
    screen.blit(scorecnt, (10,5))
    levelcnt = font.render("Level: " + str(level), True, (0, 0, 0))
    screen.blit(levelcnt, (10,25))



    for event in pygame.event.get():
        if event.type == myevent:
            applex,appley = randomapple()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
        if event.type == QUIT:
            gameon = False

    if direction == "UP":
        snake.insert(0, (snake[0][0], snake[0][1]-speed))
    elif direction == "DOWN":
        snake.insert(0, (snake[0][0], snake[0][1]+speed))
    elif direction == "LEFT":
        snake.insert(0, (snake[0][0]-speed, snake[0][1]))
    elif direction == "RIGHT":
        snake.insert(0, (snake[0][0]+speed, snake[0][1]))

    for segment in snake:
        pygame.draw.rect(screen, (0, 0, 255), (*segment, 10, 10))

    apple = pygame.draw.rect(screen, (255, 0, 0), (applex,appley,10,10))

    if pygame.Rect(*snake[0],10,10).colliderect(apple): # * for unpacking, pygame.rect for collision
        applex,appley = randomapple()
        num = random.randint(1,3)
        for i in range(0,num):
            counter += 1
            if counter % 5 == 0 :
                level += 1
                minus += 2.5

        pygame.time.set_timer(myevent, 20000) # every 20 seconds respawn apple
    else:
        snake.pop()

    for segment in snake[1:]:  # start from 1 to avoid head
        if pygame.Rect(*snake[0],10,10).colliderect(pygame.Rect(*segment, 10, 10)):
            gameon = False
            break

    if snake[0][0] > 800 or snake[0][0] < 0 or snake[0][1]>600 or snake[0][1]<0:
        gameon = False


    pygame.display.flip()
    """
    i have commented my code
    """
