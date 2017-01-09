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
boxesPosition = [240, 400, 300, 400, 360, 400, 300, 340]
wc = True
level = 1

def greenBox1():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def whiteBox1():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def greenBox2():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def whiteBox2():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def greenBox3():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def whiteBox3():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def greenBox4():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[6], boxesPosition[7], 40, 40))


def whiteBox4():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[6], boxesPosition[7], 40, 40))


def start():
    #playSurface.fill(blackColour)
    whiteBox1()
    whiteBox2()
    whiteBox3()
    whiteBox4()

# gerando os boxes randomicamente para tela inicial
def generateWelcome():
    start()
    randomPlay = []

    for i in range(5):
        randomPlay.append(random.randrange(1, 5))
    #print(randomPlay)

    # Mostrando ao jogador os boxes gerados
    for b in randomPlay:
        start()
        if (b == 1):
            greenBox1()
            pygame.display.flip()
            time.sleep(0.5)
        if (b == 2):
            greenBox2()
            pygame.display.flip()
            time.sleep(0.5)
        if (b == 3):
            greenBox3()
            pygame.display.flip()
            time.sleep(0.5)
        if (b == 4):
            greenBox4()
            pygame.display.flip()
            time.sleep(0.5)
    return randomPlay

def win():
    playSurface.fill(blackColour)
    pygame.display.flip()
    winFont = pygame.font.Font('freesansbold.ttf', 40)
    winSurf = winFont.render('Level %d' % level, True, yellowColor)
    winRect = winSurf.get_rect()
    winRect.midtop = (320, 250)
    playSurface.blit(winSurf, winRect)
    pygame.display.flip()
    time.sleep(2)

def welcome():
    welcomeFont = pygame.font.Font('freesansbold.ttf', 40)
    welcomeSurf = welcomeFont.render('BOX MEMORY', True, greenColor)
    welcomeRect = welcomeSurf.get_rect()
    welcomeRect.midtop = (320, 100)
    playSurface.blit(welcomeSurf, welcomeRect)
    welcomeSurf2 = welcomeFont.render('PRESS ENTER TO START...', True, greenColor)
    welcomeRect2 = welcomeSurf2.get_rect()
    welcomeRect2.midtop = (320, 250)
    playSurface.blit(welcomeSurf2, welcomeRect2)
    pygame.display.flip()
    start()
    pygame.display.flip()
    generateWelcome()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                global wc
                wc = False

while wc:
    welcome()
#    start()
#    generateWelcome()
win()
print('saiu!')
