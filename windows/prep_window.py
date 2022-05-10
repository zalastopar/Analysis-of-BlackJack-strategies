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


    if game.sim >0: # Button Next
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
    elif width - 955 + 300 + 40 <= mouse[0] <= width - 955 + 300 + 40 + 300 and height - 200 <= mouse[1] <= height - 200 + 80 and game.sim == 1: #and game.balance >0: # select num of simulations
        game.balance = game.balance + float(box.text)
        game.initial_balance = game.balance + float(box.text)
        box.text = ''
        box.txt_surface = box.text_font.render('', True, PINK)
        game.shuffle_deck()
        game.position = 3 

    elif width - 955 + 300 + 40 <= mouse[0] <= width - 955 + 300 + 40 + 300 and height - 200 <= mouse[1] <= height - 200 + 80 and box.text != '' and float(box.text) > 0 and game.sim == 0: # start playing
        game.balance = game.balance + float(box.text)
        game.initial_balance = game.balance + float(box.text)
        box.text = ''
        box.txt_surface = box.text_font.render('', True, PINK)
        game.shuffle_deck()
        game.position = 4 
                

    


def bet_window_sim(game, sim_box, deal_box): # game.position = 3
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Balance
    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Deposit your balance: ', TRUE, DARKPINK)
    second = text_font.render(str(game.balance), TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-700))
    gameDisplay.blit(second, (width - 600, height-700))

    # Number of simulations
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Number of dealings: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-600))

    # Number of simulations
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Number of simulations: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-400))

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)

    # Back and Next button
    b = classes.Button([width - 955, height - 200], 'Back', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)

    b = classes.Button([width - 955 + 300 + 40, height - 200], 'Next', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)
    
    # Error
    if sim_box.napaka == 3:
        print_error('Your amount must be an integer!', [width - 600, height-600 + 70], 28, DARKPINK)

    if deal_box.napaka == 3:
        print_error('Your amount must be an integer!', [width - 600, height-400 + 70], 28, DARKPINK)

    # Create textbox
    deal_box.update()
    deal_box.draw(gameDisplay)

    sim_box.update()
    sim_box.draw(gameDisplay)


def simulation_buttons(game, mouse, sim_box, deal_box): 

    #if the mouse is clicked on the button smth happens:
    if width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
        game.balance = 0
        game.position = 1
    elif width - 955 <= mouse[0] <= width - 955 + 300 and height - 200 <= mouse[1] <= height - 200 + 80: # select deposit amount again
        game.balance = 0
        game.position = 2
    elif width - 955 + 300 + 40 <= mouse[0] <= width - 955 + 300 + 40 + 300 and height - 200 <= mouse[1] <= height - 200 + 80 and sim_box.text != '' and deal_box.text != '' and int(sim_box.text) > 0 and int(deal_box.text) > 0: # next 
        game.sim = int(sim_box.text)
        game.num_dealings = int(deal_box.text)
        game.position = '3a'


    pygame.display.update()



def select_strategy_window(game, strat_buttons): # game.position = '3a'
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    '''
    # Balance
    text_font = pygame.font.SysFont('Bungee', 50)
    first = text_font.render('Deposit your balance: ', TRUE, DARKPINK)
    second = text_font.render(str(game.balance), TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-700))
    gameDisplay.blit(second, (width - 600, height-700))

    # Number of simulations
    text_font = pygame.font.SysFont('Bungee', 50)
    first = text_font.render('Number of dealings: ', TRUE, DARKPINK)
    second = text_font.render(str(game.num_dealings), TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-650))
    gameDisplay.blit(second, (width - 600, height-650))

    # Number of simulations
    text_font = pygame.font.SysFont('Bungee', 50)
    first = text_font.render('Number of simulations: ', TRUE, DARKPINK)
    second = text_font.render(str(game.sim), TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-600))
    gameDisplay.blit(second, (width - 600, height-600))
    '''

    # Select betting strategy
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Select betting strategy: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-700))
    strat_buttons.draw()

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)

    # Back and Play button
    b = classes.Button([width - 955, height - 200], 'Back', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)

    b = classes.Button([width - 955 + 300 + 40, height - 200], 'Play', LIGHTTEAL, PINK, DARKPINK, [300, 80], True)
    b.create(gameDisplay, 70)

def strategy_buttons(game, mouse, strat): ################## rabimo se eno umesno

    #if the mouse is clicked on the button smth happens:
    if width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
        game.strategy = ''
        game.sim = 0
        game.num_dealings = 0
        game.balance = 0
        game.position = 1
    elif width - 955 <= mouse[0] <= width - 955 + 300 and height - 200 <= mouse[1] <= height - 200 + 80: # select deposit amount again
        game.strategy = ''
        game.balance = 0
        game.position = 2
    elif width - 955 + 300 + 40 <= mouse[0] <= width - 955 + 300 + 40 + 300 and height - 200 <= mouse[1] <= height - 200 + 80 and game.strategy != '':  # play 
        game.position = 4
    # color the buttons
    elif width - 1300 <= mouse[0] <= width - 1300 + 500 and height - 600 <= mouse[1] <=  height - 600 + 80: # paroli
        strat.activate_button('paroli')
        game.strategy = 'paroli'
    elif width - 1300 + 500 + 40 <= mouse[0] <= width - 1300 + 500 + 500 + 40 and height - 600 <= mouse[1] <=  height - 600 + 80: # 1326
        strat.activate_button('1326')
        game.strategy = '1326'
    elif width - 1300 <= mouse[0] <= width - 1300 + 500 and height - 600 + 100 <= mouse[1] <=  height - 600 + 80 + 100: # rev_lab
        strat.activate_button('rev_lab')
        game.strategy = 'rev_lab'
    elif width - 1300 + 500 + 40 <= mouse[0] <= width - 1300 + 500 + 500 + 40 and height - 600 + 100 <= mouse[1] <=  height - 600 + 80 + 100: # increase
        strat.activate_button('increase')
        game.strategy = 'increase'
    elif width - 1300 <= mouse[0] <= width - 1300 + 500 and height - 600 + 200 <= mouse[1] <=  height - 600 + 80 + 200: # counting
        strat.activate_button('counting')
    elif width - 1300 + 500 + 40 <= mouse[0] <= width - 1300 + 500 + 500 + 40 and height - 600 + 200 <= mouse[1] <=  height - 600 + 80 + 200: # martingale
        strat.activate_button('martingale')
        game.strategy = 'martingale'
    elif width - 1300 <= mouse[0] <= width - 1300 + 500 and height - 600 + 300 <= mouse[1] <=  height - 600 + 80 + 300: # oscar
        strat.activate_button('oscar')
        game.strategy = 'oscar'
    elif width - 1300 + 500 + 40 <= mouse[0] <= width - 1300 + 500 + 500 + 40 and height - 600 + 300 <= mouse[1] <=  height - 600 + 80 + 300: # lab
        strat.activate_button('lab')
        game.strategy = 'lab'
    

    pygame.display.update()