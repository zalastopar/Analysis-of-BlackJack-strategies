from pickle import TRUE
import pygame
from pygame.locals import *


# functions
import functions.classes as classes
import functions.cards as cards

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


def print_error(txt, pos, size, col):
    text_font = pygame.font.SysFont('Bungee', size)
    warning = text_font.render(txt, TRUE, col)
    gameDisplay.blit(warning, pos)


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
        gameDisplay.blit(s_bet, (width - 1498.5 + 15, height - 850 + 15 + 40 + 40))

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)

    if hand.take_insurance > 0:
        text_font = pygame.font.SysFont('Bungee', 50)        
        ins = text_font.render('Insurance: ' + str(hand.take_insurance), TRUE, DARKTEAL)
        gameDisplay.blit(ins, (width - 1498.5 + 15, height - 850 + 15 + 40 + 40))

    # Probabilities for play with help
    if game.help:
        # create grid
        if hand.hit:
            #pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5 + 10, height - 850 + 10, 150, 40), 2)
            
            hit = classes.Button([width - 1498.5 + 10, height - 850 + 10], 'Hit:', TEAL, TEAL, DARKTEAL, [150, 40], True)
            hit.create(gameDisplay, 40, 2)
            # place for prob
            pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5 + 10 + 150, height - 850 + 10, 150, 40), 2)

            stand = classes.Button([width - 1498.5 + 10, height - 850 + 10 + 40], 'Stand:', TEAL, TEAL, DARKTEAL, [150, 40], True)
            stand.create(gameDisplay, 40, 2)
            # prob
            pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5 + 10 + 150, height - 850 + 10 + 40, 150, 40), 2)
        if hand.double(game):
            double = classes.Button([width - 1498.5 + 10, height - 850 + 10 + 80], 'Double:', TEAL, TEAL, DARKTEAL, [150, 40], True)
            double.create(gameDisplay, 40, 2)
            #
            pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5 + 10 + 150, height - 850 + 10 + 80, 150, 40), 2)
        if hand.split(game):
            split = classes.Button([width - 1498.5 + 10, height - 850 + 10 + 120], 'Split:', TEAL, TEAL, DARKTEAL, [150, 40], True)
            split.create(gameDisplay, 40, 2)
            #
            pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5 + 10 + 150, height - 850 + 10 + 120, 150, 40), 2)

    



# Create table
def place_bet(hand, game, box): # game.position = 4
    'First table screen. Player places bet.'
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create table
    pygame.draw.rect(gameDisplay, TEAL, (width - 1498.5, height - 850, width-200-3, height-100-3))
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5-2, height - 850-2, width-200, height-100), 10, 3)


    # Place your bet
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Place your bet:', TRUE, DARKTEAL)

    # Create textbox
    box.update()
    box.draw(gameDisplay)

    if box.napaka == 2:
        print_error("You can't bet more than you have!", [width/2 + 100, height - 490 - 20], 27, DARKTEAL)
    if box.napaka == 1:
        print_error('Your amount must be a number!', [width/2 + 100, height - 490 - 20], 28, DARKTEAL)

    gameDisplay.blit(first, (width/2 - 500, height - 500))
    


    # Balance
    text_font = pygame.font.SysFont('Bungee', 60)
    balance = text_font.render('Balance: ' + str(game.balance), TRUE, DARKTEAL)
    gameDisplay.blit(balance, (width - 1498.5 + 15, height - 850 + 15))

    # Bet button
    bet = classes.Button([width/2 + 100, height - 400], 'Bet', WRITING, TEAL, DARKTEAL, [300, 80], True)
    bet.create(gameDisplay, 70)

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)

    

    pygame.display.update()

def place_bet_buttons(game, mouse, hand, box):

    if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
        game.help = False
        game.balance =0
        game.position = 1
    elif width/2 + 100 <= mouse[0] <= width/2 + 100 + 300 and height - 400 <= mouse[1] <= height - 400 + 80 and box.text !='' and float(box.text) > 0 and float(box.text) <= game.balance: # bet
        hand.bet = float(box.text)
        box.text = ''
        box.txt_surface = box.text_font.render('', True, PINK)
        game.balance = game.balance - hand.bet
            
        # Add random cards

        # Player gets 2 cards
        sui, val = cards.random_card(game)
        c = classes.Card(sui, val, game.player_position)
        hand.player_hand.append(c)
        sui, val = cards.random_card(game)
        position = game.player_position
        c = classes.Card(sui, val, [position[0] + 150, position[1]])
        hand.player_hand.append(c)
        # Dealer gets 1 card
        sui, val = cards.random_card(game)
        c = classes.Card(sui, val, game.dealer_position)
        hand.dealer_hand.append(c)
        c.draw(gameDisplay)

        #hand.player_hand = [classes.Card('S', 14, [500,500]), classes.Card('S', 12, [500+150,500])]
        game.position = 5
    

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


def dealing(hand, game): # game.position = 5
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

    game.position = 6

    

