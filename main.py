import pygame
from pygame.locals import *
import datetime
import time

pygame.init()
window = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

vel = 50
x = 100
y = 300
rect = Rect(x, y, 200, 50)
run = True
total_seconds = 60
score = 0
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        if x > vel:
            vel *= 1.3
        else:
            vel = x

        if (rect.left >=300 or rect.left<100):
            vel *= -1

        rect.left += vel
        window.fill((0,0,0))
        pygame.draw.rect(window, (255,0,0), rect)   
        pygame.display.update() 
        total_seconds -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                total_seconds = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    score+=1
                    print(score)
