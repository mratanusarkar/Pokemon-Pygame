# Author: Atanu Sarkar
# Pokemon (my version)
# v0.0.0
# 05-May-2020, 11:00 PM (IST)

import pygame

# game constants
WIDTH = 800
HEIGHT = 600

# global variables
running = True

# initialize pygame
pygame.init()

# create display window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon")

# main game loop begins
while running:

    # background
    window.fill((0, 0, 0))

    # register events
    for event in pygame.event.get():
        # Quit Event
        if event.type == pygame.QUIT:
            running = False

    # render the display
    pygame.display.update()
