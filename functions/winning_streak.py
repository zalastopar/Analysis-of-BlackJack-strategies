'''
Parole system - you increase your bet after every win. 
For example, after you win the first game where you bet $15, you now bet $30. 
If you win the second game, you bet double or $60 on the third. 
However, if you win the third, you do not go $120 but down to the original $15 and 
start again, ensuring you never lose too much and walking away with hefty prize money.
'''



# drugacen hand

#hand.hit  True False
# funkcija hand.ai_hit pogleda ce hit al ne
# double  pr 10 in 11
# split - 8 in 11?

# create decision grid



def winning_streak(game, hand):
    bet = 0
    if hand.winning_streak >= 3:
        bet = game.initial_bet
    elif hand.winning_streak == 2 or hand.winning_streak == 1:
        bet = hand.bet*2
    else:
        bet = game.initial_bet

    hand.bet = bet
    game.balance = game.balance - hand.bet

    hand.player_hand = []
    hand.dealer_hand = []
    hand.winnings = 0
    hand.take_insurance = 0
    hand.take_split = 0
    hand.split_hand = []
    hand.split_bet = 0
    hand.take_double = False

'''
zacnes z balancom
stavis recimo 1/10
ce zmagas x2
sicer se enkrat prvo stavo
ce zmagas 3x zapored nazaj na zacetek
'''
