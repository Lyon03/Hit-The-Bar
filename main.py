import pygame
from pygame.locals import *
import datetime
import time

pygame.init()

music = pygame.mixer.music.load("blahaj's favourite music.wav")
bg = pygame.image.load("shareMLH.png")

vel = 50
x = 100
y = 300
run = True
total_seconds = 60
count = 0
pygame.display.set_caption("Hit The Bar")
window = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
rect = Rect(x, y, 200, 50)
font = pygame.font.SysFont("nunito", 30, True)

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
        countText = font.render("Count: " + str(count), 1, (204, 255, 255))
        musicText1 = font.render("Paused",1,(0,0,0))
        musicText2 = font.render("Playing",1,(0,0,0))
        window.blit(bg,(0,0)) 
        pygame.draw.rect(window, (0,0,0), rect)
        window.blit(countText, (440, 10))
        pygame.display.update() 
        total_seconds -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                total_seconds = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    count +=1 
                    if count%2 == 1:
                        pygame.mixer.music.play()
                        window.blit(musicText2,(280,5))
                    else:
                        pygame.mixer.music.stop()
                        window.blit(musicText1,(280,5))
                    print(count)
                    pygame.display.update() 
