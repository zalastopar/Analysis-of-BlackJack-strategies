

import functions.classes as classes
import random


a = [classes.Card('S', 6, [0,0]), classes.Card('S', 6, [0,0]), classes.Card('S', 11, [0,0])]





def random_card(game):
    c = game.deck.pop(1)
    sui = c[0]
    c = c[1:]
    val = int(c)
    return sui, val
        


