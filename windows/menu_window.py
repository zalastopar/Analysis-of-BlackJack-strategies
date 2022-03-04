from pickle import TRUE
import pygame
from pygame.locals import *


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
def menu():

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Title
    text_font = pygame.font.SysFont('Bungee', 100)
    text_surface = text_font.render('BlackJack', True, DARKPINK)
    w = text_surface.get_width()
    h = text_surface.get_height()
    first = text_font.render('BlackJack', TRUE, DARKPINK)

    gameDisplay.blit(first, ((width - w)/2, height - 650))

    # Play
    b = classes.Button([width/2 - 20-400, height - 500], 'Play', LIGHTTEAL, PINK, DARKPINK, [400, 80], True)
    b.create(gameDisplay, 70)
    # Quit
    b = classes.Button([width/2 + 20, height - 500], 'Play with help', LIGHTTEAL, PINK, DARKPINK, [400, 80], True)
    b.create(gameDisplay, 70)

    # menu
    b = classes.Button([width/2 - 20-400, height - 500 + 40 + 80], 'Simulate', LIGHTTEAL, PINK, DARKPINK, [400, 80], True)
    b.create(gameDisplay, 70)
    # Quit
    b = classes.Button([width/2 + 20, height - 500 + 40 + 80], 'Quit', LIGHTTEAL, PINK, DARKPINK, [400, 80], True)
    b.create(gameDisplay, 70)

    pygame.display.update()



def menu_buttons(game, mouse):
    #if the mouse is clicked on the button smth happens:
    if width/2 - 20-400 <= mouse[0] <= width/2 - 20-400 + 400 and height - 500 <= mouse[1] <= height - 500 + 80: # Normal game
        game.position = 2
        game.help = 0
    elif width/2 + 20 <= mouse[0] <= width/2 + 20+ 400 and height - 500 <= mouse[1] <= height - 500 + 80: # Game with help
        game.position = 2
        game.help = 1
    elif width/2 - 20-400 <= mouse[0] <= width/2 - 20-400 + 400 and height - 500 + 40 + 80 <= mouse[1] <= height - 500 + 40 + 80 + 80: # Simulations
        game.position = 2
        game.simulation = 1
    elif width/2 + 20 <= mouse[0] <= width/2 + 20 + 400 and height - 500 + 40 + 80 <= mouse[1] <= height - 500 + 40 + 80 + 80: # Quit
        pygame.quit()

