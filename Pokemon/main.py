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

# Input key states (keyboard)
LEFT_ARROW_KEY_PRESSED = 0
RIGHT_ARROW_KEY_PRESSED = 0
UP_ARROW_KEY_PRESSED = 0
DOWN_ARROW_KEY_PRESSED = 0
A_KEY_PRESSED = 0
W_KEY_PRESSED = 0
S_KEY_PRESSED = 0
D_KEY_PRESSED = 0
SPACE_BAR_PRESSED = 0
ENTER_KEY_PRESSED = 0
ESC_KEY_PRESSED = 0

# create display window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon")


def key_logger(key_event):
    global LEFT_ARROW_KEY_PRESSED
    global RIGHT_ARROW_KEY_PRESSED
    global UP_ARROW_KEY_PRESSED
    global DOWN_ARROW_KEY_PRESSED
    global A_KEY_PRESSED
    global W_KEY_PRESSED
    global S_KEY_PRESSED
    global D_KEY_PRESSED
    global SPACE_BAR_PRESSED
    global ENTER_KEY_PRESSED
    global ESC_KEY_PRESSED

    # Keypress Down Event
    if key_event.type == pygame.KEYDOWN:
        # Left Arrow Key down
        if key_event.key == pygame.K_LEFT:
            print("LOG: Left Arrow Key Pressed Down")
            LEFT_ARROW_KEY_PRESSED = 1
        # Right Arrow Key down
        if key_event.key == pygame.K_RIGHT:
            print("LOG: Right Arrow Key Pressed Down")
            RIGHT_ARROW_KEY_PRESSED = 1
        # Up Arrow Key down
        if key_event.key == pygame.K_UP:
            print("LOG: Up Arrow Key Pressed Down")
            UP_ARROW_KEY_PRESSED = 1
        # Down Arrow Key down
        if key_event.key == pygame.K_DOWN:
            print("LOG: Down Arrow Key Pressed Down")
            DOWN_ARROW_KEY_PRESSED = 1
        # A Key down
        if key_event.key == pygame.K_a:
            print("LOG: A Key Pressed Down")
            A_KEY_PRESSED = 1
        # D Key down
        if key_event.key == pygame.K_d:
            print("LOG: D Key Pressed Down")
            D_KEY_PRESSED = 1
        # W Key down
        if key_event.key == pygame.K_w:
            print("LOG: W Key Pressed Down")
            W_KEY_PRESSED = 1
        # S Key down
        if key_event.key == pygame.K_s:
            print("LOG: S Key Pressed Down")
            S_KEY_PRESSED = 1
        # Space Bar down
        if key_event.key == pygame.K_SPACE:
            print("LOG: Space Bar Pressed Down")
            SPACE_BAR_PRESSED = 1
        # Enter Key down ("Carriage RETURN key" from old typewriter lingo)
        if key_event.key == pygame.K_RETURN:
            print("LOG: Enter Key Pressed Down")
            ENTER_KEY_PRESSED = 1
        # Esc Key down
        if key_event.key == pygame.K_ESCAPE:
            print("LOG: Escape Key Pressed Down")
            ESC_KEY_PRESSED = 1

    # Keypress Up Event
    if key_event.type == pygame.KEYUP:
        # Left Arrow Key up
        if key_event.key == pygame.K_LEFT:
            print("LOG: Left Arrow Key Released")
            LEFT_ARROW_KEY_PRESSED = 0
        # Right Arrow Key up
        if key_event.key == pygame.K_RIGHT:
            print("LOG: Right Arrow Key Released")
            RIGHT_ARROW_KEY_PRESSED = 0
        # Up Arrow Key up
        if key_event.key == pygame.K_UP:
            print("LOG: Up Arrow Key Released")
            UP_ARROW_KEY_PRESSED = 0
        # Down Arrow Key up
        if key_event.key == pygame.K_DOWN:
            print("LOG: Down Arrow Key Released")
            DOWN_ARROW_KEY_PRESSED = 0
        # A Key up
        if key_event.key == pygame.K_a:
            print("LOG: A Key Released")
            A_KEY_PRESSED = 0
        # D Key up
        if key_event.key == pygame.K_d:
            print("LOG: D Key Released")
            D_KEY_PRESSED = 0
        # W Key up
        if key_event.key == pygame.K_w:
            print("LOG: W Key Released")
            W_KEY_PRESSED = 0
        # S Key up
        if key_event.key == pygame.K_s:
            print("LOG: S Key Released")
            S_KEY_PRESSED = 0
        # Space Bar up
        if key_event.key == pygame.K_SPACE:
            print("LOG: Space Bar Released")
            SPACE_BAR_PRESSED = 0
        # Enter Key up ("Carriage RETURN key" from old typewriter lingo)
        if key_event.key == pygame.K_RETURN:
            print("LOG: Enter Key Released")
            ENTER_KEY_PRESSED = 0
        # Esc Key up
        if key_event.key == pygame.K_ESCAPE:
            print("LOG: Escape Key Released")
            ESC_KEY_PRESSED = 0


# main game loop begins
while running:

    # background
    window.fill((0, 0, 0))

    # register events
    for event in pygame.event.get():
        # Quit Event
        if event.type == pygame.QUIT:
            running = False
        # Keyboard Events
        key_logger(event)

    # render the display
    pygame.display.update()
