import pygame_textinput
import pygame
pygame.init()

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
gameDisplay.fill(WHITE)

position1 = [1, 2, 100, 30]
def input(events, position):
    gameDisplay.fill(PINK)
    input_rect = pygame.draw.rect(gameDisplay, TEAL, position)

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    gameDisplay.blit(textinput.surface, (position[0], position[1]))

    # Get input text
    input = textinput.value
    s = len(input) 
    input_rect.width = max(20, len(input) + 100)
    pygame.display.flip()
    return(s)

while True:

    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    k  = input(events, position1)
    print(k)
    pygame.display.update()
    clock.tick(60)

