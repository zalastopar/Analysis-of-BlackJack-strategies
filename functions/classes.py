from pickle import TRUE
import os.path
import pygame
from pygame.locals import *



# Setting up color objects
OFFWHITE = (241, 235, 219)
WRITING = (206, 183, 127)









# game
class Game:
    def __init__(self, simulation, position, help, balance, deck):
        self.simulation = simulation # save as int how many 0 to inf
        self.position = position # which window is open
        self.help = help # TRUE or FALSE ################################################# popravi v window
        self.balance = balance
        self.deck = deck # dict of cards that already happened - currently we play with 6 decks
        self.dealer_position = [500, 70]
        self.player_position = [500, 500]

        

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
        pygame.draw.rect(screen, WRITING, (self.position[0], self.position[1], 200, 320), 5, 6)

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
        text_font = pygame.font.SysFont('Bungee', 220)
        text_surface = text_font.render(sign, True, WRITING)
        w = text_surface.get_width()
        h = text_surface.get_height()


        value = text_font.render(sign, TRUE, WRITING)
        screen.blit(value, (self.position[0] - w/2 + 200/2, self.position[1] + 320/2 - h/2))


        # Write suits on cards
        s = self.suit
        if s == 'C':
            s = 'CLUB'
        elif s == 'H':
            s = 'HEART'
        elif s == 'D':
            s = 'DIAMOND'
        elif s == 'S':
            s = 'SPADE'

        text_font = pygame.font.SysFont('Bungee', 45)
        text_surface = text_font.render(s, True, WRITING)
        wi = text_surface.get_width()
        hi = text_surface.get_height()
        c_suit = value = text_font.render(s, TRUE, WRITING)
        screen.blit(c_suit, (self.position[0] - wi/2 + 200/2, self.position[1] + 320/2 + h/2 -20))

        '''
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
        image = pygame.transform.scale(image, (width*0.05, height*0.05))
        width, height = image.get_width(), image.get_height()
        screen.blit(image, (self.position[0] + 8, self.position[1] + h + 5))
        #screen.blit(image, (self.position[0] - width/2 + 200/2, self.position[1] + 320/2 + h/2 ))

        # self.position[1] - (self.position[1] + 320/2 - h/2)/2 - height/2

        '''

    def card_back(self, screen):
        # Blank card
        pygame.draw.rect(screen, OFFWHITE, (self.position[0], self.position[1], 200, 320), border_radius=6)
        pygame.draw.rect(screen, WRITING, (self.position[0], self.position[1], 200, 320), 5, 6)


        # Add Kitten
        path = os.path.join("suits/2.png")
        image = pygame.image.load(path)

        width, height = image.get_width(), image.get_height()

        image = pygame.transform.scale(image, (width*0.35, height*0.35))
        width, height = image.get_width(), image.get_height()
        screen.blit(image, (self.position[0] + (200-width)/2, self.position[1] + (320 - height)/2))



class Hand:
    def __init__(self, bet, hand, dealer_hand, insurance, double, split, winnings):
        self.bet = bet # float
        self.player_hand = hand # sez with cards
        self.dealer_hand = dealer_hand # sez with player cards
        self.take_insurance = insurance # bool - if player decided for an insurance
        self.take_split = split # bool - if player splited
        self.take_double = double # bool - if player doubled
        self.winnings = winnings

    def __repr__(self):
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def __str__(self) -> str:
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def hand_value(self, who): # who 'D' for deaker and 'P' for player
        '''The function takes a list of cards and calculates its value'''
        if who == 'D':
            cards = self.dealer_hand
        else:
            cards = self.player_hand
            
        hand = []
        # remove suit and only look at value
        for card in cards:
            val = card.real_value()
            hand.append(val)

        hand_value = 0
        soft = False

        if 11 in hand: # 11 ali 1??????????? zapis
            '''Ace can count as 11 or as 1. There can be only 1 ace in hand that counts as 11
            otherwise hand value would be > 22. So max 1 ace counts as 11 and other as 1.'''
            ace = hand.count(11)
            hand = [value for value in hand if value != 11]
            val = sum(hand) 
            val = val + ace # firstly count all aces as one
            if val + 10 <= 21:
                val = val + 10 # if it is possible count one ace as 11
                soft = True
            hand_value = val
        else:
            hand_value = sum(hand)

        return(hand_value, soft)

    def split(self):
        s = False
        hand = self.player_hand
        if len(hand) == 2 and hand[0].real_value() == hand[1].real_value():
            s = True
        return s

    def double(self):
        d = False
        hand = self.player_hand
        if len(hand) == 2:
            d = True
        return d
    
    def insurance(self):
        hand = self.dealer_hand[0]
        if hand.value == 11:
            return True
        else:
            return False

    def hit(self):    # goes also for stand
        val, k = self.hand_value('P')
        if val > 21:
            return False
        return True
            
    def BlackJack(self, who): # who can be either 'D' (dealer) or 'P' player
        if who == 'D':
            hand = self.dealer_hand
            if len(hand) != 2:
                return False
        else:
            hand = self.player_hand
        first = hand[0]
        second= hand[1]
        if len(hand) == 2 and [first.real_value(), second.real_value()] == [10, 11]:
            return True
        elif  len(hand) == 2 and [first.real_value(), second.real_value()] == [11, 10]:
            return True
 
    def who_wins(self):
        winnings = 0
        dealer, k = self.hand_value('D')
        player, k = self.hand_value('P')
        if self.BlackJack('P'):
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
            

        
class Button:
    def __init__(self, position, txt, lightcol, col, darkcol, size, border):
        self.position = position
        self.txt = txt
        self.lightcol = lightcol
        self.darkcol = darkcol
        self.col = col
        self.size = size #  [width, height]
        self.border = border #bool


    def create(self, screen, txt_size):
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
            pygame.draw.rect(screen, darkcol, (position[0], position[1], width, height), 5)


        # Define button text 
        text_font = pygame.font.SysFont('Bungee', txt_size)
        text_surface = text_font.render(self.txt, True, darkcol)
        w = text_surface.get_width()
        h = text_surface.get_height()

        first = text_font.render(self.txt, TRUE, darkcol)
 
        screen.blit(first, (position[0] + (width - w)/2, position[1] + (height -h)/2))


    
