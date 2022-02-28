from pickle import TRUE
import pygame
from pygame.locals import *
import time
import sys
import pygame_textinput

# functions
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



# Preparations for textbox
textinput = pygame_textinput.TextInputVisualizer()


def input(events, position, player):
    
    #gameDisplay.fill(PINK)

    txt = textinput.value

    # Make text look pretty
    textinput.font_color = WHITE
    textinput.cursor_color = DARKTEAL
    
    # Only floats allowed lower than your deposit amount and save value 
    money = 0

    try:
        money = float(txt)
        # Delete warning
        text_font = pygame.font.SysFont('Bungee', 30)
        warning = text_font.render('Your amount must be a number!', TRUE, DARKTEAL)
        pygame.draw.rect(gameDisplay, TEAL, [position[0], position[1] + position[3], 10+ warning.get_width(), position[3]])
        
        if player.balance < money:
            # Write warning
            text_font = pygame.font.SysFont('Bungee', 30)
            warning = text_font.render("You can't bet more than you have!", TRUE, DARKTEAL)
            gameDisplay.blit(warning, (position[0], position[1] + position[3]))
            player.bet = 0.0
            
        else:
            player.bet = money

    except:
        # Write warning
        text_font = pygame.font.SysFont('Bungee', 30)
        warning = text_font.render('Your amount must be a number!', TRUE, DARKTEAL)
        gameDisplay.blit(warning, (position[0], position[1] + position[3]))

        # Set input to ''
        textinput.value = ''


    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    gameDisplay.blit(textinput.surface, (position[0], position[1] + position[3]/3))




# Create table
def table(events, player, game):
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create table
    pygame.draw.rect(gameDisplay, TEAL, (width - 1498.5, height - 850, width-200-3, height-100-3))
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5-2, height - 850-2, width-200, height-100), 10, 3)

    # Place your bet
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Place your bet:', TRUE, DARKTEAL)
    position = [width/2 + 100, height - 490, 100, 50]
    input(events, position, player)



    gameDisplay.blit(first, (width/2 - 500, height - 500))


    mouse = pygame.mouse.get_pos()

    # Balance
    text_font = pygame.font.SysFont('Bungee', 65)
    bet = text_font.render('Bet amount: ' + str(player.bet), TRUE, DARKTEAL)
    text_font = pygame.font.SysFont('Bungee', 50)

    balance = text_font.render('Balance: ' + str(player.balance), TRUE, DARKTEAL)

    gameDisplay.blit(bet, (width - 1498.5 + 15, height - 120 ))
    gameDisplay.blit(balance, (width - 1498.5 + 15, height - 120 - 40))

    # Bet button
    pygame.draw.rect(gameDisplay, LIGHTTEAL, (width/2 + 100, height - 400, 100, 50))
    if width/2 + 100 <= mouse[0] <= width/2 + 100 + 100 and height - 400 <= mouse[1] <= height - 400 + 50:
        pygame.draw.rect(gameDisplay, LIGHTPINK, (width/2 + 100, height - 400, 100, 50))
    pygame.draw.rect(gameDisplay, DARKTEAL, (width/2 + 100, height - 400, 100, 50), 2)

    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Bet', TRUE, DARKTEAL)
    gameDisplay.blit(first, (width/2 + 100 + 15, height - 400 + 8))

    # Menu button
    if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35:
        pygame.draw.rect(gameDisplay, LIGHTPINK, ( width - 65, 5, 65, 30))
    text_font = pygame.font.SysFont('Bungee', 30)
    first = text_font.render('Menu', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 60, 10))


    # Clicking buttons
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the button smth happens:
            if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
                game.position = 1
            elif width/2 + 100 <= mouse[0] <= width/2 + 100 + 100 and height - 400 <= mouse[1] <= height - 400 + 50 and player.bet > 0:
                game.position = 5
    

    pygame.display.update()


# dodaj gumbe glede na karte


    '''
    # Create buttons
    pygame.draw.rect(gameDisplay, PINK, (width - 955, height - 100, 150, 70))
    pygame.draw.rect(gameDisplay, PINK, (width - 955 + 160, height - 100, 150, 70))

    # Lighter whene mouse is on button
    mouse = pygame.mouse.get_pos()
    if  width - 955 <= mouse[0] <= width - 955 + 150 and height - 100 <= mouse[1] <= height - 100 + 70:
        pygame.draw.rect(gameDisplay, LIGHTPINK, (width - 955, height - 100, 150, 70))
    elif  width - 955 + 160 <= mouse[0] <= width - 955 + 160 + 150 and height - 100 <= mouse[1] <= height - 100 + 70:
        pygame.draw.rect(gameDisplay, LIGHTPINK, (width - 955 + 160, height - 100, 150, 70))


    # Create border
    pygame.draw.rect(gameDisplay, DARKPINK, (width - 955, height - 100, 150, 70), 5)
    pygame.draw.rect(gameDisplay, DARKPINK, (width - 955 + 160, height - 100, 150, 70), 5)

    # Define button text
    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Hit', TRUE, DARKPINK)
    second = text_font.render('Stand', TRUE, DARKPINK)

    gameDisplay.blit(first, (width - 955 + 45, height - 100 + 15))
    gameDisplay.blit(second, (width - 955 + +160 + 15, height - 100 + 15))

    # še double in split
    #pygame.draw.rect(gameDisplay, PINK, (width - 955 - 160, height - 100, 150, 70))
    #pygame.draw.rect(gameDisplay, PINK, (width - 955 + 160 + 160, height - 100, 150, 70))
    #pygame.draw.rect(gameDisplay, DARKPINK, (width - 955 - 160, height - 100, 150, 70), 5)
    #pygame.draw.rect(gameDisplay, DARKPINK, (width - 955 + 160 + 160, height - 100, 150, 70), 5)
    

    #text_font = pygame.font.SysFont('Bungee', 60)
    #third = text_font.render('Double', TRUE, DARKPINK)
    #fourth = text_font.render('Split', TRUE, DARKPINK)

    #gameDisplay.blit(third, (width - 955 - 160 + 3, height - 100 + 15))
    #gameDisplay.blit(fourth, (width - 955 + 160 + 160 + 30, height - 100 + 15))

    '''