from pickle import TRUE
import pygame
from pygame.locals import *
import time
import sys
import pygame_textinput

# functions
import functions.classes as classes
import functions.cards as cards

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

'''
def input(events, position, game, hand):
    
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
        pygame.draw.rect(gameDisplay, TEAL, [position[0], position[1] + position[3], 10 + warning.get_width(), position[3]])
        
        if game.balance < money:
            # Write warning
            text_font = pygame.font.SysFont('Bungee', 30)
            warning = text_font.render("You can't bet more than you have!", TRUE, DARKTEAL)
            gameDisplay.blit(warning, (position[0], position[1] + position[3]))
            hand.bet = 0.0
            
        else:
            hand.bet = money

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
'''

def empty_table(hand, game):
    'Function creates an empty table. Later different figures will be added to it.'

    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create table
    pygame.draw.rect(gameDisplay, TEAL, (width - 1498.5, height - 850, width-200-3, height-100-3))
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5-2, height - 850-2, width-200, height-100), 10, 3)

    # Balance
    text_font = pygame.font.SysFont('Bungee', 65)
    bet = text_font.render('Bet amount: ' + str(hand.bet), TRUE, DARKTEAL)
    text_font = pygame.font.SysFont('Bungee', 50)

    balance = text_font.render('Balance: ' + str(game.balance), TRUE, DARKTEAL)

    gameDisplay.blit(bet, (width - 1498.5 + 15, height - 120 ))
    gameDisplay.blit(balance, (width - 1498.5 + 15, height - 120 - 40))

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)


# Create table
def table(events, hand, game): # game.position = 4
    'First table screen. Player places bet.'
    # Create empty window
    pygame.draw.rect(gameDisplay, PINK, (0, 0, width, height))

    # Create table
    pygame.draw.rect(gameDisplay, TEAL, (width - 1498.5, height - 850, width-200-3, height-100-3))
    pygame.draw.rect(gameDisplay, DARKTEAL, (width - 1498.5-2, height - 850-2, width-200, height-100), 10, 3)


    # Place your bet
    text_font = pygame.font.SysFont('Bungee', 100)
    first = text_font.render('Place your bet:', TRUE, DARKTEAL)
    position = [width/2 + 100, height - 490, 100, 50]
    #################################input(events, position, game, hand) ############################# bet

    gameDisplay.blit(first, (width/2 - 500, height - 500))

    mouse = pygame.mouse.get_pos()

    # Balance
    text_font = pygame.font.SysFont('Bungee', 65)
    bet = text_font.render('Bet amount: ' + str(hand.bet), TRUE, DARKTEAL)
    text_font = pygame.font.SysFont('Bungee', 50)


    balance = text_font.render('Balance: ' + str(game.balance), TRUE, DARKTEAL)

    gameDisplay.blit(bet, (width - 1498.5 + 15, height - 120 ))
    gameDisplay.blit(balance, (width - 1498.5 + 15, height - 120 - 40))

    # Bet button
    bet = classes.Button([width/2 + 100, height - 400], 'Bet', LIGHTPINK, LIGHTTEAL, DARKTEAL, [300, 80], True)
    bet.create(gameDisplay, 70)

    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)


    # Clicking buttons
    mouse = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the button smth happens:
            if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
                game.position = 1
            elif width/2 + 100 <= mouse[0] <= width/2 + 100 + 300 and height - 400 <= mouse[1] <= height - 400 + 80 and hand.bet > 0: # bet
                game.position = 5
    

    pygame.display.update()


def draw_hand(hand):
    i = 0
    for card in hand:
        card.draw(gameDisplay)

def first_round(hand, game):  # game.position = 5
    'After the bet is placed dealer deals first round of cards. Player gets 2 and dealer gets only 1 face up.'
    game.balance = game.balance - hand.bet
    empty_table(hand, game)

    # Player gets first card
    sui, val = cards.random_card(game)
    c = classes.Card(sui, val, game.player_position)
    hand.player_hand.append(c)
    c.draw(gameDisplay)

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(500)

    # Dealer gets one card
    sui, val = cards.random_card(game)
    c = classes.Card(sui, val, game.dealer_position)
    hand.dealer_hand.append(c)
    c.draw(gameDisplay)

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(500)

    # Player gets one more card
    player_position = [game.player_position[0] + 150, game.player_position[1]]
    sui, val = cards.random_card(game)
    c = classes.Card(sui, val, player_position)
    hand.player_hand.append(c)
    c.draw(gameDisplay)

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(500)

    d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
    d_card.card_back(gameDisplay)

    #hand.dealer_hand = [classes.Card('S', 2, [0,0]), classes.Card('S', 14, [0,150])]

    # Go to window with buttons
    game.position = 6

