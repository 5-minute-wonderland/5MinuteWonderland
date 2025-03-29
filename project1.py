
print("hello world")
# num1 = 10
# num2 = 20
# print(num1,num2,"sum is:",num1+num2)

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
box = pygame.Rect(180,180,100,50)
wall = pygame.Rect(0,0,800,20)
wall2 = pygame.Rect(0,580,800,20)
box2 = pygame.Rect(600,200,100,30)

gameOn = True
while gameOn:
    screen.fill((0,40,80))
    pygame.draw.rect(screen,(150,75,0),wall)
    pygame.draw.rect(screen,(150,75,0),wall2)
    pygame.draw.rect(screen,(75,150,0),box2)


    pygame.draw.rect(screen,(200,10,10), box)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        box.move_ip(-1,0)
        if box.right < 0:
            box.left = 800
    elif key[pygame.K_d] == True:
        box.move_ip(1,0)
        if box.left > 800:
            box.right = 0 

    elif key[pygame.K_w] == True:
        box.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        box.move_ip(0, 1)

    elif key[pygame.K_i] == True:
        box2.move_ip(0, -1)

    elif key[pygame.K_k] == True:
        box2.move_ip(0, 1)

    if box.colliderect(wall) or box.colliderect(wall2):
        gameOn = False  
  



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           gameOn = False
    pygame.display.update()
    
pygame.quit()

       
    