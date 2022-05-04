from pickle import TRUE
import os.path
import pygame
from pygame.locals import *
import random




# Setting up color objects
PINK = (242,233,222)
DARKPINK = (222,93,131)#(212,112,162)
LIGHTPINK = (239,187,204)

TEAL = (221,173,175)
DARKTEAL = (216,105,105)
LIGHTTEAL = (239,187,204)

OFFWHITE = (242,233,222)
WRITING = (255,153,153)

width = 1600
height = 900
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(PINK)
pygame.display.set_caption("BlackJack Table")


def print_error(txt, pos):
    text_font = pygame.font.SysFont('Bungee', 30)
    warning = text_font.render(txt, TRUE, TEAL)
    gameDisplay.blit(warning, pos)

def random_card(game):
    c = game.deck.pop(1)
    sui = c[0]
    c = c[1:]
    val = int(c)
    return sui, val


# game
class Game:
    def __init__(self, simulation, position, help, balance, deck, initial_bet, length, sim, data_balance, data_bet, data_0x, data_3x, data_5x, data_10x, data_to0, prob_data, split_data, soft_data):
        self.simulation = simulation # save as int how many 0 to inf
        self.position = position # which window is open
        self.help = help # TRUE or FALSE ################################################# popravi v window
        self.balance = balance
        self.deck = deck # list of cards that can be chosen - currently we play with 6 decks
        self.dealer_position = [500, 70]
        self.player_position = [500, 500]  
        self.initial_bet = initial_bet
        self.length = length # int number of bets

        self.sim = sim # number of simulation
        self.data_balance = data_balance # dictionary: key = a number of simulation, value = list of balances after each dealings
        self.data_bet = data_bet # dictionary: key = a number of simulation, value = list of bets
        self.data_0x = data_0x # list: 1 if balcance gets to 0, 0 else
        self.data_3x = data_3x # list: 1 if balance gets to 3x, 0 else
        self.data_5x = data_5x # list: 1 if balance gets to 5x, 0 else
        self.data_10x = data_10x # list: 1 if balance gets to 10x, 0 else
        self.data_to0 = data_to0 # list: number or dealings needed to get to 0 balance 

        self.prob_data = prob_data # dict
        self.split_data = split_data # dict
        self.soft_data = soft_data # dict

    def shuffle_deck(self):
        deck = []
        suits = ['S', 'H', 'D', 'C']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for s in suits:
            for v in values:
                c = s + str(v)
                part = [c, c, c, c, c, c]
                deck = deck + part
        random.shuffle(deck)
        self.deck = deck



