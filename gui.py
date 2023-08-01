import pygame
import sys

block_size = 20

def grid_gui(x, y):
    global screen, clock, WINDOW_HEIGHT, WINDOW_WIDTH
    # pygame setup
    pygame.init()
    WINDOW_HEIGHT = y*block_size
    WINDOW_WIDTH = x*block_size
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    screen.fill("purple")

    while running:
        drawGrid()

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        obj = [(0,0), (1,3), (4,2), (2, 5)]

        drawObj(obj)

def drawGrid():
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, "white", rect, 1)

def drawObj(obj):
    for x, y in obj[0:]:
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(screen, "black", rect)
