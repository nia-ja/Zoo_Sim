import time

import pygame
import sys

block_size = 20

def grid_gui(x, y):
    global screen, clock, window_hight, window_width
    # pygame setup
    pygame.init()
    window_hight = y*block_size
    window_width = x*block_size
    screen = pygame.display.set_mode((window_width, window_hight))
    clock = pygame.time.Clock()
    running = True

    while running:
        # drawGrid()

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        obj = [(0,0), (1,3), (4,2), (2, 5)]

        drawObj(obj)

        obj2 = [(0,0), (2, 5)]

        drawObj(obj2)


def drawGrid():
    for x in range(0, window_width, block_size):
        for y in range(0, window_hight, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, "white", rect, 1)

def drawObj(obj):
    screen.fill("purple")
    drawGrid()
    for x, y in obj[0:]:
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(screen, "black", rect)
    
    pygame.display.update()
    time.sleep(3)