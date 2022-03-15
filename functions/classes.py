from pickle import TRUE
import os.path
import pygame
from pygame.locals import *




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

        '''
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
    def __init__(self, bet, hand, dealer_hand, insurance, double, split, split_hand, winnings, split_bet):
        self.bet = bet # float
        self.player_hand = hand # sez with cards
        self.dealer_hand = dealer_hand # sez with player cards
        self.take_insurance = insurance # num, how much is insurance
        self.take_split = split # 0 - if not split, 1-dealing first hand, 2-dealing 2nd hand 
        self.split_hand = split_hand
        self.take_double = double # bool - if player doubled
        self.winnings = winnings
        self.split_bet = split_bet

    def __repr__(self):
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def __str__(self) -> str:
        return 'Bet: ' + str(self.bet) + '\nPlayer:' + str(self.player_hand) + '\nDealer: ' + str(self.dealer_hand)

    def hand_value(self, who): # who 'D' for deaker and 'P' for player 'S' split hand
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
        if game.balance >= self.bet/2:
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
        if self.BlackJack(who):
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

