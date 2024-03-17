import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((805,805))

pygame.display.set_caption("circle")
gameon = True
x = 400
y = 400
while gameon:
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(x,y),25)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:#new circle draws everytime but screen.fill fills all by white everytime
                if y>0:
                    y-=20
                    pygame.draw.circle(screen,(255,0,0),(x,y),25)
            if event.key == pygame.K_LEFT:
                if x>0:
                    x-=20
                    pygame.draw.circle(screen,(255,0,0),(x,y),25)
            if event.key == pygame.K_RIGHT:
                if x<800:
                    x+=20
                    pygame.draw.circle(screen,(255,0,0),(x,y),25)
            if event.key == pygame.K_DOWN:
                if y<800:
                    y+=20
                    pygame.draw.circle(screen,(255,0,0),(x,y),25)
        if event.type == QUIT:
            gameon = False

    pygame.display.flip()
