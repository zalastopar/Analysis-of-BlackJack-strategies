
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

# functions
import functions.classes as classes



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
# 5 - table cards
# 6 - table cards double
# 7 - table cards split
# 8 - table result 

# When menu player deletes 

mygame = classes.Game(0, 4, 0, 10, {})
myhand = classes.Hand(5, [], [], 0)

 
# Beginning Game Loop
while True:

    pygame.display.update()
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    position = mygame.position
    if position == 1:
        table_window.simple_table(myhand, mygame)
        #menu_window.menu(events, mygame) 
    elif position == 2:
        prep_window.bet_window(events, mygame)
    elif position == 3:
        prep_window.bet_window_sim(events, mygame)
    elif position == 4:
        table_window.playing_game(myhand, mygame)
        #table_window.table(events, myhand, mygame)

    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)



    