def adding_buttons(hand, game): # game.position = 6
    'Function draws hands and adds action buttons.'

    empty_table(hand, game)

    # Different setting for split
    if hand.take_split == 1:
        #change_size(hand.player_hand, 800-5-150)
        draw_hand(hand.player_hand)
        draw_hand(hand.split_hand)
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)
    elif hand.take_split == 2:
        #change_size(hand.player_hand, width - 150)
        draw_hand(hand.player_hand)
        draw_hand(hand.split_hand)
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)
    else:
        # Draw hand
        change_size(hand.player_hand, width - 150)
        draw_hand(hand.player_hand)
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)




    # Check if the game is over for player
    val, k = hand.hand_value('P')
    v, k = hand.hand_value('S')
    if hand.BlackJack('P'):
        if hand.take_split == 1:
            hand.take_split = 2
            game.position = 9
        elif hand.take_split == 2 and v <= 21:
            game.position = 8
        else:
            game.position = 10
    elif val > 21:
        if hand.take_split == 1:
            hand.take_split = 2
            game.position = 9
        elif hand.take_split == 2 and v <= 21:
            game.position = 8
        else:
            game.position = 10
    elif val == 21:
        if hand.take_split == 1:
            hand.take_split = 2
            game.position = 9
        elif hand.take_split == 2 and v <= 21:
            game.position = 8
        else:
            game.positoin = 8
    
    # Draw value of hand
    value, k =  hand.hand_value('P')
    text_font = pygame.font.SysFont('Bungee', 50)
    v = text_font.render('Hand value: ' + str(value), TRUE, DARKTEAL)
    gameDisplay.blit(v, (game.player_position[0], game.player_position[1] - 40))

    # Check which buttons are necessary
    # Hit and stand
    if hand.hit:
        hit = classes.Button([width - 955, height - 70], 'Hit', WRITING, TEAL, DARKTEAL, [140, 60], True)
        hit.create(gameDisplay, 60)

        stand = classes.Button([width - 955 + 140 + 10, height - 70], 'Stand', WRITING, TEAL, DARKTEAL, [140, 60], True)
        stand.create(gameDisplay, 60)
    # Split
    if hand.split(game):
        split = classes.Button([width - 955 - 140 - 10, height - 70], 'Split', WRITING, TEAL, DARKTEAL, [140, 60], True)
        split.create(gameDisplay, 60)
    # Double
    if hand.double(game):
        double = classes.Button([width - 955 + 140 + 10 + 140 + 10, height - 70], 'Double', WRITING, TEAL, DARKTEAL, [140, 60], True)
        double.create(gameDisplay, 55)
    # Insurance
    if hand.insurance(game):
        ins = classes.Button([width - 955 + 140 + 140 + 140 +140 + 50, height - 70], 'Insurance', LIGHTTEAL, PINK, DARKTEAL, [200, 60], True)
        ins.create(gameDisplay, 55)
    
    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)




def dealing_buttons(game, mouse, hand):
    if width - 955 + 140 + 140 + 140 +140 + 50 <= mouse[0] <= width - 955 + 140 + 140 + 140 +140 + 50 + 200 and height - 70 <= mouse[1] <= height - 70 + 60 and hand.insurance(game): #insurance
        if hand.take_split == 2:
            hand.take_insurance = hand.take_insurance + hand.split_bet/2
        else:
            hand.take_insurance = hand.take_insurance + hand.bet/2

    #if the mouse is clicked on the button smth happens:
    if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
        game.position = 1

    elif width - 955 <= mouse[0] <= width - 955 + 140 and height - 70 <= mouse[1] <= height - 70 + 60: # Hit

        position = game.player_position
        num = len(hand.player_hand)
        sui, val = cards.random_card(game)
        if hand.take_split > 0:
            c = classes.Card(sui, val, [position[0] + 120*num, position[1]])
        else:
            c = classes.Card(sui, val, [position[0] + 150*num, position[1]])

        hand.player_hand.append(c)

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(200)

        game.position = 6

    elif width - 955 + 140 + 10 <= mouse[0] <= width - 955 + 140 + 140 + 10 and height - 70 <= mouse[1] <= height - 70 + 60: # Stand
        if hand.take_split == 1:
            hand.take_split = 2
            game.position = 9
        else:
            game.position = 8

    elif width - 955 + 140 + 10 + 140 + 10 <= mouse[0] <= width - 955 + 140 + 10 + 140 + 10 + 150 and height - 70 <= mouse[1] <= height - 70 + 60 and hand.double(game): # Double
        if hand.take_split == 1: 
            sui, val = cards.random_card(game)
            c = classes.Card(sui, val, [game.player_position[0] + 120*2, game.player_position[1]])
            hand.player_hand.append(c)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(200)
            # Change bet amount
            game.balance = game.balance - hand.bet
            hand.bet = hand.bet*2
            hand.take_split = 2
            game.position = 9

        elif hand.take_split == 2:
            sui, val = cards.random_card(game)
            c = classes.Card(sui, val, [game.player_position[0] + 120*2, game.player_position[1]])
            hand.player_hand.append(c)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(200)
            game.balance = game.balance - hand.split_bet
            hand.split_bet = hand.split_bet*2
            game.position = 8
        else:
            sui, val = cards.random_card(game)
            c = classes.Card(sui, val, [game.player_position[0] + 150*2, game.player_position[1]])
            hand.player_hand.append(c)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(200)
            game.balance = game.balance - hand.bet
            hand.bet = hand.bet*2
            game.position = 8
    elif width - 955 - 140 - 10 <= mouse[0] <= width - 955 - 140 - 10 + 140 and height - 70 <= mouse[1] <= height - 70 + 60 and hand.split(game): # split
        hand.take_split = 1
        c = hand.player_hand[0]
        d = hand.player_hand[1]
        c.position = [150, 500]
        hand.player_hand = [c]
        d.position = [800, 500]
        hand.split_hand = [d]


        game.balance = game.balance - hand.bet
        hand.split_bet = hand.bet ##########################spremen prikaz
        
        game.position = 9


