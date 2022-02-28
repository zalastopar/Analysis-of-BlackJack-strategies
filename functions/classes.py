from pickle import TRUE
#from turtle import position
import pygame
from pygame.locals import *

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

OFFWHITE = (241, 235, 219)
WRITING = (206, 183, 127)


# game
class Game:
    def __init__(self, simulation, position, help):
        self.simulation = simulation # save as int how many 0 to inf
        self.position = position # which window is open
        self.help = help # 0 if without help, 1 if with help


# player
class Player:
    def __init__(self, balance, bet):
        self.balance = balance  # float
        self.bet = bet  # float

# card
class Card:
    def __init__(self, suit, value, position) -> None:
        self.suit = suit # suit of the card
        self.value = value # numbar of the card
        self.position = position #position of the card on the table (x, y)




        

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


        # Draw value to card
        text_font = pygame.font.SysFont('Bungee', 200)
        text_surface = text_font.render(sign, True, WRITING)
        w = text_surface.get_width()
        h = text_surface.get_height()
        
        image = pygame.image.load('racecar.png')
        screen.blit(image, (0, 0))

        value = text_font.render(sign, TRUE, WRITING)
        screen.blit(value, (self.position[0] - w/2 + 200/2, self.position[1] + 320/2 - h/2))

    