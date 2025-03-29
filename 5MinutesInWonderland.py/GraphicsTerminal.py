import pygame
import pygame.freetype
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('5 Minutes in Wonderland')

alice = pygame.image.load('C:\\Python Programs\\.venv\\5MinutesInWonderland.py\\5 Min in Wonderland PNGs\\Alice.PNG').convert_alpha()
alice = pygame.transform.scale(alice,(300,300))
forestBG = pygame.image.load('C:\\Python Programs\\.venv\\5MinutesInWonderland.py\\5 Min in Wonderland PNGs\\Forest BG.png').convert()
forestBG = pygame.transform.scale(forestBG,(600,600))
textBox = pygame.image.load('C:\\Python Programs\\.venv\\5MinutesInWonderland.py\\5 Min in Wonderland PNGs\\TextBox.PNG').convert_alpha()
textBox = pygame.transform.scale(textBox,(550,550))

aliceRect = alice.get_rect()
aliceRect.center = ((300,300))
textBoxRect = textBox.get_rect()
textBoxRect.center = ((300,500))

pygame.display.flip()
run = True
while run:
    screen.blit(forestBG, forestBG.get_rect())
    screen.blit(alice, aliceRect)
    screen.blit(textBox, textBoxRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()           
    pygame.display.update()