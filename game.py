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
play = []
level = 1
boxes = 1
wc = True


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


def generateWelcome():
    start()
    randomPlay = []

    for i in range(5):
        randomPlay.append(random.randrange(1, 5))
    # print(randomPlay)

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


def start():
    #    playSurface.fill(blackColour)
    whiteBox1()
    whiteBox2()
    whiteBox3()
    whiteBox4()
    pygame.display.flip()


def win():
    playSurface.fill(blackColour)
    pygame.display.flip()
    winFont = pygame.font.Font('freesansbold.ttf', 40)
    winSurf = winFont.render('Level %d' % level, True, yellowColor)
    winRect = winSurf.get_rect()
    winRect.midtop = (320, 250)
    playSurface.blit(winSurf, winRect)
    pygame.display.flip()
    time.sleep(1)


def gameOver():
    playSurface.fill(blackColour)
    gameOverFont = pygame.font.Font('freesansbold.ttf', 48)
    gameOverSurf = gameOverFont.render('Game Over!', True, redColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 200)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


# gerando os boxes randomicamente
def generateBoxes():
    start()
    randomPlay = []
    playSurface.fill(blackColour)

    for i in range(boxes):
        randomPlay.append(random.randrange(1, 5))
    # print(randomPlay)

    # Mostrando ao jogador os boxes gerados
    for b in randomPlay:
        start()
        if (b == 1):
            greenBox1()
            pygame.display.flip()
            time.sleep(1)
        if (b == 2):
            greenBox2()
            pygame.display.flip()
            time.sleep(1)
        if (b == 3):
            greenBox3()
            pygame.display.flip()
            time.sleep(1)
        if (b == 4):
            greenBox4()
            pygame.display.flip()
            time.sleep(1)
    return randomPlay


# Jogando
while True:

    while wc:
        welcome()

    win()
    gaming = True
    start()
    computer = generateBoxes()

    while gaming:
        start()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    greenBox3()
                    pygame.display.flip()
                    play.append(3)
                if event.key == K_LEFT or event.key == ord('a'):
                    greenBox1()
                    pygame.display.flip()
                    play.append(1)
                if event.key == K_UP or event.key == ord('w'):
                    greenBox4()
                    pygame.display.flip()
                    play.append(4)
                if event.key == K_DOWN or event.key == ord('s'):
                    greenBox2()
                    pygame.display.flip()
                    play.append(2)
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                if event.key == K_RETURN:
                    if play == computer:
                        play = []
                        level += 1
                        boxes += 1
                    else:
                        gameOver()
                    gaming = False
        timer.tick(60)
