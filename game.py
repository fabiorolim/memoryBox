"""
Minicurso de introdução ao Pygame
Prof: Fábio Rolim
IFPI - CAPAU
"""

import pygame, time, random
from pygame.locals import *

pygame.init()
play_surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Memory Box')
red_colour = pygame.Color(255, 0, 0)
black_colour = pygame.Color(0, 0, 0)
white_colour = pygame.Color(255, 255, 255)
grey_colour = pygame.Color(150, 150, 150)
green_color = pygame.Color(0, 255, 0)
yellow_color = pygame.Color(255, 255, 0)
boxes_position = [240, 400, 300, 400, 360, 400, 300, 340]
play = []
level = 1
boxes = 1
wc = True


def greenBox1():
    return pygame.draw.rect(play_surface, green_color, Rect(boxes_position[0], boxes_position[1], 40, 40))


def whiteBox1():
    return pygame.draw.rect(play_surface, white_colour, Rect(boxes_position[0], boxes_position[1], 40, 40))


def greenBox2():
    return pygame.draw.rect(play_surface, green_color, Rect(boxes_position[2], boxes_position[3], 40, 40))


def whiteBox2():
    return pygame.draw.rect(play_surface, white_colour, Rect(boxes_position[2], boxes_position[3], 40, 40))


def greenBox3():
    return pygame.draw.rect(play_surface, green_color, Rect(boxes_position[4], boxes_position[5], 40, 40))


def whiteBox3():
    return pygame.draw.rect(play_surface, white_colour, Rect(boxes_position[4], boxes_position[5], 40, 40))


def greenBox4():
    return pygame.draw.rect(play_surface, green_color, Rect(boxes_position[6], boxes_position[7], 40, 40))


def whiteBox4():
    return pygame.draw.rect(play_surface, white_colour, Rect(boxes_position[6], boxes_position[7], 40, 40))

#Animação da tela de inicio
def generateWelcome():
    start()
    random_play = []

    for i in range(5):
        random_play.append(random.randrange(1, 5))

    for b in random_play:
        start()
        if (b == 1):
            greenBox1()
        if (b == 2):
            greenBox2()
        if (b == 3):
            greenBox3()
        if (b == 4):
            greenBox4()
        pygame.display.update()
        time.sleep(0.5)
    return random_play

def start():
    whiteBox1()
    whiteBox2()
    whiteBox3()
    whiteBox4()
    pygame.display.update()

def welcome():
    welcomeFont = pygame.font.Font('freesansbold.ttf', 40)
    welcomeSurf = welcomeFont.render('MEMORY BOX', True, green_color)
    welcomeRect = welcomeSurf.get_rect()
    welcomeRect.midtop = (320, 100)
    play_surface.blit(welcomeSurf, welcomeRect)
    welcomeSurf2 = welcomeFont.render('PRESS ENTER TO START...', True, green_color)
    welcomeRect2 = welcomeSurf2.get_rect()
    welcomeRect2.midtop = (320, 250)
    play_surface.blit(welcomeSurf2, welcomeRect2)
    start()
    generateWelcome()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                global wc
                wc = False


def win():
    play_surface.fill(black_colour)
    pygame.display.flip()
    winFont = pygame.font.Font('freesansbold.ttf', 40)
    winSurf = winFont.render('Level %d' % level, True, yellow_color)
    winRect = winSurf.get_rect()
    winRect.midtop = (320, 250)
    play_surface.blit(winSurf, winRect)
    pygame.display.update()
    time.sleep(1)


def gameOver():
    play_surface.fill(black_colour)
    gameOverFont = pygame.font.Font('freesansbold.ttf', 48)
    gameOverSurf = gameOverFont.render('Game Over!', True, red_colour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 200)
    play_surface.blit(gameOverSurf, gameOverRect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    exit()


# gerando os boxes randomicamente
def generateBoxes():
    start()
    random_play = []
    play_surface.fill(black_colour)

    for i in range(boxes):
        random_play.append(random.randrange(1, 5))
    # print(randomPlay)

    # Mostrando ao jogador os boxes gerados
    for b in random_play:
        start()
        if (b == 1):
            greenBox1()
        if (b == 2):
            greenBox2()
        if (b == 3):
            greenBox3()
        if (b == 4):
            greenBox4()
        pygame.display.update()
        time.sleep(1)
    return random_play


#Jogando
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
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    greenBox3()
                    play.append(3)
                if event.key == K_LEFT or event.key == ord('a'):
                    greenBox1()
                    play.append(1)
                if event.key == K_UP or event.key == ord('w'):
                    greenBox4()
                    play.append(4)
                if event.key == K_DOWN or event.key == ord('s'):
                    greenBox2()
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
                pygame.display.update()
                time.sleep(0.4)