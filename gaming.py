from pickle import TRUE
import pygame
from pygame.locals import *

import sys
import pygame_textinput
import os


# import other python files
# windows
import windows.menu_window as menu_window
import windows.prep_window as prep_window
import windows.end_window as end_window
import windows.table_ai as table_ai

import windows.table as table

# functions
import functions.classes as classes
from functions.cards import *
import functions.strategies as strategies



# Initialize program
pygame.init()

clock = pygame.time.Clock()

 
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
 

# Windows
# 1 - menu
# 2 - prep
# 3 - prep and sim
# 4 - table bet
# 5 - table - first round
# 6 - table - add buttonst
# 7 - table - add player card
# 8 - table - add dealer cards
# 9 - table - split
# 10 - table who wins
# 12 - cash out
# 13 - finnish


# When menu player deletes 

mygame = classes.Game('', 0, 1, False, 0, 0, {}, 10, 1, 0, 1, {}, {}, {'data_0x': {}, 'data_3x': {}, 'data_5x': {}, 'data_10x': {}}, [], {}, {}, {})
myhand = classes.Hand(0, [], [], 0, False, False, [], 0, 0, [])
aihand = classes.Hand_ai(0, [], [], False, False, [], 0, 0, [])



# strategies
paroli = strategies.paroli(0, 0)
sys1326 = strategies.system1326(0, 0, 1)
revlab = strategies.reverse_lab(0, [], 0, 0)
onehalf = strategies.one_half_increase(0, 0)
mart = strategies.martingale(0, 0)
oscar = strategies.oscars_grind(0, 0, 0)
lab = strategies.labouchere(0, [], 0, 0)
counting = strategies.card_counting(0, 0, 0)
strat_buttons = classes.StrategyButton(paroli, sys1326, revlab, onehalf, counting, mart, oscar, lab, '')

# input boxes
balance_box = classes.InputBox(width - 600, height-695, 300, 70, '', 100)
bet_box = classes.InputBox(width/2 + 100, height - 490, 300, 70, '', 100, [LIGHTTEAL, DARKTEAL, OFFWHITE], txtcol = OFFWHITE)
num_sim_box = classes.InputBox(width - 600, height-400, 300, 70, '', 100, is_int = True)
num_deal_box = classes.InputBox(width - 600, height-600, 300, 70, '', 100, is_int= True)
bet_unit = classes.InputBox(width - 530, height-700, 300, 70, '', 100)
desired_profit = classes.InputBox(width - 530, height-500, 300, 70, '', 100)





napaka = False

mygame.shuffle_deck()




def view(position):
    if position == 1:
        menu_window.menu()
    elif position == 2:
        prep_window.bet_window(mygame, balance_box)
    elif position == 3:                           ############ simulation - bomo naredili pol
        prep_window.bet_window_sim(mygame, num_sim_box, num_deal_box)
    elif position == '3a':
        prep_window.select_strategy_window(mygame, strat_buttons)
    elif position == '3b':
        prep_window.unit_strategy(mygame, strat_buttons, bet_unit, desired_profit)
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
    elif position == 21:
        table_ai.deal_first_hand(mygame, aihand, strat_buttons)
    elif position == 22:
        table_ai.first_dealing(mygame, aihand, strat_buttons)
    elif position == 23:
        table_ai.dealing(mygame, aihand, strat_buttons)
    elif position == 24:
        table_ai.deal_dealer(mygame, aihand, strat_buttons)
    elif position == 25:
        table_ai.ai_winner(mygame, aihand, strat_buttons)
    elif position == 26:
        table_ai.split(mygame, aihand, strat_buttons)
    elif position == 27:
        table_ai.saving_data(mygame, aihand, strat_buttons)
    elif position == 28:
        table_ai.set_bet(mygame, aihand, strat_buttons)


# ponovimo ga 100x? 1000x?
# mogoce 1000x in imamo 100 rund

    

konec = False
# Beginning Game Loop
while True:
    if konec:
        break

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
                prep_window.simulation_buttons(mygame, mouse, num_sim_box, num_deal_box)
            elif position == '3a':
                prep_window.strategy_buttons(mygame, mouse, strat_buttons)
            elif position == '3b':
                prep_window.unit_strategy_button(mygame, mouse, strat_buttons, bet_unit, desired_profit)
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
        elif position == 4:
            bet_box.handle_event(event, gameDisplay, mygame, True)
        elif position == 3:
            num_sim_box.handle_event(event, gameDisplay, mygame)
            num_deal_box.handle_event(event, gameDisplay, mygame)
        elif position == '3b':
            bet_unit.handle_event(event, gameDisplay, mygame, True)
            desired_profit.handle_event(event, gameDisplay, mygame)




