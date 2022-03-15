from pickle import TRUE
import pygame
from pygame.locals import *
import time
import sys
import pygame_textinput

# functions
import functions.classes as classes
import functions.cards as cards

# Setting up color objects
PINK = (242,233,222)
DARKPINK = (222,93,131)#(212,112,162)
LIGHTPINK = (239,187,204)

TEAL = (221,173,175)
DARKTEAL = (216,105,105)
LIGHTTEAL = (239,187,204)

OFFWHITE = (242,233,222)
WRITING = (255,153,153)

# Setup a 1600x900 pixel display with caption
width = 1600
height = 900
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(PINK)
pygame.display.set_caption("BlackJack Table")



def cash_out(game):  # game.position = 12
    '''Cash out window. PLayer can cash out or play again'''

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # New balance
    text_font = pygame.font.SysFont('Bungee', 100)
    text_surface = text_font.render('Your new balance is ' + str(game.balance), True, DARKPINK)
    w = text_surface.get_width()
    h = text_surface.get_height()

    first = text_font.render('Your new balance is ' + str(game.balance), TRUE, DARKPINK)
    gameDisplay.blit(first, ((width - w)/2, height - 650))

    # Cash out
    b = classes.Button([width/2 - 300/2 - 40 - 300, height - 500], 'Cash out', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)
    # Play again
    b = classes.Button([width/2 - 300/2, height - 500], 'Play again', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)
    # Add on
    b = classes.Button([width/2 + 300/2 + 40, height - 500], 'Add on', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)


def cash_out_buttons(game,mouse):

    if  width/2 - 300/2 - 40 - 300 <= mouse[0] <= width/2 - 300/2 - 40  and height - 500 <= mouse[1] <= height - 500 + 80: # Cash out
        game.position = 13
    elif width/2 - 300/2 <= mouse[0] <= width/2 - 300/2 + 300 and height - 500 <= mouse[1] <= height - 500 + 80 and game.balance > 0: # Play again
        game.position = 4
    elif width/2 + 300/2 + 40 <= mouse[0] <= width/2 + 300/2 + 40 + 300 and height - 500 <= mouse[1] <= height - 500 + 80:
        game.position = 2
    

def finnish(game): # game.position = 13
    '''Window after cash out. Player can go on menu or leave game.'''

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Successful cash out
    text_font = pygame.font.SysFont('Bungee', 100)
    text_surface = text_font.render('You have successfully cashed out ' + str(game.balance) + '.', True, DARKPINK)
    w = text_surface.get_width()
    h = text_surface.get_height()
    first = text_font.render('You have successfully cashed out ' + str(game.balance) + '.', TRUE, DARKPINK)

    gameDisplay.blit(first, ((width - w)/2, height - 650))

    # Buttons
    # Menu
    b = classes.Button([width/2 - 20-300, height - 500], 'Menu', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)
    # Quit
    b = classes.Button([width/2 + 20, height - 500], 'Quit', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)


def finnish_buttons(game, mouse):

    if  width/2 - 20-300 <= mouse[0] <= width/2 - 20 and height - 500 <= mouse[1] <= height - 500 + 80: # Cash out
        game.balance = 0
        game.position = 1
        game.help = False
    elif width/2 + 20 <= mouse[0] <= width/2 + 20 + 300 and height - 500 <= mouse[1] <= height - 500 + 80: # Quit
        pygame.quit()
