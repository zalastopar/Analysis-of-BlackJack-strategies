# deal cards
# compare hand to dealer

import functions.classes as classes
import random


a = [classes.Card('S', 6, [0,0]), classes.Card('S', 13, [0,0]), classes.Card('S', 11, [0,0])]


def hand_value(sez):
    '''The function takes a list of cards and calculates its value'''
    hand = []
    # remove suit and only look at value
    for card in sez:
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


def random_card(game):
    print(game.deck)
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
    