# card
class Card:
    def __init__(self, suit, value, position):
        self.suit = suit # suit of the card D(diamond), C(clubs), H(hearts), S(spade)
        self.value = value # number of the card
        self.position = position #position of the card on the table (x, y)

    def __repr__(self):
        return self.suit + str(self.value)

    def __str__(self):
        return self.suit + str(self.value)

    def real_value(self):
        if self.value in [12, 13, 14]:
            return 10
        else:
            return self.value

    def draw(self, screen):
        # Blank card
        pygame.draw.rect(screen, OFFWHITE, (self.position[0], self.position[1], 200, 320), border_radius=6)
        pygame.draw.rect(screen, DARKTEAL, (self.position[0], self.position[1], 200, 320), 5, 6)

        sign = self.value
        if sign == 14:
            sign = 'K'
        elif sign == 13:
            sign = 'Q'
        elif sign == 12:
            sign = 'J'
        elif sign == 11:
            sign = 'A'
        elif sign == 1:
            sign = 'A'
        else:
            sign = str(sign)


        # Draw value on card
        text_font = pygame.font.SysFont('Agency FB', 200)
        text_surface = text_font.render(sign, True, LIGHTPINK)
        w = text_surface.get_width()
        h = text_surface.get_height()


        value = text_font.render(sign, TRUE, WRITING)
        screen.blit(value, (self.position[0] - w/2 + 200/2, self.position[1] + 320/2 - h/2))


        # For small text
        text_font = pygame.font.SysFont('Agency FB', 50)
        text_surface = text_font.render(sign, True, LIGHTPINK)
        w = text_surface.get_width()
        h = text_surface.get_height()
        value = text_font.render(sign, TRUE, PINK)


        # Draw suit on card
        s = self.suit
        if s == 'C':
            path = os.path.join("suits/club.png")
        elif s == 'H':
            path = os.path.join("suits/heart.png")
        elif s == 'D':
            path = os.path.join("suits/diamond.png")
        elif s == 'S':
            path = os.path.join("suits/spade.png")

        
        image = pygame.image.load(path)
        width, height = image.get_width(), image.get_height()
        image = pygame.transform.scale(image, (width*0.5, height*0.5))
        width, height = image.get_width(), image.get_height()
        screen.blit(image, (self.position[0] + 200 - width - 1, self.position[1] + 4))
        screen.blit(image, (self.position[0] + 3, self.position[1] + 320 - height - 4))




        # self.position[1] - (self.position[1] + 320/2 - h/2)/2 - height/2

        # Small values
        text_font = pygame.font.SysFont('Bungee', 60)
        text_surface = text_font.render(sign, True, WRITING)
        w = text_surface.get_width()
        h = text_surface.get_height()
        value = text_font.render(sign, TRUE, WRITING)
        screen.blit(value, (self.position[0] + 7, self.position[1] + 5))
        screen.blit(value, (self.position[0] + 200 -w - 6, self.position[1] + 320 - height + 4))

    def card_back(self, screen):
        # Blank card
        pygame.draw.rect(screen, OFFWHITE, (self.position[0], self.position[1], 200, 320), border_radius=6)
        pygame.draw.rect(screen, DARKTEAL, (self.position[0], self.position[1], 200, 320), 5, 6)


        # Add Kitten
        path = os.path.join("suits/cat1.png")
        image = pygame.image.load(path)

        width, height = image.get_width(), image.get_height()

        image = pygame.transform.scale(image, (width*0.32, height*0.32))
        width, height = image.get_width(), image.get_height()
        screen.blit(image, (self.position[0] + (200-width)/2 + 3, self.position[1] + (320 - height)/2))

