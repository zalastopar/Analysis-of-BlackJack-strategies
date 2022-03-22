from pickle import TRUE
import pygame
from pygame.locals import *


# functions
import functions.classes as classes
import functions.cards as cards

# Setting up color objects



'''
Miza za AI
-ne rabjo prvega beta - sam upisejo
ne rabjo help

rabjo hit
stand
double 
split
'''


#PINK = (216, 0, 115)
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



def empty_table(hand, game):
    'Function creates an empty table. Later different figures will be added to it.'

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create table
    pygame.draw.rect(gameDisplay, TEAL, (width - 1498.5, height - 850, width-200-3, height-100-3))
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5-2, height - 850-2, width-200, height-100), 10, 3)

    # Balance
    text_font = pygame.font.SysFont('Bungee', 50)
    bet = text_font.render('Bet: ' + str(hand.bet), TRUE, DARKTEAL)
    text_font = pygame.font.SysFont('Bungee', 35)
    balance = text_font.render('Balance: ' + str(game.balance), TRUE, DARKTEAL)

    gameDisplay.blit(bet, (width - 1498.5 + 15, height - 850 + 30 + 15))
    gameDisplay.blit(balance, (width - 1498.5 + 15, height - 850 + 15))
    
    if hand.take_split > 0:
        s_bet = text_font = pygame.font.SysFont('Bungee', 50)
        s_bet = text_font.render('Split bet: ' + str(hand.split_bet), TRUE, DARKTEAL)
        gameDisplay.blit(s_bet, (width - 1498.5 + 15, height - 850 + 15 + 40 + 25))

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)
    '''
    if hand.take_insurance > 0:
        text_font = pygame.font.SysFont('Bungee', 50)        
        ins = text_font.render('Insurance: ' + str(hand.take_insurance), TRUE, DARKTEAL)
        gameDisplay.blit(ins, (width - 1498.5 + 15, height - 850 + 15 + 40 + 55))
    '''


# deal first hand

def deal_first_hand(game, hand): # game.position = 21
        '''
        hand.bet = float(box.text)
        box.text = ''
        box.txt_surface = box.text_font.render('', True, PINK)
        game.balance = game.balance - hand.bet
        '''

        # Add random cards

        # Player gets 2 cards
        sui, val = classes.random_card(game)
        c = classes.Card(sui, val, game.player_position)
        hand.player_hand.append(c)
        sui, val = classes.random_card(game)
        position = game.player_position
        c = classes.Card(sui, val, [position[0] + 150, position[1]])
        hand.player_hand.append(c)
        # Dealer gets 1 card
        sui, val = classes.random_card(game)
        c = classes.Card(sui, val, game.dealer_position)
        hand.dealer_hand.append(c)
        c.draw(gameDisplay)

        #hand.dealer_hand = [classes.Card('S', 11, game.dealer_position)]
        #hand.player_hand = [classes.Card('S', 14, [500,500]), classes.Card('S', 12, [500+150,500])]
        game.position = 22
    

def draw_hand(hand):
    i = 0
    for card in hand:
        card.draw(gameDisplay)

def hand_size(hand):
    first = hand[0].position[0]
    last = hand[-1].position[0]
    size = last - first + 150
    return size

def change_size(hand, pogoj):
    prejsnji = 150
    novi = 140

    while hand_size(hand) > pogoj:
        #spremeni velikost
        i = 0
        for card in hand:
            pos = card.position
            card.position = [pos[0] - i*prejsnji + i*novi, pos[1]]
            i = i+1
            prejsnji = novi
            novi = novi - 1

# draw hand
def first_dealing(game, hand): # game.position = 22
    'After the bet is placed dealer deals first round of cards. Player gets 2 and dealer gets only 1 face up.'

    empty_table(hand, game)

    # Player gets first card
    card = hand.player_hand[0]
    card.draw(gameDisplay)
    
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(500)

    # Dealer gets one card
    card = hand.dealer_hand[0]
    card.draw(gameDisplay)

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(500)

    # Player gets one more card
    card = hand.player_hand[1]
    card.draw(gameDisplay)

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(500)

    d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
    d_card.card_back(gameDisplay)

    # check if player will hit
    move = hand.next_move()
    if move == 'H':
        game.position = 23
    elif move == 'S':
        game.position = 24
    elif move == 'D':
        sui, val = classes.random_card(game)
        position = game.player_position
        c = classes.Card(sui, val, [position[0] + 150, position[1]])
        hand.player_hand.append(c)

        game.position = 24



def dealing(game, hand): # game.position = 23

    empty_table(hand, game)

    # Draw hand
    change_size(hand.player_hand, width - 150)
    draw_hand(hand.player_hand)
    draw_hand(hand.dealer_hand)
    d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
    d_card.card_back(gameDisplay)

    move = hand.next_move()
    if move == 'H':
        sui, val = classes.random_card(game)
        position = game.player_position
        c = classes.Card(sui, val, [position[0] + 150, position[1]])
        hand.player_hand.append(c)

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(200)

        game.position = 23
    else:
        game.position = 24




    '''
    if hand.take_split > 0:
        c = classes.Card(sui, val, [position[0] + 120*num, position[1]])
    else:
        c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
    '''



def deal_dealer(game, hand): # game.position = 24
    empty_table(hand, game)

    # draw hand
    draw_hand(hand.player_hand)
    draw_hand(hand.dealer_hand)

    position = game.dealer_position
    val, k = hand.hand_value('D')
    num = len(hand.dealer_hand)
    if val > 17:
        game.position = 25
    else:
        if hand.BlackJack('D'):
            game.position = 25
        
        if val == 17:
            if k:
                sui, val = classes.random_card(game)
                c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
                hand.dealer_hand.append(c)
                c.draw(gameDisplay)
                val, k = hand.hand_value('D')
            
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(500)
                game.position = 24
            else:
                game.position = 25

        else:
            sui, val = classes.random_card(game)
            c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
            hand.dealer_hand.append(c)
            c.draw(gameDisplay)
            val, k = hand.hand_value('D')

            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(500)

            game.position = 24
    

# ending game.position
def ai_winner(game, hand): # game.position = 25
    empty_table(hand, game) 

    draw_hand(hand.player_hand)
    if len(hand.dealer_hand) == 1:
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)
    else:
        draw_hand(hand.dealer_hand)

    money = hand.who_wins('P')
    hand.winnings = money * hand.bet

    if money == 0: # lost
        text_font = pygame.font.SysFont('Bungee', 100)
        first = text_font.render('YOU LOST', TRUE, DARKTEAL)
        gameDisplay.blit(first, (game.player_position[0], game.player_position[1] - 80))

    else: # won
        text_font = pygame.font.SysFont('Bungee', 100)
        first = text_font.render('YOU WON: ' + str(money*hand.bet), TRUE, DARKTEAL)
        gameDisplay.blit(first, (game.player_position[0], game.player_position[1] - 80))

    pygame.time.delay(500)
    
    # if play again game.position = 21
    # else neki svojga



