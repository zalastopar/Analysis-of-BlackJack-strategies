import pygame_textinput
import pygame
pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

screen = pygame.display.set_mode((800, 200))
clock = pygame.time.Clock()

PINK = (216, 0, 115)

while True:
    screen.fill(PINK)
    pygame.draw.rect(screen, TEAL, (width - 1000, height - 600, 400, 100))
    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (100, 10))

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(60)