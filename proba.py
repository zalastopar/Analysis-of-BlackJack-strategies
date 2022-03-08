import pygame as pygame
from pickle import TRUE


pygame.init()
screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


TEAL = (0, 128, 128)
DARKPINK = (102, 0, 51)
DARKTEAL = (0,73,83)
LIGHTTEAL = (95,158,160)
LIGHTPINK = (250, 12, 139)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = TEAL
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = LIGHTPINK if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                    try:
                        money = float(self.text)
                        napaka = False
                        # Delete warning
                        text_font = pygame.font.SysFont('Bungee', 30)
                        warning = text_font.render('Your amount must be a number!', TRUE, TEAL)
                        pygame.draw.rect(screen, TEAL, [100, 100, 10 + warning.get_width(), 30])
                        
                        '''
                        if game.balance < money:
                            # Write warning
                            text_font = pygame.font.SysFont('Bungee', 30)
                            warning = text_font.render("You can't bet more than you have!", TRUE, DARKTEAL)
                            screen.blit(warning, (100, 200))
                        else:
                            hand.bet = money
                        '''
                    except:
                        napaka = True
                        if napaka:
                            text_font = pygame.font.SysFont('Bungee', 30)
                            warning = text_font.render('Your amount must be a number!', TRUE, TEAL)
                            screen.blit(warning, (500, 500))
                        # Set input to ''
                        self.text = ''

                        



                    #self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(300, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()
