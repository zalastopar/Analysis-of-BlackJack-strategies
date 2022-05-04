import functions.classes as classes

def save_simulation(hand, game):
    '''
    game
        self.sim = sim # number of simulation
        self.data_balance = data_balance # dictionary: key = a number of simulation, value = list of balances after each dealings
        self.data_bet = data_bet # dictionary: key = a number of simulation, value = list of bets
        self.data_0x = data_0x # list: 1 if balcance gets to 0, 0 else
        self.data_3x = data_3x # list: 1 if balance gets to 3x, 0 else
        self.data_5x = data_5x # list: 1 if balance gets to 5x, 0 else
        self.data_10x = data_10x # list: 1 if balance gets to 10x, 0 else
        self.data_to0 = data_to0
    '''
    sim = game.sim

    # balance 
    if sim not in game.data_balance.keys():
        game.data_balance[sim] = [game.balance]
    else: 
        game.data_balance[sim].append(game.balance)
    
    # bet
    if sim not in game.data_bet.keys():
        game.data_bet[sim] = [hand.bet + hand.split_bet]
    else: 
        game.data_bet[sim].append(hand.bet + hand.split_bet)

    
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

        if winnings > hand.bet + hand.split_bet: # player wins
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
