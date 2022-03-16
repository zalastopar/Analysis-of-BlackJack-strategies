from pickle import TRUE
import pygame
import pygame_textinput

import pygame_textinput
import pygame.locals as pl

import functions.classes as classes

pygame.init()

 
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


# Preparations for textbox
textinput = pygame_textinput.TextInputVisualizer()


def print_error(txt, pos, size, col):
    text_font = pygame.font.SysFont('Bungee', size)
    warning = text_font.render(txt, TRUE, col)
    gameDisplay.blit(warning, pos)



def bet_window(game, box): # game.position = 2
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))
    

    # Place your money
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Deposit your balance: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-700))


    if game.simulation >0: # Button Next
        b = classes.Button([width - 955, height - 200], 'Back', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
        b.create(gameDisplay, 70)

        b = classes.Button([width - 955 + 300 + 40, height - 200], 'Next', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
        b.create(gameDisplay, 70)


    else: #  Button Play
        b = classes.Button([width - 955, height - 200], 'Back', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
        b.create(gameDisplay, 70)

        b = classes.Button([width - 955 + 300 + 40, height - 200], 'Play', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
        b.create(gameDisplay, 70)

    if box.napaka == 1:
        print_error('Your amount must be a number!', [width - 600, height-695 + 70], 28, DARKPINK)


    # Create textbox
    box.update()
    box.draw(gameDisplay)



    pygame.display.update()

def prep_buttons(game, mouse, box):

    if width - 955 <= mouse[0] <= width - 955 + 300 and height - 200 <= mouse[1] <= height - 200 + 80: # go back (to Menu)
        game.position = 1 
    elif width - 955 + 300 + 40 <= mouse[0] <= width - 955 + 300 + 40 + 300 and height - 200 <= mouse[1] <= height - 200 + 80 and game.simulation >0: #and game.balance >0: # select num of simulations
        game.position = 4 ############# 3 
    elif width - 955 + 300 + 40 <= mouse[0] <= width - 955 + 300 + 40 + 300 and height - 200 <= mouse[1] <= height - 200 + 80 and box.text != '' and float(box.text) > 0 and game.simulation == 0: # start playing
        game.balance = game.balance + float(box.text)
        box.text = ''
        box.txt_surface = box.text_font.render('', True, PINK)
        game.shuffle_deck()
        game.position = 4 
                

    

'''
def bet_window_sim(events, game): # game.position = 3
    # Money placed
    pygame.draw.rect(gameDisplay, PINK, (width - 600, height-700, 100, 100))

    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Deposit your balance: ', TRUE, DARKPINK)
    second = text_font.render(str(game.balance), TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-700))
    gameDisplay.blit(second, (width - 600, height-700))

    # Number of simulations
    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Insert number of simulations: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-500))
    position = [width - 750, height-500, 100, 50]
    ######################################game.simulation = input(events, position, 0)

    # Select playing strategy
    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Select playing strategy: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-400))

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)

    # Back and Play button
    b = classes.Button([width - 955, height - 200], 'Back', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)

    b = classes.Button([width - 955 + 300 + 40, height - 200], 'Play', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)


    # Clicking buttons
    mouse = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the button smth happens:
            if width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
                game.position = 1
            elif width - 955 <= mouse[0] <= width - 955 + 300 and height - 200 <= mouse[1] <= height - 200 + 80: # select deposit amount again
                game.position = 2
            elif width - 955 + 300 + 40 <= mouse[0] <= width - 955 + 300 + 40 + 300 and height - 200 <= mouse[1] <= height - 200 + 80: # start game
                game.position = 4


    pygame.display.update()
'''