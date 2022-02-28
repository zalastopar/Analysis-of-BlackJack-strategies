import pygame_textinput
import pygame
pygame.init()
import sys
import pygame.locals as pl
from pickle import TRUE


# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (60,179,113)
PINK = (216, 0, 115)
TEAL = (0, 128, 128)
DARKPINK = (102, 0, 51)
DARKTEAL = (0,73,83)
LIGHTTEAL = (95,158,160)
LIGHTPINK = (250, 12, 139)

width = 1600
height = 900
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(PINK)



def input(events, position):
    base_font = pygame.font.Font(None, 32)
    
    gameDisplay.fill(PINK)

    txt = textinput.value

    # Make text look pretty
    textinput.font_color = WHITE
    textinput.cursor_color = DARKPINK
    text_surface = base_font.render(txt, True, DARKPINK)

    # Change rect size
    s = text_surface.get_width()
    position[2] = max(100, s + s/3)
    pygame.draw.rect(gameDisplay, LIGHTPINK, position)

    
    # Only integers allowed and save value
    money = 0
    try:
        money = float(txt)
    except:
        print(len(txt))
        # Write warning
        text_font = pygame.font.SysFont('Bungee', 30)
        warning = text_font.render('Amount must be a number!', TRUE, WHITE)
        pygame.draw.rect(gameDisplay, LIGHTPINK, [position[0], position[1], 10+ warning.get_width(), position[3]])
        gameDisplay.blit(warning, (position[0], position[1] + 5))

        # Set input to ''
        textinput.value = ''


    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    gameDisplay.blit(textinput.surface, (position[0], position[1]))

    pygame.display.flip()
    return(money)

'''
while True:

    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    money = input(events, position1)


    pygame.display.update()

'''
