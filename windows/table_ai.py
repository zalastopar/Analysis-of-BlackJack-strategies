from pickle import TRUE
import pygame
from pygame.locals import *
import pandas as pd



# functions
import functions.classes as classes
import functions.cards as cards
import functions.strategies as strategies
import functions.save_data as save_data


# Setting up color objects
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
    balance = text_font.render('Balance: ' + str(round(game.balance, 2)), TRUE, DARKTEAL)

    gameDisplay.blit(bet, (width - 1498.5 + 15, height - 850 + 30 + 15))
    gameDisplay.blit(balance, (width - 1498.5 + 15, height - 850 + 15))
    
    if hand.take_split > 0:
        s_bet = text_font = pygame.font.SysFont('Bungee', 50)
        s_bet = text_font.render('Split bet: ' + str(round(hand.split_bet,2)), TRUE, DARKTEAL)
        gameDisplay.blit(s_bet, (width - 1498.5 + 15, height - 850 + 15 + 40 + 25))

    '''
    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)
    
    if hand.take_insurance > 0:
        text_font = pygame.font.SysFont('Bungee', 50)        
        ins = text_font.render('Insurance: ' + str(hand.take_insurance), TRUE, DARKTEAL)
        gameDisplay.blit(ins, (width - 1498.5 + 15, height - 850 + 15 + 40 + 55))
    '''


# deal first hand

def deal_first_hand(game, hand, strat): # game.position = 21
        '''
        hand.bet = float(box.text)
        box.text = ''
        box.txt_surface = box.text_font.render('', True, PINK)
        game.balance = game.balance - hand.bet
        '''

        strat.active_strategy.set_bet(game)

        # preveri ce je dovolj denarja ############################################################
        if game.balance >= strat.active_strategy.bet:
            game.balance = game.balance - strat.active_strategy.bet
        else:
            game.position = 13 ##################################################
        hand.restart_hand()
        hand.bet = strat.active_strategy.bet

        # Add random cards

        # Player gets 2 cards
        sui, val = classes.random_card(game)
        c = classes.Card(sui, val, game.player_position)
        if strat.active_strategy.strat == 'counting':
            strat.active_strategy.change_count(c) ###########################################################################
            strat.active_strategy.cards += 1
        hand.player_hand.append(c)
        sui, val = classes.random_card(game)
        position = game.player_position
        c = classes.Card(sui, val, [position[0] + 150, position[1]])
        if strat.active_strategy.strat == 'counting':
            strat.active_strategy.change_count(c) ###########################################################################
            strat.active_strategy.cards += 1
        hand.player_hand.append(c)
        # Dealer gets 1 card
        sui, val = classes.random_card(game)
        c = classes.Card(sui, val, game.dealer_position)
        if strat.active_strategy.strat == 'counting':
            strat.active_strategy.change_count(c) ###########################################################################
            strat.active_strategy.cards += 1
        hand.dealer_hand.append(c)

        #hand.dealer_hand = [classes.Card('S', 4, game.dealer_position)]
        #hand.player_hand = [classes.Card('S', 11, [500,500]), classes.Card('S', 11, [500+150,500])]
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
def first_dealing(game, hand,strat): # game.position = 22
    'After the bet is placed dealer deals first round of cards. Player gets 2 and dealer gets only 1 face up.'

    empty_table(hand, game)

    # Player gets first card
    card = hand.player_hand[0]
    card.draw(gameDisplay)
    
    pygame.display.flip()
    pygame.event.pump()
    #pygame.time.delay(200)

    # Dealer gets one card
    card = hand.dealer_hand[0]
    card.draw(gameDisplay)

    pygame.display.flip()
    pygame.event.pump()
    #pygame.time.delay(200)

    # Player gets one more card
    card = hand.player_hand[1]
    card.draw(gameDisplay)

    pygame.display.flip()
    pygame.event.pump()
    #pygame.time.delay(200)

    d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
    d_card.card_back(gameDisplay)

    # check if player will hit
    move = hand.next_move(game)
    if move == 'H':
        game.position = 23
    elif move == 'S':
        hand.move.append('S') # save move
        game.position = 24
    elif move == 'D':
        hand.move.append('D') # save move
        sui, val = classes.random_card(game)
        position = game.player_position
        c = classes.Card(sui, val, [position[0] + 2*150, position[1]])
        if strat.active_strategy.strat == 'counting':
            strat.active_strategy.change_count(c) ###########################################################################
            strat.active_strategy.cards += 1
        hand.player_hand.append(c)

        pygame.display.flip()
        pygame.event.pump()
        #pygame.time.delay(200)

        game.balance = game.balance - hand.bet
        hand.bet = hand.bet*2

        game.position = 24
    elif move == 'split':
        hand.move.append('split') # save move
        hand.take_split = 1
        c = hand.player_hand[0]
        d = hand.player_hand[1]
        c.position = [150, 500]
        hand.player_hand = [c]
        d.position = [800, 500]
        hand.split_hand = [d]
        #print(hand.player_hand)
        #print(hand.split_hand)

        game.balance = game.balance - hand.bet
        hand.split_bet = hand.bet

        game.position = 26



