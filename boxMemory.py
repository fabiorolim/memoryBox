import pygame, sys, time, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
display = pygame.display.set_mode((640, 480))
# suface = pygame.Surface((600, 440))
pygame.display.set_caption('Memory Box')
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
greenColor = pygame.Color(0, 255, 0)
yellowColor = pygame.Color(255, 255, 0)
boxesPosition = [240, 400, 300, 400, 360, 400, 300, 340]
timer = pygame.time.Clock()
running = True


def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 24)
    gameOverSurf = gameOverFont.render('Game Over', True, redColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    display.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


def welcome():
    gameWelcomeFont = pygame.font.Font('freesansbold.ttf', 28)
    gameWelcomeSurf = gameWelcomeFont.render('MEMORY BOX', True, yellowColor)
    gameWelcomeRect = gameWelcomeSurf.get_rect()
    gameWelcomeRect.midtop = (640, 480)
    display.blit(gameWelcomeSurf, gameWelcomeRect)
    pygame.display.flip()
    time.sleep(2)


def start():
    display.fill(blackColour)
    whiteBox1()
    whiteBox2()
    whiteBox3()
    whiteBox4()
    pygame.display.flip()
    running = True


# Gerando os boxes randomicamentes
def computer(boxes, nivel):

    randomPlay = []
    c = 0
    for i in range(boxes):
        randomPlay.append(random.randrange(1, 4))
        c += 1
    print('c %d' % c)
    print(randomPlay)

    # Mostrando ao jogador os boxes gerados
    e = 0
    for b in randomPlay:
        start()
        e += 1
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

    # randomPlay = []
    print('e %d' % e)
    return randomPlay


def greenBox1():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def whiteBox1():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def greenBox2():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def whiteBox2():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def greenBox3():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def whiteBox3():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def greenBox4():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[6], boxesPosition[7], 40, 40))


def whiteBox4():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[6], boxesPosition[7], 40, 40))


'''
def begin(nivel, boxes):

    randomPlay = []
    start()
    fpsClock.tick(20)

    # Gerando os boxes randomicamentes
    c = 0
    for i in range(boxes):
        randomPlay.append(random.randrange(1, 4))
        c += 1
    print('c %d' % c)
    print(randomPlay)

    # Mostrando ao jogador os boxes gerados
    e = 0
    for b in randomPlay:
        start()
        e += 1
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

    #randomPlay = []
    print('e %d' % e)
    return randomPlay


def round(randomPlay):
    play = []
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
    if event.key == K_KP_ENTER:
        if randomPlay == random:
            print('Venceu!')
        else:
            gameOver()
'''

while running == True:
    print('Comecou')
    start()
    timer.tick(27)
    computer = computer(4, 1)
    play = []
    for event in pygame.event.get():
        print('Estamos jogando!')
        print(event)
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            print('Detectou tecla')
            if event.key == K_LEFT:
                greenBox1()
                pygame.display.flip()
                play.append(1)
                print('LEFT')
            if event.key == K_UP:
                greenBox4()
                pygame.display.flip()
                play.append(4)
            if event.key == K_RIGHT:
                greenBox2()
                pygame.display.flip()
                play.append(2)
    if computer == play:
        running = False
start()
