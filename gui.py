from operator import itemgetter
import pygame
import sys
import time
import math

import color_palette

block_size = 80

def get_screen_size():
    pygame.init()
    infoObj = pygame.display.Info()
    screen_width = infoObj.current_w
    screen_height = infoObj.current_h
    return (screen_width, screen_height, block_size)

def grid_gui(x, y, get_coordinates, get_all_empty_xy):
    global screen, clock, window_hight, window_width, font_title, font_big, font_small, itarations, title
    # pygame setup
    window_hight = y*block_size
    window_width = x*block_size
    screen = pygame.display.set_mode((window_width, window_hight))
    clock = pygame.time.Clock()
    running = True
    iterations = 0
    title = "Elephant Zoo"
    pygame.display.set_caption(title)
    font_title = pygame.font.Font('fonts/Monoton-Regular.ttf', 50)
    font_big = pygame.font.Font('fonts/Righteous-Regular.ttf', 20)
    font_small = pygame.font.Font('fonts/ShareTechMono-Regular.ttf', 12)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if iterations < 1:
            drawStartScreen()
            time.sleep(10)
            iterations += 1
        else:
            drawObj(get_coordinates(), get_all_empty_xy())

def end_game():
    screen.fill(color_palette.dark_grey_hex)
    title_text = "The End"
    draw_logo(title_text)
    draw_title(title_text)

def draw_logo(title_text = ""):
    logo = pygame.image.load("img/logo.png")
    width_position = (screen.get_width() - logo.get_width()) / 2

    # get title height
    title_height = calc_title_height(title_text)
    height_position = (screen.get_height() - logo.get_height() - title_height) / 2 - 50

    screen.blit(logo, (width_position,height_position))

def get_title(title_text):
    title_imgs = []

    if title_text == "The End":
        img = font_title.render(title_text, True, pygame.Color(color_palette.teal_hex))
        title_imgs.append(img)
    else:
        for word in title_text.split(" "):
            # render a given font into an image
            img = font_title.render(word, True,
                    pygame.Color(color_palette.teal_hex))
            title_imgs.append(img)
    
    return title_imgs

def calc_title_height(title_text):
    title_imgs = get_title(title_text)
    return title_imgs[0].get_height() * len(title_imgs)


def draw_title(title_text):
    
    title_imgs = get_title(title_text)
    
    for idx, img in enumerate(title_imgs):
        # center on X axis
        width_position = (screen.get_width() - img.get_width()) / 2

        # calculate individual Y position to put all text in the middle on Y axis
        logo_height = 100
        height_position = (screen.get_height() - img.get_height() ) / 2 - (img.get_height() / 2 * len(title_imgs)) + (img.get_height() * idx) + logo_height / 2
        
        # put text image onto the screen
        screen.blit(img, (width_position,height_position))

def draw_grass(x, y, grass_type):
    if grass_type == "short":
        grass_img = pygame.image.load("img/grass/grass_short.png")

        count = math.floor(block_size / 15)

        for num in range(count):
            grass_target = pygame.Rect(x*block_size + 15 * num, y*block_size + 60, block_size, block_size)
            screen.blit(grass_img, grass_target)

    elif grass_type == "tall":
        grass_img = pygame.image.load("img/grass/grass.png")
        grass_target = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        screen.blit(grass_img, grass_target)

def draw_description(x, y, description):
    # add text (description)
    # first color - font color, second - background color
    screen.blit(font_big.render(f" {description} ", True, color_palette.teal_hex, color_palette.dark_grey_hex), (x*block_size, y*block_size+55))

def draw_progress(x,y,age,lifespan = 10):
    progress_line_length = 10
    lived = 0

    if 0 < age < lifespan:
        lived = math.floor(progress_line_length / lifespan * age)
    elif age == lifespan:
        lived = 10

    lived_square = pygame.image.load("img/squares/square_black.png")
    available_square = pygame.image.load("img/squares/square_teal.png")

    for num in range(lived):
        square_target = pygame.Rect(x*block_size + (block_size - 11), y*block_size + 6 * min(num, 9) + 10, block_size, block_size)
        screen.blit(lived_square, square_target)
    
    for num in range((lived),(progress_line_length)):
        square_target = pygame.Rect(x*block_size + (block_size - 11), y*block_size + 6 * num + 10, block_size, block_size)
        screen.blit(available_square, square_target)

def draw_failures(x, y, num):
    failure_img = pygame.image.load("img/grass/grass_fails.png")

    failure_remain = 3 - num

    for failure in range(failure_remain):
        failure_target = pygame.Rect(x*block_size + 19 + 14*failure, y*block_size + 64, block_size, block_size)

        screen.blit(failure_img, failure_target)



def drawGrid():
    for x in range(0, window_width, block_size):
        for y in range(0, window_hight, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, "white", rect, 1)

def drawStartScreen():
    screen.fill(color_palette.dark_grey_hex)

    draw_logo()

    draw_title(title)

    pygame.display.update()

def drawObj(obj, empty):
    screen.fill(color_palette.base_blue_hex)

    # empty tiles
    for x, y in empty[0:]:
        draw_grass(x, y, "tall")
    
    live_objs = 0

    # tiles with objects
    for x, y, color, description, image, id, size, age_bar, failures in obj[0:]:
        # change color of the block
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(screen, color, rect)

        # add image
        tileset = pygame.image.load(image)

        # for animals (50px*50px)
        if size == "small":
            target = pygame.Rect(x*block_size + 15, y*block_size + 15, block_size, block_size)
        # for landscape (80px*80px)
        else:
            target = pygame.Rect(x*block_size, y*block_size, block_size, block_size)

        screen.blit(tileset, target)

        if age_bar:
            live_objs += 1
            draw_progress(x, y, int(description))
        else:
            draw_description(x, y, description)
        
        if failures is not False:
            draw_failures(x, y, failures)

        # add text (id)
        screen.blit(font_small.render(f" id:{id} ", True, color_palette.dark_grey_hex, color_palette.teal_hex), (x*block_size, y*block_size))

    if live_objs == 0:
        end_game()
    else:
        drawGrid()
    

    pygame.display.update()
    # temp
    time.sleep(0.5)
    # time.sleep(3)