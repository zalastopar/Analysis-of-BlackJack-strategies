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

def pre_ending(hand, game): # game.position = 11
    game.balance = game.balance + hand.winnings*hand.bet
    game.position = 12
    hand.player_hand = []
    hand.dealer_hand = []

def cash_out(event, game, mouse):  # game.position = 12
    '''Cash out window. PLayer can cash out or play again'''

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))
    game.balance = game.balance + 100
    # New balance
    text_font = pygame.font.SysFont('Bungee', 100)
    text_surface = text_font.render('Your new balance is ' + str(game.balance), True, DARKPINK)
    w = text_surface.get_width()
    h = text_surface.get_height()

    first = text_font.render('Your new balance is ' + str(game.balance), TRUE, DARKPINK)
    gameDisplay.blit(first, ((width - w)/2, height - 650))

    # Cash out
    b = classes.Button([width/2 - 20-300, height - 500], 'Cash out', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)
    # Add on
    b = classes.Button([width/2 + 20, height - 500], 'Play again', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)

    mouse = pygame.mouse.get_pos()
    # Clicking buttons

    if event.type == pygame.MOUSEBUTTONDOWN:

        #if the mouse is clicked on the button smth happens:
        if  width/2 - 20-300 <= mouse[0] <= width/2 - 20 and height - 500 <= mouse[1] <= height - 500 + 80: # Cash out
            game.position = 13
        elif width/2 + 20 <= mouse[0] <= width/2 + 20 + 300 and height - 500 <= mouse[1] <= height - 500 + 80: # Add on
            game.position = 4

def finnish(event, game, mouse): # game.position = 13
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

    mouse = pygame.mouse.get_pos()
    # Clicking buttons

    if event.type == pygame.MOUSEBUTTONDOWN:

        #if the mouse is clicked on the button smth happens:
        if  width/2 - 20-300 <= mouse[0] <= width/2 - 20 and height - 500 <= mouse[1] <= height - 500 + 80: # Cash out
            game.position = 1
        elif width/2 + 20 <= mouse[0] <= width/2 + 20 + 300 and height - 500 <= mouse[1] <= height - 500 + 80: # Add on
            pygame.quit()