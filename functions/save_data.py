from numpy import NaN
import functions.classes as classes
import pandas as pd
import os.path

def save_bet_sim(hand, game):
    sim = game.sim
    if sim not in game.data_bet.keys():
        game.data_bet[sim] = []
    game.data_bet[sim].append(hand.bet + hand.split_bet)

def save_simulation(hand, game):
    sim = game.sim
    # balance 
    if sim not in game.data_balance.keys():
        game.data_balance[sim] = [game.balance]
    else:
        game.data_balance[sim].append(game.balance)
    


    #self.data_multiple = data_multiple
    # data 0x
    if sim not in game.data_multiple['data_0x'].keys():
        if game.balance == 0: 
            game.data_multiple['data_0x'][sim] = game.length
        if (sim - 1) not in game.data_multiple['data_0x'].keys() and (sim - 1) != 0 and sim != 0:
            game.data_multiple['data_0x'][sim-1] = 0

    # data 3x
    if sim not in game.data_multiple['data_3x'].keys(): # not yet to 300
        if game.balance >= 3*game.initial_balance: # startin balance = 100
            game.data_multiple['data_3x'][sim] = game.length
        if (sim - 1) not in game.data_multiple['data_3x'].keys() and (sim - 1) != 0 and sim != 0:
            game.data_multiple['data_3x'][sim-1] = 0

    # data 5x
    if sim not in game.data_multiple['data_5x'].keys(): # not yet to 500
        if game.balance >= 5*game.initial_balance: # startin balance = 100
            game.data_multiple['data_5x'][sim] = game.length
        if (sim - 1) not in game.data_multiple['data_5x'].keys() and (sim - 1) != 0 and sim != 0:
            game.data_multiple['data_5x'][sim-1] = 0

    # data 10x
    if sim not in game.data_multiple['data_10x'].keys(): # not yet to 1000
        if game.balance >= 10*game.initial_balance: # startin balance = 100
            game.data_multiple['data_10x'][sim] = game.length
        if (sim - 1) not in game.data_multiple['data_10x'].keys() and (sim - 1) != 0 and sim != 0:
            game.data_multiple['data_10x'][sim-1] = 0

    