class Hand:
    def __init__(self, bet, hand, dealer_hand, insurance, double, split, split_hand, winnings, split_bet, move):
        self.bet = bet # float
        self.player_hand = hand # sez with cards
        self.dealer_hand = dealer_hand # sez with player cards
        self.take_insurance = insurance # num, how much is insurance
        self.take_split = split # 0 - if not split, 1-dealing first hand, 2-dealing 2nd hand 
        self.split_hand = split_hand
        self.take_double = double # bool - if player doubled
        self.winnings = winnings
        self.split_bet = split_bet
        self.move = move

    def __repr__(self):
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def __str__(self):
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def hand_value(self, who): # who 'D' for dealer and 'P' for player 'S' split hand
        '''The function takes a list of cards and calculates its value'''
        if who == 'D':
            cards = self.dealer_hand
        elif who == 'S':
            cards = self.split_hand
        else:
            cards = self.player_hand
            
        hand = []
        # remove suit and only look at value
        for card in cards:
            val = card.real_value()
            hand.append(val)

        hand_value = 0
        soft = False
        #print(hand)
        val = 0
        ace = 0
        if 11 in hand:
            '''Ace can count as 11 or as 1. There can be only 1 ace in hand that counts as 11
            otherwise hand value would be > 22. So max 1 ace counts as 11 and other as 1.'''
            ace = hand.count(11)
            #print(ace)
            hand = [value for value in hand if value != 11]
            val = sum(hand) 
            val = val + ace # firstly count all aces as one
            #print(val)
            #print(val + 10 <= 21)
            if val + 10 <= 21:
                val = val + 10 # if it is possible count one ace as 11
                soft = True
            hand_value = val
        else:
            hand_value = sum(hand)

        return(hand_value, soft)

    def split(self, game):
        s = False
        hand = self.player_hand
        if game.balance >= self.bet:
            if len(hand) == 2 and hand[0].real_value() == hand[1].real_value() and self.take_split == 0:
                s = True
        return s

    def double(self, game):
        d = False
        hand = self.player_hand
        if game.balance >= self.bet:
            if len(hand) == 2:
                d = True
        return d
    
    def insurance(self, game):
        s = False
        hand = self.dealer_hand[0]
        if game.balance >= self.bet/2 and self.take_split == 0 and self.take_insurance == 0:
            if hand.value == 11:
                s = True
        return s

    def hit(self):    # goes also for stand
        val, k = self.hand_value('P')
        if val > 21:
            return False
        return True
            
    def BlackJack(self, who): # who can be either 'D' (dealer) or 'P' player or 'S' split
        if who == 'D':
            hand = self.dealer_hand
            if len(hand) != 2:
                return False
        elif who == 'S':
            hand = self.split_hand
        else:
            hand = self.player_hand
        first = hand[0]
        second= hand[1]
        if len(hand) == 2 and [first.real_value(), second.real_value()] == [10, 11]:
            return True
        elif  len(hand) == 2 and [first.real_value(), second.real_value()] == [11, 10]:
            return True
 
    def who_wins(self, who): # 'P' player, 'S' split hand
        winnings = 0
        dealer, k = self.hand_value('D')
        player, k = self.hand_value(who)
        if self.BlackJack(who) and self.BlackJack('D'):
            winnings = 1
        elif self.BlackJack(who):
            winnings = 2.5
        elif player > 21:  # over 21 - you lose
            winnings = 0
        elif player <= 21: # you maybe win
            # check dealers cards
            if self.BlackJack('D'): # dealer BJ - you lose
                winnings = 0
            elif dealer > 21: # dealer over - you win
                winnings = 2
            else:
                if dealer == player:
                    winnings = 1
                elif dealer > player:
                    winnings = 0
                else:
                    winnings = 2

        return winnings

    def restart_hand(self):
        self.player_hand = []
        self.dealer_hand = []
        self.winnings = 0
        self.bet = 0
        self.take_insurance = 0
        self.take_split = 0
        self.split_hand = []
        self.split_bet = 0
        self.take_double = False


