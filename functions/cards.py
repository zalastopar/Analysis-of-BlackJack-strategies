

import functions.classes as classes
import random


a = [classes.Card('S', 6, [0,0]), classes.Card('S', 6, [0,0]), classes.Card('S', 11, [0,0])]





def random_card(game):
    suits = ['S', 'H', 'D', 'C']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # get random values
    sui = random.choice(suits)
    val = random.choice(values)
    c = sui + str(val)
    # check if we have already used all cards
    if c in game.deck.keys(): 
        if game.deck[c] < 6:
            game.deck[c] = game.deck[c] + 1
            return sui, val
        else:
            random_card(game) # new random card
    else:
        game.deck[c] = 1
        return sui, val
        

        



# situation
# hit
# stand
# double
# split
''' spada bolj pod windows
def deal_cards(hand, game):
    # ze prej naredimo nov hand: bet kolikor je, tukaj dodamo ostalo

    #ena random karta igralcu, ena dealerju in se ena igralcu
    # pazis kere karte so ze ble
    player_position = [0, 0] ############################
    sui, val = random_card(game)
    hand.player_hand.append(sui, val, player_position)

    #dealer hand
    dealer_position = [0,0] ########################
    sui, val = random_card(game)
    hand.dealer_hand.append(sui, val, dealer_positions)

    # 2nd player card
    sui, val = random_card(game)
    hand.player_hand.append(sui, val, player_position + [0, 100])


'''
    