def adding_buttons(events, hand, game): # game.position = 6
    'Function draws hands and adds action buttons.'

    empty_table(hand, game)

    # Draw hand
    draw_hand(hand.player_hand)
    draw_hand(hand.dealer_hand)
    d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
    d_card.card_back(gameDisplay)

    # Check if the game is over for player
    val, k = hand.hand_value('P')
    if hand.BlackJack('P'):
        game.position = 10
    elif val > 21:
        game.position = 10
    elif val == 21:
        game.positoin = 8
    
    
    # Check which buttons are necessary
    # Hit and stand
    if hand.hit:
        hit = classes.Button([width - 955, height - 70], 'Hit', LIGHTPINK, PINK, DARKTEAL, [140, 60], True)
        hit.create(gameDisplay, 60)

        stand = classes.Button([width - 955 + 140 + 10, height - 70], 'Stand', LIGHTPINK, PINK, DARKTEAL, [140, 60], True)
        stand.create(gameDisplay, 60)
    # Split
    if hand.split():
        split = classes.Button([width - 955 - 140 - 10, height - 70], 'Split', LIGHTPINK, PINK, DARKTEAL, [140, 60], True)
        split.create(gameDisplay, 60)
    # Double
    if hand.double():
        double = classes.Button([width - 955 + 140 + 10 + 140 + 10, height - 70], 'Double', LIGHTPINK, PINK, DARKTEAL, [140, 60], True)
        double.create(gameDisplay, 55)
    # Insurance
    if hand.insurance():
        ins = classes.Button([width - 955 + 140 + 140 + 140 +140 + 50, height - 70], 'Insurance', LIGHTTEAL, PINK, DARKTEAL, [200, 60], True)
        ins.create(gameDisplay, 55)
    
    # Menu button
    menu = classes.Button([width - 65, 5], 'Menu', LIGHTPINK, PINK, DARKPINK, [65, 30], False)
    menu.create(gameDisplay, 30)

    # Add action to buttons
    mouse = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width - 955 <= mouse[0] <= width - 955 + 140 and height - 70 <= mouse[1] <= height - 70 + 60 and hand.insurance(): #insurance
                hand.take_insurance = True

            #if the mouse is clicked on the button smth happens:
            if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
                game.position = 1
            elif width - 955 <= mouse[0] <= width - 955 + 140 and height - 70 <= mouse[1] <= height - 70 + 60: # Hit
                game.position = 7
            elif width - 955 + 140 + 10 <= mouse[0] <= width - 955 + 140 + 140 + 10 and height - 70 <= mouse[1] <= height - 70 + 60: # Stand
                game.position = 8
            elif width - 955 + 140 + 10 + 140 + 10 <= mouse[0] <= width - 955 + 140 + 10 + 140 + 10 + 150 and height - 70 <= mouse[1] <= height - 70 + 60 and hand.double(): # Double
                hand.take_double = True
                game.position = 7
            elif width - 955 - 140 - 10 <= mouse[0] <= width - 955 - 140 - 10 + 140 and height - 70 <= mouse[1] <= height - 70 + 60 and hand.split(): # Split
                hand.take_split = True
                game.position = 9

def add_player_cards(hand, game): # game.position = 7
    position = game.player_position
    num = len(hand.player_hand)
    if hand.take_double: # only one card is added
        sui, val = cards.random_card(game)
        c = classes.Card(sui, val, [position[0] + 150*2, position[1]])
        hand.player_hand.append(c)
        hand.take_double = False
        game.position = 8
    else: 
        sui, val = cards.random_card(game)
        c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
        hand.player_hand.append(c)
        game.position = 6

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(200)

def add_dealer_cards(hand, game): # game.position = 8

    empty_table(hand, game)
    draw_hand(hand.player_hand)
    draw_hand(hand.dealer_hand)

    position = game.dealer_position
    val, k = hand.hand_value('D')

    while val <= 17:
        if hand.BlackJack('D'):
            break

        val, k = hand.hand_value('D')
        num = len(hand.dealer_hand)
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
            else:
                break

        else:
            sui, val = cards.random_card(game)
            c = classes.Card(sui, val, [position[0] + 150*num, position[1]])
            hand.dealer_hand.append(c)
            c.draw(gameDisplay)
            val, k = hand.hand_value('D')

            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(500)

    game.position = 10

def split(): #game.position = 9
    pass

def winner(events, hand, game): # game.position = 10

    empty_table(hand, game)  
    draw_hand(hand.player_hand)
    if len(hand.dealer_hand) == 1:
        draw_hand(hand.dealer_hand)
        d_card = classes.Card('S', 12, [game.dealer_position[0] + 150, game.dealer_position[1]])
        d_card.card_back(gameDisplay)
    else:
        draw_hand(hand.dealer_hand)


    money = hand.who_wins()
    hand.winnings = money
   
    if money == 0: # lost
        text_font = pygame.font.SysFont('Bungee', 100)
        first = text_font.render('YOU LOST', TRUE, DARKTEAL)
        gameDisplay.blit(first, (game.player_position[0], game.player_position[1] - 80))

    else: # won
        text_font = pygame.font.SysFont('Bungee', 100)
        first = text_font.render('YOU WON: ' + str(money*hand.bet), TRUE, DARKTEAL)
        gameDisplay.blit(first, (game.player_position[0], game.player_position[1] - 80))


    # Next button
    next = classes.Button([width/2 - 140/2, height - 70], 'Next', LIGHTPINK, PINK, DARKTEAL, [140, 60], True)
    next.create(gameDisplay, 60)


    mouse = pygame.mouse.get_pos()
    # Clicking buttons
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the button smth happens:
            if  width - 65 <= mouse[0] <= width and 5 <= mouse[1] <= 35: # Go back to menu
                game.position = 1
            elif width/2 - 140/2 <= mouse[0] <= width/2 - 140/2 + 140 and height - 70 <= mouse[1] <= height - 70 + 60: # Hit
                game.position = 11

    pygame.display.update()





 



        