# first key = player, second keys = dealer
decisions = {}
decisions[9] = {2: 'H', 3: 'D', 4: 'D', 5: 'D', 6 : 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[10] = {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'H', 11: 'H'}
decisions[11] = {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'D', 11: 'D'}
decisions[12] = {2: 'H', 3: 'H', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[13] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[14] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[15] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[16] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[17] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}
# pod 9 hit, nad 17 stand


# ace and smth
# only when player has 2 cards
soft = {}
soft[2] = {2: 'H', 3: 'H', 4: 'H', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[3] = {2: 'H', 3: 'H', 4: 'H', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[4] = {2: 'H', 3: 'H', 4: 'DH', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[5] = {2: 'H', 3: 'H', 4: 'DH', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[6] = {2: 'H', 3: 'DH', 4: 'DH', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[7] = {2: 'DS', 3: 'DS', 4: 'DS', 5: 'DS', 6 : 'DS', 7: 'S', 8: 'S', 9: 'H', 10: 'H', 11: 'H'}
soft[8] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6 : 'DS', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}
soft[9] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6 : 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}
soft[10] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6 : 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}

# split
splitgrid = {}
splitgrid[2] = {2: 'N', 3: 'N', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[3] = {2: 'N', 3: 'N', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[4] = {2: 'N', 3: 'N', 4: 'N', 5: 'N', 6 : 'N', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[5] = {2: 'N', 3: 'N', 4: 'N', 5: 'N', 6 : 'N', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[6] = {2: 'N', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[7] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[8] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'Y', 9: 'Y', 10: 'Y', 11: 'Y'}
splitgrid[9] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'N', 8: 'Y', 9: 'Y', 10: 'N', 11: 'N'}
splitgrid[10] = {2: 'N', 3: 'N', 4: 'N', 5: 'N', 6 : 'N', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[11] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'Y', 9: 'Y', 10: 'Y', 11: 'Y'}


class Hand_ai:
    def __init__(self, bet, hand, dealer_hand, double, split, split_hand, winnings, split_bet, move):
        self.bet = bet # float
        self.player_hand = hand # sez with cards
        self.dealer_hand = dealer_hand # sez with player cards
        self.take_split = split # 0 - if not split, 1-dealing first hand, 2-dealing 2nd hand 
        self.split_hand = split_hand
        self.take_double = double # bool - if player doubled
        self.winnings = winnings # float - 1 if push, 2.5 if BJ, 2 if win, 0 if lose
        self.split_bet = split_bet 
        self.splitgrid = splitgrid # directions how to play
        self.soft = soft # directions how to play
        self.decisions = decisions # directions how to play 
        self.move = move # list of 'H', 'S', 'split', 'D'

    def __repr__(self):
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def __str__(self):
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def hand_value(self, who): # who 'D' for dealer and 'P' for player 'S' split hand
        '''The function takes a list of cards and calculates its value'''
        if who == 'D':
            cards = self.dealer_hand
        elif who == 'S':
            cards = self.split_hand
        else:
            cards = self.player_hand
            
        hand = []
        # remove suit and only look at value
        for card in cards:
            val = card.real_value()
            hand.append(val)

        hand_value = 0
        soft = False
        #print(hand)
        val = 0
        ace = 0
        if 11 in hand:
            '''Ace can count as 11 or as 1. There can be only 1 ace in hand that counts as 11
            otherwise hand value would be > 22. So max 1 ace counts as 11 and other as 1.'''
            ace = hand.count(11)
            #print(ace)
            hand = [value for value in hand if value != 11]
            val = sum(hand) 
            val = val + ace # firstly count all aces as one
            #print(val)
            #print(val + 10 <= 21)
            if val + 10 <= 21:
                val = val + 10 # if it is possible count one ace as 11
                soft = True
            hand_value = val
        else:
            hand_value = sum(hand)

        return(hand_value, soft)

    def split(self, game):
        s = False
        hand = self.player_hand
        if game.balance >= self.bet:
            if len(hand) == 2 and hand[0].real_value() == hand[1].real_value() and self.take_split == 0:
                s = True
        return s

    def double(self, game):
        d = False
        hand = self.player_hand
        if game.balance >= self.bet:
            if len(hand) == 2:
                d = True
        return d
    
    def insurance(self, game):
        s = False
        hand = self.dealer_hand[0]
        if game.balance >= self.bet/2 and self.take_split == 0 and self.take_insurance == 0:
            if hand.value == 11:
                s = True
        return s

    def hit(self):    # goes also for stand
        val, k = self.hand_value('P')
        if val > 21:
            return False
        return True
            
    def BlackJack(self, who): # who can be either 'D' (dealer) or 'P' player or 'S' split
        if who == 'D':
            hand = self.dealer_hand
            if len(hand) != 2:
                return False
        elif who == 'S':
            hand = self.split_hand
        else:
            hand = self.player_hand
        first = hand[0]
        second= hand[1]
        if len(hand) == 2 and [first.real_value(), second.real_value()] == [10, 11]:
            return True
        elif  len(hand) == 2 and [first.real_value(), second.real_value()] == [11, 10]:
            return True
 
    def who_wins(self, who): # 'P' player, 'S' split hand, 'D' dealer
        winnings = 0
        dealer, k = self.hand_value('D')
        player, k = self.hand_value(who)
        if self.BlackJack(who) and self.BlackJack('D'):
            winnings = 1
        elif self.BlackJack(who):
            winnings = 2.5
        elif player > 21:  # over 21 - you lose
            winnings = 0
        elif player <= 21: # you maybe win
            # check dealers cards
            if self.BlackJack('D'): # dealer BJ - you lose
                winnings = 0
            elif dealer > 21: # dealer over - you win
                winnings = 2
            else:
                if dealer == player:
                    winnings = 1
                elif dealer > player:
                    winnings = 0
                else:
                    winnings = 2

        return winnings

    def next_move(self, game):
        val, k = self.hand_value('P')
        val2, k = self.hand_value('D')
        # check for split
        if self.split(game):
            num = self.player_hand[0].real_value()
            #print('split')
            #print(num)
            check = self.splitgrid[num][val2]
            if check == 'Y':
                #print('res ssplit')
                return 'split'

        #check for ace
        if 11 == self.player_hand[0].value and len(self.player_hand) == 2: # ace is first card
            num = self.player_hand[1].real_value()
            check = self.soft[num][val2]
            # DH
            if check == 'DH':
                if self.double(game):
                    return 'D'
                else:
                    return 'H'
            # DS
            elif check == 'DS':
                if self.double(game):
                    return 'D'
                else:
                    return 'H'
            else:
                return check
        elif 11 == self.player_hand[1].value and len(self.player_hand) == 2: # ace is second card
            num = self.player_hand[0].real_value()
            check = self.soft[num][val2]
            # DH
            if check == 'DH':
                if self.double(game):
                    return 'D'
                else:
                    return 'H'
            # DS
            elif check == 'DS':
                if self.double(game):
                    return 'D'
                else:
                    return 'H'
            else:
                return check
        else:
            #print(val)
            if val <= 8:
                return 'H'
            elif val >= 18:
                return 'S'
            else:
                return self.decisions[val][val2]

    def restart_hand(self):
        self.player_hand = []
        self.dealer_hand = []
        self.winnings = 0
        self.bet = 0
        self.take_insurance = 0
        self.take_split = 0
        self.split_hand = []
        self.split_bet = 0
        self.take_double = False
        self.move = []

class Button:
    def __init__(self, position, txt, lightcol, col, darkcol, size, border):
        self.position = position
        self.txt = txt
        self.lightcol = lightcol
        self.darkcol = darkcol
        self.col = col
        self.size = size #  [width, height]
        self.border = border #bool


    def create(self, screen, txt_size, border_size = 5):
        '''Function creates button. It gets lighter if mouse is on it (LIGHTCOL).
        Text and border are in DARKCOL. Text is centralised. Button is in COL. '''
        width = self.size[0]
        height = self.size[1]
        position = self.position

        col = self.col
        darkcol = self.darkcol
        lightcol = self.lightcol

        pygame.draw.rect(screen, col, (position[0], position[1], width, height))

        # Lighter whene mouse is on button
        mouse = pygame.mouse.get_pos()
        if  position[0] <= mouse[0] <= width + position[0] and position[1] <= mouse[1] <= height + position[1]:
            pygame.draw.rect(screen, lightcol, (position[0], position[1], width, height))

        # Create border
        if self.border:
            pygame.draw.rect(screen, darkcol, (position[0], position[1], width, height), border_size)


        # Define button text 
        text_font = pygame.font.SysFont('Bungee', txt_size)
        text_surface = text_font.render(self.txt, True, darkcol)
        w = text_surface.get_width()
        h = text_surface.get_height()

        first = text_font.render(self.txt, TRUE, darkcol)
 
        screen.blit(first, (position[0] + (width - w)/2, position[1] + (height -h)/2))


class InputBox:   
    '''the main code for this class comes from https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
    I have made some alternations.'''

    def __init__(self, x, y, w, h, text='', text_size = 50, col=[LIGHTPINK, DARKPINK, OFFWHITE], napaka = 0, txtcol = WRITING):
        self.rect = pygame.Rect(x, y, w, h)
        self.col = col
        self.color = col[0]
        self.text = text
        self.text_font = pygame.font.SysFont('Bungee', text_size)
        self.txt_surface = self.text_font.render(text, True, self.color)
        self.active = False
        self.napaka = napaka
        self.txtcol = txtcol

    def handle_event(self, event, screen, game, bet = False):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.col[1] if self.active else self.col[0]
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                    try:
                        money = float(self.text)
                        self.napaka = 0
                        if bet and game.balance < money:
                            # write error
                            self.napaka = 2
                    except:
                        # Write warning
                        self.napaka = 1 

                        # Set input to ''
                        self.text = ''

                # Re-render the text.
                self.txt_surface = self.text_font.render(self.text, TRUE, self.txtcol)

                    

    def update(self):
        # Resize the box if the text is too long.
        width = max(300, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

