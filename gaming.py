from pickle import TRUE
import pygame
from pygame.locals import *
import time
import sys
import pygame_textinput
import os


# import other python files
# windows
import windows.menu_window as menu_window
import windows.prep_window as prep_window
import windows.end_window as end_window

import windows.table as table

# functions
from functions.classes import *
from functions.cards import *


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
OFFWHITE = (241, 235, 219)
WRITING = (206, 183, 127)

 
# Setup a 1600x900 pixel display with caption
width = 1600
height = 900
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(PINK)
pygame.display.set_caption("BlackJack Table")
 

# Windows
# 1 - menu
# 2 - prep
# 3 - prep and sim
# 4 - table bet
# 5 - table - first round
# 6 - table - add buttons
# 7 - table - add player card
# 8 - table - add dealer cards
# 9 - table - split
# 10 - table who wins
# 12 - cash out
# 13 - finnish


# When menu player deletes 

mygame = Game(0, 1, False, 0, {})
myhand = Hand(0, [], [], 0, False, False, [], 0, 0)

balance_box = classes.InputBox(width - 600, height-695, 300, 70, '', 100)
bet_box = classes.InputBox(width/2 + 100, height - 490, 300, 70, '', 100, [LIGHTTEAL, DARKTEAL, OFFWHITE])

napaka = False

def view(position):
    if position == 1:
        menu_window.menu()
    elif position == 2:
        prep_window.bet_window(mygame, balance_box)
    elif position == 3:   
        pass                               ############ simulation - bomo naredili pol
        #prep_window.bet_window_sim(events, mygame)

    elif position == 4:
        table.place_bet(myhand, mygame, bet_box)
    elif position == 5:
        table.dealing(myhand, mygame)
    elif position == 6:
        table.adding_buttons(myhand, mygame)
    elif position == 8:
        table.add_dealer_cards(myhand, mygame)
    elif position == 9:
        table.split(myhand, mygame)
    elif position == 10:
        table.winner(myhand, mygame)
    elif position == 12:
        end_window.cash_out(mygame)
    elif position == 13:
        end_window.finnish(mygame)





# Beginning Game Loop
while True:
    view(mygame.position)
    pygame.display.update()
    events = pygame.event.get()
    position = mygame.position
    mouse = pygame.mouse.get_pos()



    for event in events:


        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if position == 1:
                menu_window.menu_buttons(mygame, mouse)
            elif position == 2:
                prep_window.prep_buttons(mygame, mouse, balance_box)   
            elif position == 3:
                pass
            elif position == 4:
                table.place_bet_buttons(mygame, mouse, myhand, bet_box)
            elif position == 6:
                table.dealing_buttons(mygame, mouse, myhand)
            elif position == 10:
                table.winner_buttons(mygame, mouse, myhand)
            elif position == 12:
                end_window.cash_out_buttons(mygame, mouse)
            elif position == 13:
                end_window.finnish_buttons(mygame, mouse)
        if position == 2:
                balance_box.handle_event(event, gameDisplay, mygame)
        elif position ==4:
                bet_box.handle_event(event, gameDisplay, mygame, True)



            
