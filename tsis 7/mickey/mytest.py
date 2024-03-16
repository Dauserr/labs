import pygame
from datetime import datetime
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Chasy")
main = pygame.image.load("labs/tsis 7/mickey/mainclock.png")
left = pygame.image.load("labs/tsis 7/mickey/leftarm.png")
right = pygame.image.load("labs/tsis 7/mickey/rightarm.png")
gameon = True
center = (400,370)
current_time = datetime.now()
current_minutes = current_time.minute
current_seconds = current_time.second
print("Current Minutes:", current_minutes)
print("Current Seconds:", current_seconds)

clock = pygame.time.Clock()
while gameon:
    screen.fill((255,255,255))

    rect = main.get_rect()
    rect.center = center
    screen.blit(main,rect)

    current_time = datetime.now()
    current_minutes = current_time.minute
    current_seconds = current_time.second
    sec_angle = current_seconds * 6 # 1 second == 6 degrees
    min_angle = current_minutes * 6

    #seconds = pygame.time.get_ticks() // 1000 # the number of milliseconds, //100 gives seconds
    #sec_angle = seconds * 6 # 1 second == 6 degrees
    #min_angle = seconds/10

    rotated_left = pygame.transform.rotate(left, -sec_angle-5)# "-" что бы по часовой было
    rect = rotated_left.get_rect()
    rect.center = center
    screen.blit(rotated_left,rect)

    rotated_right = pygame.transform.rotate(right, -min_angle-9)
    rect = rotated_right.get_rect()
    rect.center = center
    screen.blit(rotated_right,rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            gameon = False

    #seconds -= 6
    #minutes -= 6/60
    pygame.display.flip()
    clock.tick(165) # smooth