def add_dealer_cards(hand, game): # game.position = 8

    empty_table(hand, game)
    draw_hand(hand.player_hand)
    draw_hand(hand.split_hand)
    draw_hand(hand.dealer_hand)

    position = game.dealer_position
    val, k = hand.hand_value('D')
    num = len(hand.dealer_hand)
    if val > 17:
        game.position = 10
    else:
        if hand.BlackJack('D'):
            game.position = 10
        
        if val == 17:
            if k:
                sui, val = cards.random_card(game)
                c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
                hand.dealer_hand.append(c)
                c.draw(gameDisplay)
                val, k = hand.hand_value('D')
            
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(500)
                game.position = 8
            else:
                game.position = 10

        else:
            sui, val = cards.random_card(game)
            c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
            hand.dealer_hand.append(c)
            c.draw(gameDisplay)
            val, k = hand.hand_value('D')

            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(500)

            game.position = 8


def split(hand, game): #game.position = 9

    empty_table(hand, game)

    if hand.take_split == 1:
        draw_hand(hand.player_hand)
        draw_hand(hand.split_hand)
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)


        game.player_position = [150, 500]
        sui, val = cards.random_card(game)
        c = classes.Card(sui, val, [game.player_position[0] + 120, game.player_position[1]])
        hand.player_hand.append(c)

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(600)

        draw_hand(hand.player_hand)

        game.position = 6

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

        sui, val = cards.random_card(game)
        c = classes.Card(sui, val, [game.player_position[0] + 120, game.player_position[1]])
        hand.player_hand.append(c)
        

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(600)

        c.draw(gameDisplay)

        game.position = 6






def winner(hand, game): # game.position = 10

    empty_table(hand, game) 

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
        else: # won
            text_font = pygame.font.SysFont('Bungee', 100)
            first = text_font.render('YOU WON: ' + str(money*hand.split_bet), TRUE, DARKTEAL)

        draw_hand(hand.split_hand)
        mon = hand.who_wins('S')

        if mon == 0: # lost
            text_font = pygame.font.SysFont('Bungee', 100)
            second = text_font.render('YOU LOST', TRUE, DARKTEAL)

        else: # won
            text_font = pygame.font.SysFont('Bungee', 100)
            second = text_font.render('YOU WON: ' + str(mon*hand.bet), TRUE, DARKTEAL)
            

        gameDisplay.blit(first, (800, 500 - 80))
        gameDisplay.blit(second, (150, 500 - 80))


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

        else: # won
            text_font = pygame.font.SysFont('Bungee', 100)
            first = text_font.render('YOU WON: ' + str(money*hand.bet), TRUE, DARKTEAL)
            gameDisplay.blit(first, (game.player_position[0], game.player_position[1] - 80))

    # Next button
    next = classes.Button([width/2 - 140/2, height - 70], 'Next', WRITING, TEAL, DARKTEAL, [140, 60], True)
    next.create(gameDisplay, 60)



def winner_buttons(game, mouse, hand):

    if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
        # Restart hand
        hand.player_hand = []
        hand.dealer_hand = []
        hand.winnings = 0
        hand.bet = 0
        hand.take_insurance = 0
        hand.take_split = 0
        hand.split_hand = []
        hand.split_bet = 0
        hand.take_double = False
        
        game.player_position = [500, 500]

        game.position = 1
    elif width/2 - 140/2 <= mouse[0] <= width/2 - 140/2 + 140 and height - 70 <= mouse[1] <= height - 70 + 60: # Go to ending

        # Change balance
        money = hand.who_wins('P')
        hand.winnings = hand.winnings + money * hand.split_bet
        game.balance = game.balance + hand.winnings
        if len(hand.split_hand) > 0:
            mon = hand.who_wins('S')
            hand.winnings = hand.winnings + mon * hand.bet
            game.balance = game.balance + hand.winnings

        # Restart hand
        hand.player_hand = []
        hand.dealer_hand = []
        hand.winnings = 0
        hand.bet = 0
        hand.take_insurance = 0
        hand.take_split = 0
        hand.split_hand = []
        hand.split_bet = 0
        hand.take_double = False

        game.player_position = [500, 500]
        game.position = 12



