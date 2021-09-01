import pygame, sys
from pygame.locals import *
pygame.init()
windowSurface = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('1234')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SKYBLUE = (135,206, 235)
CHOCO = (111, 82, 66)
basicFont = pygame.font.SysFont(None, 48)
message =  'fuckyou'
text = basicFont.render(message, False, WHITE, CHOCO)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
windowSurface.fill(SKYBLUE)
pixArray = pygame.PixelArray(windowSurface)
pixArray[500][360] = BLACK
del pixArray
windowSurface.blit(text, textRect)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == K_ESCAPE:
            pygame.quit()
            sys.exit()