def save_prob(hand, game):
    # a izenacenje stejemo?
    # ni split
    winnings = hand.who_wins('P')
    dealer = hand.dealer_hand[0].real_value()

    # check for soft hand
    # game.soft_data
    if 11 == hand.player_hand[0].real_value() or 11 == hand.player_hand[1].real_value(): # ace is first or second card
        if 11 == hand.player_hand[0].real_value():
            second = hand.player_hand[1].real_value()
        else: 
            second = hand.player_hand[0].real_value()

        if winnings > 1: # player wins
            if second in game.soft_data.keys(): # player value exists
                if dealer in game.soft_data[second].keys(): # dealer value exists
                    game.soft_data[second][dealer][0] += 1
                    game.soft_data[second][dealer][1] += 1
                else: # dealer value doesnt exist
                    game.soft_data[second][dealer] = [1,1]
            else: # player value doesnt exist
                game.soft_data[second] = {}
                game.soft_data[second][dealer] = [1,1]
        else: # player loses
            if second in game.soft_data.keys(): # player value exists
                if dealer in game.soft_data[second].keys(): # dealer value exists
                    game.soft_data[second][dealer][1] += 1
                else: # dealer value doesnt exist
                    game.soft_data[second][dealer] = [0, 1]
            else: # player value doesnt exist
                game.soft_data[second] = {}
                game.soft_data[second][dealer] = [0, 1]

    # check for split
    # game.split_data
    if hand.split_bet > 0: # it was split
        card_value = hand.player_hand[0].real_value()

        if hand.winnings > hand.bet + hand.split_bet: # player wins
            if card_value in game.split_data.keys(): # player value exists
                if dealer in game.split_data[card_value].keys(): # dealer value exists
                    game.split_data[card_value][dealer][0] += 1
                    game.split_data[card_value][dealer][1] += 1
                else: # dealer value doesnt exist
                    game.split_data[card_value][dealer] = [1, 1]
            else: # player value doesnt exist
                game.split_data[card_value] = {}
                game.split_data[card_value][dealer] = [1, 1]
        else: # player loses
            if card_value in game.split_data.keys(): # player value exists
                if dealer in game.split_data[card_value].keys(): # dealer value exists
                    game.split_data[card_value][dealer][1] += 1
                else: # dealer value doesnt exist
                    game.split_data[card_value][dealer] = [0, 1]
            else: # player value doesnt exist
                game.split_data[card_value] = {}
                game.split_data[card_value][dealer] = [0, 1]

    # game.prob_data
    if hand.split_bet > 0: # save normal data from split hand
        length = len(hand.split_hand)
        player = hand.split_hand
        winnings = hand.who_wins('S')

        for i in range(2,length+1): # 2, 3, 4, ... len-1
            temp_hand = classes.Hand(0, [], [], 0, False, False, [], 0, 0, []) #  create temporary hand to calculate real value
            for j in range(i): # 0, 1, ... i-1
                temp_hand.player_hand.append(player[j])
            hand_val, k = temp_hand.hand_value('P')

            #print(hand_val)
            #print(dealer)
            if winnings > 1: # we win
                if hand_val in game.prob_data.keys(): # player value exists
                    if dealer in game.prob_data[hand_val].keys(): # dealer value exists
                        game.prob_data[hand_val][dealer][0] +=1 
                        game.prob_data[hand_val][dealer][1] +=1 
                    else: # dealer value doesnt exist
                        game.prob_data[hand_val][dealer] = [1,1]
                else: # player value doesnt exist
                    game.prob_data[hand_val]= {}
                    game.prob_data[hand_val][dealer] = [1,1]
            else: # we lose
                if hand_val in game.prob_data.keys(): # player value exists
                    if dealer in game.prob_data[hand_val].keys(): # dealer value exists
                        game.prob_data[hand_val][dealer][1] +=1 
                    else: # dealer doesnt exist
                        game.prob_data[hand_val][dealer] = [0,1]
                else:  # player doesnt exist
                    game.prob_data[hand_val]= {}
                    game.prob_data[hand_val][dealer] = [0,1]


    length = len(hand.player_hand)
    player = hand.player_hand
    winnings = hand.who_wins('P')

    # normal hand - including soft 
    for i in range(2,length+1): # 2, 3, 4, ... len-1
        temp_hand = classes.Hand(0, [], [], 0, False, False, [], 0, 0, []) #  create temporary hand to calculate real value
        for j in range(i): # 0, 1, ... i-1
            temp_hand.player_hand.append(player[j])
        hand_val, k = temp_hand.hand_value('P')

        #print(hand_val)
        #print(dealer)
        if winnings > 1: # we win
            if hand_val in game.prob_data.keys(): # player value exists
                if dealer in game.prob_data[hand_val].keys(): # dealer value exists
                    game.prob_data[hand_val][dealer][0] +=1 
                    game.prob_data[hand_val][dealer][1] +=1 
                else: # dealer value doesnt exist
                    game.prob_data[hand_val][dealer] = [1,1]
            else: # player value doesnt exist
                game.prob_data[hand_val]= {}
                game.prob_data[hand_val][dealer] = [1,1]
        else: # we lose
            if hand_val in game.prob_data.keys(): # player value exists
                if dealer in game.prob_data[hand_val].keys(): # dealer value exists
                    game.prob_data[hand_val][dealer][1] +=1 
                else: # dealer doesnt exist
                    game.prob_data[hand_val][dealer] = [0,1]
            else:  # player doesnt exist
                game.prob_data[hand_val]= {}
                game.prob_data[hand_val][dealer] = [0,1]

def nicer_dict(dict):
    new_dict = {}
    for player in dict.keys():
        new_dict[int(player)] = {}
        for dealer in dict[player].keys():
            if dict[player][dealer] != dict[player][dealer]:
                pass
            else:
                sez = dict[player][dealer][1:-1]
                sez = [int(x) for x in list(sez.split(", "))]
                new_dict[int(player)][dealer] = sez
    return new_dict

def combine_dict(old, new):
    updated = old
    for player in new.keys():
        if player in old.keys(): # player exists
            for dealer in new[player].keys():
                if dealer in old[player].keys(): # dealer exists
                    sez = [old[player][dealer][0] + new[player][dealer][0], old[player][dealer][1] + new[player][dealer][1]]
                    updated[player][dealer] = sez
                else: # dealer doest exist
                    updated[player][dealer] = new[player][dealer]
        else: # player doest exist
            updated[player] = new[player]
    return updated


def update_csv_prob(new_dict, csv_file):
    # check if old data exists
    if not os.path.exists(csv_file):
        pd.DataFrame({}).to_csv(csv_file)
        old_dict = {}
    else: 
        # get old data
        df = pd.read_csv(csv_file, index_col = 0) 
        old_dict = nicer_dict(df.to_dict())
    # merge data
    updated = combine_dict(old_dict, new_dict)
    # save as csv
    df = pd.DataFrame(updated)
    df.to_csv(csv_file)
    #print('old')
    #print(old_dict)
    #print('new')
    #print(new_dict)
    #print('combined')
    #print(updated)
