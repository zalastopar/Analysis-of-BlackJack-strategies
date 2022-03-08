from pickle import TRUE
import pygame
import pygame_textinput

import pygame_textinput
import pygame.locals as pl

import functions.classes as classes

pygame.init()

 
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


# Preparations for textbox
textinput = pygame_textinput.TextInputVisualizer()


def print_error(txt, pos, size, col):
    text_font = pygame.font.SysFont('Bungee', size)
    warning = text_font.render(txt, TRUE, col)
    gameDisplay.blit(warning, pos)



def input(events, position, typeof):

    base_font = pygame.font.Font(None, 40)

    txt = textinput.value

    # Make text look pretty
    textinput.font_color = WHITE
    textinput.cursor_color = DARKPINK
    text_surface = base_font.render(txt, True, DARKPINK)

    # Change rect size
    s = text_surface.get_width()
    position[2] = max(100, s + s/3)
    pygame.draw.rect(gameDisplay, LIGHTPINK, position)

    
    # Only integers or floats allowed and save value
    money = 0

    if isinstance(typeof, int): # we want int
        try:
            money = int(txt)
            # Delete warning
            text_font = pygame.font.SysFont('Bungee', 30)
            warning = text_font.render('You amount must be an integer!', TRUE, WHITE)
            pygame.draw.rect(gameDisplay, PINK, [position[0], position[1] + position[3], 10+ warning.get_width(), position[3]])
        except:
            # Write warning
            text_font = pygame.font.SysFont('Bungee', 30)
            warning = text_font.render('Your amount must be an integer!', TRUE, WHITE)
            gameDisplay.blit(warning, (position[0], position[1] + position[3]))

            # Set input to ''
            textinput.value = ''

    else: # we want float
        try:
            money = float(txt)
            # Delete warning
            text_font = pygame.font.SysFont('Bungee', 30)
            warning = text_font.render('Your amount must be a number!', TRUE, WHITE)
            pygame.draw.rect(gameDisplay, PINK, [position[0], position[1] + position[3], 10+ warning.get_width(), position[3]])
        except:
            # Write warning
            text_font = pygame.font.SysFont('Bungee', 30)
            warning = text_font.render('Your amount must be a number!', TRUE, WHITE)
            gameDisplay.blit(warning, (position[0], position[1] + position[3]))

            # Set input to ''
            textinput.value = ''


    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    gameDisplay.blit(textinput.surface, (position[0], position[1] + position[3]/3))


    return(money)




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
        game.balance = float(box.text)
        box.text = ''
        box.txt_surface = box.text_font.render('', True, PINK)
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