def dealing(game, hand, strat): # game.position = 23

    empty_table(hand, game)

    # Draw hand
    change_size(hand.player_hand, width - 150)
    draw_hand(hand.player_hand)
    draw_hand(hand.dealer_hand)
    if len(hand.split_hand) > 0:
        draw_hand(hand.split_hand)
    d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
    d_card.card_back(gameDisplay)

    move = hand.next_move(game)
    if move == 'H':
        hand.move.append('H') # save move
        sui, val = classes.random_card(game)
        position = game.player_position
        num = len(hand.player_hand)
        c = classes.Card(sui, val, [position[0] + num*150, position[1]])
        if strat.active_strategy.strat == 'counting':
            strat.active_strategy.change_count(c) ###########################################################################
            strat.active_strategy.cards += 1
        hand.player_hand.append(c)

        pygame.display.flip()
        pygame.event.pump()
        #pygame.time.delay(200)

        game.position = 23
    else:
        if hand.take_split == 1:
            hand.move.append('S') # save move
            hand.move.append(',') # save move - split start new hand
            hand.take_split = 2
            pygame.display.flip()
            pygame.event.pump()
            #pygame.time.delay(200)
            game.position = 26
        else:
            hand.move.append('S') # save move 
            game.position = 24


    '''
    if hand.take_split > 0:
        c = classes.Card(sui, val, [position[0] + 120*num, position[1]])
    else:
        c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
    '''


    
def split(game, hand, strat): #game.position = 26

    empty_table(hand, game)
    #print('aaa')
    if hand.take_split == 1:
        draw_hand(hand.player_hand)
        draw_hand(hand.split_hand)
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)


        game.player_position = [150, 500]
        sui, val = classes.random_card(game)
        c = classes.Card(sui, val, [game.player_position[0] + 120, game.player_position[1]])
        if strat.active_strategy.strat == 'counting':
            strat.active_strategy.change_count(c) ###########################################################################
            strat.active_strategy.cards += 1
        hand.player_hand.append(c)

        pygame.display.flip()
        pygame.event.pump()
        #pygame.time.delay(600)

        draw_hand(hand.player_hand)

        game.position = 23

    elif hand.take_split == 2:

        game.player_position = [800, 500]
        umesna = hand.player_hand
        hand.player_hand = hand.split_hand
        hand.split_hand = umesna



        draw_hand(hand.player_hand)
        draw_hand(hand.split_hand)
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)

        sui, val = classes.random_card(game)
        c = classes.Card(sui, val, [game.player_position[0] + 120, game.player_position[1]])
        if strat.active_strategy.strat == 'counting':
            strat.active_strategy.change_count(c) ###########################################################################
            strat.active_strategy.cards += 1
        hand.player_hand.append(c)
        

        pygame.display.flip()
        pygame.event.pump()
        #pygame.time.delay(600)

        c.draw(gameDisplay)

        game.position = 23

def deal_dealer(game, hand, strat): # game.position = 24
    empty_table(hand, game)

    # draw hand
    draw_hand(hand.player_hand)
    draw_hand(hand.dealer_hand)
    draw_hand(hand.split_hand)

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
                if strat.active_strategy.strat == 'counting':
                    strat.active_strategy.change_count(c) ###########################################################################
                    strat.active_strategy.cards += 1
                hand.dealer_hand.append(c)
                c.draw(gameDisplay)
                val, k = hand.hand_value('D')
            
                pygame.display.flip()
                pygame.event.pump()
                #pygame.time.delay(200)
                game.position = 24
            else:
                game.position = 25

        else:
            sui, val = classes.random_card(game)
            c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
            if strat.active_strategy.strat == 'counting':
                strat.active_strategy.change_count(c) ###########################################################################
                strat.active_strategy.cards += 1
            hand.dealer_hand.append(c)
            c.draw(gameDisplay)
            val, k = hand.hand_value('D')

            pygame.display.flip()
            pygame.event.pump()
            #pygame.time.delay(200)

            game.position = 24
    

