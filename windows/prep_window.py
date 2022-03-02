from pickle import TRUE
import pygame
import pygame_textinput

import pygame_textinput
import pygame.locals as pl


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


def input(events, position, typeof):

    base_font = pygame.font.Font(None, 30)
    
    #gameDisplay.fill(PINK)

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




def bet_window(events, game):
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))
    

    # Place your money
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Deposit your balance: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-700))
    position = [width - 600, height-695, 100, 50]
    balance = input(events, position, 0.0)
    game.balance = balance

    mouse = pygame.mouse.get_pos()
    if game.simulation >0: # Button Next
        pygame.draw.rect(gameDisplay, TEAL, (width - 955, height - 200, 200, 100))
        pygame.draw.rect(gameDisplay, TEAL, (width - 955 + 200 + 20, height - 200, 200, 100))
        

        if  width - 955 <= mouse[0] <= width - 955 + 200 and height - 200 <= mouse[1] <= height - 100 + 100:
            pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 955, height - 200, 200, 100))
        elif  width - 955 + 200 + 20 <= mouse[0] <= width - 955 + 200 + 20 + 200 and height - 200 <= mouse[1] <= height - 200 + 100:
            pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 955 + 200 + 20, height - 200, 200, 100))


        pygame.draw.rect(gameDisplay, DARKTEAL, (width - 955 + 200 + 20, height - 200, 200, 100), 2)
        pygame.draw.rect(gameDisplay, DARKTEAL, (width - 955, height - 200, 200, 100), 2)

        text_font = pygame.font.SysFont('Bungee', 80)
        first = text_font.render('Back', TRUE, DARKTEAL)
        second = text_font.render('Next', TRUE, DARKTEAL)
        gameDisplay.blit(first, (width - 955 + 35, height - 200 + 25))
        gameDisplay.blit(second, (width - 955 + 200 + 20 + 45, height - 200 + 25))

    else: #  Button Play
        pygame.draw.rect(gameDisplay, TEAL, (width - 955, height - 200, 200, 100))
        pygame.draw.rect(gameDisplay, TEAL, (width - 955 + 200 + 20, height - 200, 200, 100))
        

        if  width - 955 <= mouse[0] <= width - 955 + 200 and height - 200 <= mouse[1] <= height - 100 + 100:
            pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 955, height - 200, 200, 100))
        elif  width - 955 + 200 + 20 <= mouse[0] <= width - 955 + 200 + 20 + 200 and height - 200 <= mouse[1] <= height - 200 + 100:
            pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 955 + 200 + 20, height - 200, 200, 100))


        pygame.draw.rect(gameDisplay, DARKTEAL, (width - 955 + 200 + 20, height - 200, 200, 100), 2)
        pygame.draw.rect(gameDisplay, DARKTEAL, (width - 955, height - 200, 200, 100), 2)

        text_font = pygame.font.SysFont('Bungee', 80)
        first = text_font.render('Back', TRUE, DARKTEAL)
        second = text_font.render('Play', TRUE, DARKTEAL)
        gameDisplay.blit(first, (width - 955 + 35, height - 200 + 25))
        gameDisplay.blit(second, (width - 955 + 200 + 20 + 45, height - 200 + 25))

    '''
    # Menu button
    if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35:
        pygame.draw.rect(gameDisplay, LIGHTPINK, ( width - 65, 5, 65, 30))
    text_font = pygame.font.SysFont('Bungee', 30)
    first = text_font.render('Menu', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 60, 10))
    '''

    # Clicking buttons
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the button smth happens:
            if width - 955 <= mouse[0] <= width - 955 + 200 and height - 200 <= mouse[1] <= height - 100 + 100: 
                game.position = 1 # go back (to Menu)
            elif width - 955 + 200 + 20 <= mouse[0] <= width - 955 + 200 + 20 + 200 and height - 200 <= mouse[1] <= height - 200 + 100 and game.simulation >0 and game.balance >0:
                game.position = 3 # select num of simulations
            elif width - 955 + 200 + 20 <= mouse[0] <= width - 955 + 200 + 20 + 200 and height - 200 <= mouse[1] <= height - 200 + 100 and game.simulation == 0 and game.balance >0:
                game.position = 4 # start playing
                

    pygame.display.update()



def bet_window_sim(events, game):
    # Money placed
    pygame.draw.rect(gameDisplay, PINK, (width - 600, height-700, 100, 50))

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
    game.simulation = input(events, position, 0)

    # Select playing strategy
    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Select playing strategy: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-400))

    # Menu button
    mouse = pygame.mouse.get_pos()
    if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35:
        pygame.draw.rect(gameDisplay, LIGHTPINK, ( width - 65, 5, 65, 30))
    text_font = pygame.font.SysFont('Bungee', 30)
    first = text_font.render('Menu', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 60, 10))

    # Back and Play button
    pygame.draw.rect(gameDisplay, TEAL, (width - 955, height - 200, 200, 100))
    pygame.draw.rect(gameDisplay, TEAL, (width - 955 + 200 + 20, height - 200, 200, 100))
    
    if  width - 955 <= mouse[0] <= width - 955 + 200 and height - 200 <= mouse[1] <= height - 100 + 100:
        pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 955, height - 200, 200, 100))
    elif  width - 955 + 200 + 20 <= mouse[0] <= width - 955 + 200 + 20 + 200 and height - 200 <= mouse[1] <= height - 200 + 100:
        pygame.draw.rect(gameDisplay, LIGHTTEAL, (width - 955 + 200 + 20, height - 200, 200, 100))

    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 955 + 200 + 20, height - 200, 200, 100), 2)
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 955, height - 200, 200, 100), 2)

    text_font = pygame.font.SysFont('Bungee', 80)
    first = text_font.render('Back', TRUE, DARKTEAL)
    second = text_font.render('Play', TRUE, DARKTEAL)
    gameDisplay.blit(first, (width - 955 + 35, height - 200 + 25))
    gameDisplay.blit(second, (width - 955 + 200 + 20 + 45, height - 200 + 25))


    # Clicking buttons
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the button smth happens:
            if width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
                game.position = 1
            elif width - 955 <= mouse[0] <= width - 955 + 200 and height - 200 <= mouse[1] <= height - 100 + 100: # select deposit amount again
                game.position = 2
            elif width - 955 + 200 + 20 <= mouse[0] <= width - 955 + 200 + 20 + 200 and height - 200 <= mouse[1] <= height - 200 + 100: # gp play
                game.position = 4

    pygame.display.update()