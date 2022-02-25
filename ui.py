
from pickle import TRUE
import pygame
from pygame.locals import *
import time
import sys
import pygame_textinput



# Initialize program
pygame.init()

clock = pygame.time.Clock()

 
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
def menu_window():

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create buttons
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600, 400, 100))
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600 + 110, 400, 100))
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600 + 220, 400, 100))
    pygame.draw.rect(gameDisplay, TEAL, (width - 1000, height - 600 + 330, 400, 100))

    # Show were is the mouse
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

    # Define font for title
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


    pygame.display.update()

# Create table
def table_window():
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create table
    pygame.draw.rect(gameDisplay, TEAL, (width - 1498.5, height - 850, width-200-3, height-100-3))
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5-2, height - 850-2, width-200, height-100), 10, 3)

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


    # Balance
    text_font = pygame.font.SysFont('Bungee', 65)
    first = text_font.render('Bet amount:', TRUE, DARKTEAL)
    text_font = pygame.font.SysFont('Bungee', 50)
    second = text_font.render('Balance: ', TRUE, DARKTEAL)

    gameDisplay.blit(first, (width - 1498.5 + 15, height - 120 ))
    gameDisplay.blit(second, (width - 1498.5 + 15, height - 120 - 40))

    # Menu button
    if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35:
        pygame.draw.rect(gameDisplay, LIGHTPINK, ( width - 65, 5, 65, 30))
    text_font = pygame.font.SysFont('Bungee', 30)
    first = text_font.render('Menu', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 60, 10))

    pygame.display.update()


def bet_window():
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Place your bet
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Deposit your balance: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-700))

    # prostor kjer se vpise denar

    # Number of simulations
    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Insert number of simulations: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-500))

    # Select playing strategy
    text_font = pygame.font.SysFont('Bungee', 60)
    first = text_font.render('Select playing strategy: ', TRUE, DARKPINK)
    gameDisplay.blit(first, (width - 1400, height-400))





def deal_cards():
    pass



def text_box():
    pass



 
# Beginning Game Loop
while True:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    menu_window()
        

    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)



    









