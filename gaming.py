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
import windows.table_window as table_window
import windows.prep_window as prep_window
import windows.end_window as end_window
import windows.proba as proba
import windows.table as table_w

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
# 11 - prefinnish
# 12 - cash out
# 13 - finnish


# When menu player deletes 

mygame = Game(0, 1, 0, 100, {})
myhand = Hand(0, [], [], False, False, False, 0)

 

def view(position):
    if position == 1:
        menu_window.menu()
    elif position == 2:
        prep_window.bet_window(mygame)

    elif position == 3:   
        pass                               ############ simulation - bomo naredili pol
        #prep_window.bet_window_sim(events, mygame)

    elif position == 4:
        table_w.place_bet(myhand, mygame)
    
    elif position == 5:
        table_w.dealing(myhand, mygame)
    elif position == 6:
        table_w.adding_buttons(myhand, mygame)
    elif position == 8:
        table_w.add_dealer_cards(myhand, mygame)
    elif position == 9:
        pass
    elif position == 10:
        table_w.winner(myhand, mygame)
    '''
    elif position == 11:
        end_window.pre_ending(myhand, mygame)
    elif position == 12:
        end_window.cash_out(mygame)
    elif position == 13:
        end_window.finnish(mygame)
    '''


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
                prep_window.prep_buttons(mygame, mouse)
                myhand = Hand(0, [], [], False, False, False, 0)
            elif position == 3:
                pass
            elif position == 4:
                table_w.place_bet_buttons(mygame, mouse, myhand)
            elif position == 6:
                table_w.dealing_buttons(mygame, mouse, myhand)
            elif position == 10:
                table_w.winner_buttons(mygame, mouse, myhand)

            
            '''if position == 11:
                view = proba.pre_ending(myhand, mygame)
            elif position == 12:
                view = proba.cash_out(event, mygame, mouse)
            elif position == 13:
                view = proba.finnish(event, mygame, mouse)
            '''