from xml.dom import xmlbuilder
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

xScreen = 640
yScreen = 480

xSnake = xScreen/2
ySnake = yScreen/2

velocity = 5
xControl = velocity
yControl = 0

xApple = randint(40, 600)
yApple = randint(50, 430)

apples = 0

font = pygame.font.SysFont('arial', 40, True, False)

screen = pygame.display.set_mode((xScreen, yScreen))

pygame.display.set_caption("Sussiest game omag!!")

clock = pygame.time.Clock()

listSnake = []

inicialSize = 5

def inscreaseSnakeSize(listSnake):
    for XandY in listSnake:
        pygame.draw.rect(screen, (0, 255, 0), (XandY[0], XandY[1], 20, 20))

while True:
    clock.tick(60)
    screen.fill((25, 25, 25))
    message = f'Apples: {apples}'
    formatedText = font.render(message, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # new movement

        if event.type == KEYDOWN:
            if event.key == K_a:
                if xControl == velocity:
                    pass
                else:
                    xControl = -velocity
                    yControl = 0
            if event.key == K_d:
                if xControl == -velocity:
                    pass
                else:
                    xControl = velocity
                    yControl = 0
            if event.key == K_w:
                if yControl == velocity:
                    pass
                else:
                    yControl = -velocity
                    xControl = 0
            if event.key == K_s:
                if yControl == -velocity:
                    pass
                else:
                    yControl = velocity
                    xControl = 0

    xSnake += xControl 
    ySnake += yControl

    snake = pygame.draw.rect(screen, (0, 255, 0), (xSnake, ySnake, 20, 20))

    apple = pygame.draw.rect(screen, (255, 0, 0), (xApple, yApple, 20, 20))

    if snake.colliderect(apple):
        xApple = randint(40, 600)
        yApple = randint(50, 430)
        apples += 1
        inicialSize += 1

    listHead = []
    listHead.append(xSnake)
    listHead.append(ySnake)

    listSnake.append(listHead)

    if len(listSnake) > inicialSize:
        del listSnake[0]

    inscreaseSnakeSize(listSnake)

    screen.blit(formatedText,(450, 40))

    pygame.display.update()