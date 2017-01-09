import pygame, sys, time, random
from pygame.locals import *

pygame.init()
timer = pygame.time.Clock()
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Memory Box')
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
greenColor = pygame.Color(0, 255, 0)
yellowColor = pygame.Color(255, 255, 0)
playSurface.fill(blackColour)
boxesPosition = [240, 400, 300, 400, 360, 400, 300, 340]
play = []
randomPlay = []
nivel = 1
boxes = 4