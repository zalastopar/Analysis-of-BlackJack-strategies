def save_data(hand, game):
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
    length = len(hand.player_hand)
    player = hand.player_hand
    dealer = hand.dealer_hand[0].real_value()

    for i in range(2,length+1): # 2, 3, 4, ... len-1
        hand_val = 0
        for j in range(i): # 0, 1, ... i-1
            hand_val = hand_val + player[j].real_value()
        print(hand_val)
        print(dealer)
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


    # normal

    #soft

    # split