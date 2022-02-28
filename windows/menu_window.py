from pickle import TRUE
import pygame
from pygame.locals import *
'''
import time
import sys
import pygame_textinput
'''

# Import functions
import functions.classes as classes


# Setting up color objects
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (60,179,113)
PINK = (216, 0, 115)
TEAL = (0, 128, 128)
DARKPINK = (102, 0, 51)
DARKTEAL = (0,73,83)
LIGHTTEAL = (95,158,160)
LIGHTPINK = (250, 12, 139)

# Setup a 1600x900 pixel display with caption
width = 1600
height = 900
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(PINK)
pygame.display.set_caption("BlackJack Table")

# Create menu
def menu(events, game):

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create buttons
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600, 400, 100))
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600 + 110, 400, 100))
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600 + 220, 400, 100))
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600 + 330, 400, 100))

    # Show were is the mouse (buttons gets lighter)
    mouse = pygame.mouse.get_pos()
    if  width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 <= mouse[1] <= height - 600 + 100:
        pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 1000, height - 600, 400, 100))
    elif  width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 + 110 <= mouse[1] <= height - 600 + 100 + 110:
        pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 1000, height - 600 + 110, 400, 100))
    elif  width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 +220 <= mouse[1] <= height - 600 + 100 + 220:
        pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 1000, height - 600 + 220, 400, 100))
    elif  width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 + 330 <= mouse[1] <= height - 600 + 100 + 330:
        pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 1000, height - 600 + 330, 400, 100))

    # Make button border
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1000, height - 600, 400, 100), 2)
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1000, height - 600 + 110, 400, 100), 2)
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1000, height - 600 + 220, 400, 100), 2)
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1000, height - 600 + 330, 400, 100), 2)

    # Define font for title and make title
    title_font = pygame.font.SysFont('Bungee', 150)
    title = title_font.render('BlackJack', TRUE, DARKPINK)
    gameDisplay.blit(title, (width-1000-60, height - 600 - 200))

    # Define button text
    text_font = pygame.font.SysFont('Bungee', 80)
    first = text_font.render('Play', TRUE, DARKPINK)
    second = text_font.render('Play with help', TRUE, DARKPINK)
    third = text_font.render('Simulate', TRUE, DARKPINK)
    fourth = text_font.render('Quit', TRUE, DARKPINK)
    
    gameDisplay.blit(first, (width-1000 + 135, height - 600 + 25))
    gameDisplay.blit(second, (width-1000 + 10, height - 600 + 25 + 110))
    gameDisplay.blit(third, (width-1000 + 85, height - 600 + 25 + 220))
    gameDisplay.blit(fourth, (width-1000 + 135, height - 600 + 25 + 330))

    # Clicking buttons
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #if the mouse is clicked on the button smth happens:
            if width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 <= mouse[1] <= height - 600 + 100: # Normal game
                game.position = 2
                game.help = 0
            elif width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 + 110 <= mouse[1] <= height - 600 + 100 + 110: # Game with help
                game.position = 2
                game.help = 1
            elif width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 +220 <= mouse[1] <= height - 600 + 100 + 220: # Simulations
                game.position = 2
                game.simulation = 1
            elif width - 1000 <= mouse[0] <= width - 1000 + 400 and height - 600 + 330 <= mouse[1] <= height - 600 + 100 + 330: # Quit
                pygame.quit()


    pygame.display.update()