def ai_winner(game, hand, strat): # game.position = 25
    empty_table(hand, game) 
    #print(hand.move)
    #print(hand.player_hand)
    #print(hand.dealer_hand)
    #print(hand.split_hand)

    # announce winner

    # winner with split
    if hand.take_split == 2:
        # draw dealers cards
        if len(hand.dealer_hand) == 1:
            draw_hand(hand.dealer_hand)
            d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
            d_card.card_back(gameDisplay)
        else:
            draw_hand(hand.dealer_hand)

        # draw players cards
        draw_hand(hand.player_hand)
        money = hand.who_wins('P')

        if money == 0: # lost
            text_font = pygame.font.SysFont('Bungee', 100)
            first = text_font.render('YOU LOST', TRUE, DARKTEAL)
        elif money == 1: # push
            text_font = pygame.font.SysFont('Bungee', 100)
            first = text_font.render('PUSH: ' + str(money*hand.split_bet), TRUE, DARKTEAL)
        else: # won
            text_font = pygame.font.SysFont('Bungee', 100)
            first = text_font.render('YOU WON: ' + str(money*hand.split_bet), TRUE, DARKTEAL)

        draw_hand(hand.split_hand)
        mon = hand.who_wins('S')

        if mon == 0: # lost
            text_font = pygame.font.SysFont('Bungee', 100)
            second = text_font.render('YOU LOST', TRUE, DARKTEAL)
        elif mon == 1: # push
            text_font = pygame.font.SysFont('Bungee', 100)
            second = text_font.render('PUSH: ' + str(mon*hand.bet), TRUE, DARKTEAL)
        else: # won
            text_font = pygame.font.SysFont('Bungee', 100)
            second = text_font.render('YOU WON: ' + str(mon*hand.bet), TRUE, DARKTEAL)
            

        gameDisplay.blit(first, (800, 500 - 80))
        gameDisplay.blit(second, (150, 500 - 80))

    # normal winner
    else:
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
        elif money == 1: # push
            text_font = pygame.font.SysFont('Bungee', 100)
            first = text_font.render('PUSH: ' + str(money*hand.bet), TRUE, DARKTEAL)
            gameDisplay.blit(first, (game.player_position[0], game.player_position[1] - 80))
        else: # won
            text_font = pygame.font.SysFont('Bungee', 100)
            first = text_font.render('YOU WON: ' + str(money*hand.bet), TRUE, DARKTEAL)
            gameDisplay.blit(first, (game.player_position[0], game.player_position[1] - 80))


    pygame.display.flip()
    pygame.event.pump()
    #pygame.time.delay(1000)

    # save data
    save_data.save_prob(hand, game)
    
    #print(game.prob_data)  
    #print(game.soft_data)
    #print(game.split_data)
    #print(hand.player_hand)
    #print(hand.dealer_hand)
    #print(game.data_balance)
    #print(game.balance)
    #print(game.data_bet)
    #print(hand.bet)

    # new bet or cash out
    if game.length >=100:  ### igramo 100 mesanj
        # Change balance
        money = hand.who_wins('P')
        w = hand.winnings + money * hand.split_bet
        game.balance = game.balance + w
        if len(hand.split_hand) > 0:
            mon = hand.who_wins('S')
            hand.winnings = hand.winnings + mon * hand.bet
            game.balance = game.balance + hand.winnings

        # save balance data
        save_data.save_simulation(hand, game)
        print('multiple')
        print(game.data_multiple)
        print('balance')
        print(game.data_balance)
        print('bet')
        print(game.data_bet)
        df = pd.DataFrame(game.data_bet)
        print(df)

        game.player_position = [500, 500]
        
        # new round of simulation
        if game.sim < 100: # we have 100 simulations
            game.sim += 1
            game.shuffle_deck()
            game.length = 0
            game.balance = game.initial_balance

            # restart strategies
            strat.restart_strategies(game)



            
            

        else: # finnish
            
            # save probabilities
            save_data.update_csv_prob(game.prob_data, 'data/prob_data.csv')
            save_data.update_csv_prob(game.split_data, 'data/split_data.csv')
            save_data.update_csv_prob(game.soft_data, 'data/soft_data.csv')

            # save balance
            df = pd.DataFrame(game.data_multiple)
            df.to_csv('data/' + strat.active_strategy.strat + '.csv')

            df = pd.DataFrame(game.data_bet)
            df.to_csv('data/' + strat.active_strategy.strat + '-bet.csv')

            df = pd.DataFrame(game.data_balance)
            df.to_csv('data/' + strat.active_strategy.strat + '-balance.csv')
            
            game.position = 13


    else: # bet again
        
        # Change balance
        money = hand.who_wins('P')
        hand.winnings = hand.winnings + money * hand.split_bet
        if len(hand.split_hand) > 0:
            mon = hand.who_wins('S')
            hand.winnings = hand.winnings + mon * hand.bet
        game.balance = game.balance + hand.winnings

        # save balance data
        save_data.save_simulation(hand, game)

        # check winning streak
        if strat.active_strategy.strat in ['paroli', '1326', 'rev_lab', 'increase']: # wining streak
            if hand.winnings >= hand.bet + hand.split_bet:
                strat.active_strategy.winning_streak += 1 
            else:
                strat.active_strategy.winning_streak = 0 
        elif strat.active_strategy.strat == 'counting':
            pass
        else: # losing streak
            if hand.winnings >= hand.bet + hand.split_bet:
                strat.active_strategy.losing_streak = 0
            else:
                strat.active_strategy.losing_streak += 1

        game.length += 1
        game.player_position = [500, 500]

        # shuffle deck if there is less than 20% cards left
        if len(game.deck) <= 0.2*6*52:
            game.shuffle_deck()
            if strat.active_strategy.strat == 'counting': # restart counting
                strat.active_strategy.cards = 0
                strat.active_strategy.count = 0


        game.position = 21
