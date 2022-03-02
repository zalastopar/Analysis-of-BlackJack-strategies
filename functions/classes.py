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

    '''
    def __repr__(self):
        return 'Simulation: ' + str(self.simulation) + '\nHelp: ' + str(self.help) + '\nBalace: ' + str(self.balance)

    def __init__(self):
        return 'Simulation: ' + str(self.simulation) + '\nHelp: ' + str(self.help) + '\nBalace: ' + str(self.balance)
    '''
        

# card
class Card:
    def __init__(self, suit, value, position) -> None:
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



class Hand:
    def __init__(self, bet, hand, dealer_hand, round):
        self.bet = bet # float
        self.player_hand = hand # sez with cards
        self.dealer_hand = dealer_hand # sez with player cards
        self.round = round

    def __repr__(self):
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def __str__(self) -> str:
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

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

    
