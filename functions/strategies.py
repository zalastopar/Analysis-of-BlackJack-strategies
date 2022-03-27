
# https://www.legitgamblingsites.com/blog/how-to-best-take-advantage-of-streaks-in-blackjack/
import random


class paroli:

    '''
    The Paroli system is one of the easiest positive progression strategies to use. 
    You begin by determining a fixed betting unit.
    Ideally, this amount will be worth 2% to 5% of your bankroll. 
    For example, if your bankroll is worth $500, you can use a $10 betting unit.
    The Paroli works by doubling your betting unit after every win. 
    You then stop after three wins and return to the original stake.
    Some players like going to 4-5 wins before returning to the original bet, 
    but this is risky because we already covered that your chances of winning 
    four straight hands are less than 10%.
    The nice thing about the Paroli system is that you win more during hot streaks 
    without being too risky. The trouble, though, is that you only have a 10.6% 
    chance of winning a three hand sequence.
    '''

    def __init__(self, winning_streak, bet):
        self.winning_streak = winning_streak
        self.bet = bet

    def set_bet(self, game):
        bet = 0
        if self.winning_streak >= 3:
            bet = game.initial_bet
        elif self.winning_streak == 2 or self.winning_streak == 1:
            bet = self.bet*2
        else:
            bet = game.initial_bet
        
        self.bet = bet

class system1326:
    '''
    The 1 3 2 6 strategy isn’t as popular as the Paroli, 
    but it’s still a simple positive progression strategy that can bring you big winnings.
    This system begins with choosing a fixed betting unit. 
    And just like with the Paroli, 2% to 5% of your bankroll is a good unit size.
    Each number in the 1 3 2 6 system represents how many betting units you risk in the sequence. 
    In other words, you bet one unit, followed by three units, two units, and six units.
    You start a fresh sequence every time you lose a bet or win four straight wagers.
    The primary advantage of the 1 3 2 6 strategy is that you can book profits even 
    if you don’t complete the sequence. The downside is that 
    you’ll rarely win four blackjack hands in a row and reach the end of the betting string.
    '''

    def __init__(self, winning_streak, bet, round) -> None:
        self.winning_streak = winning_streak
        self.bet = bet
        self.round = round

    def set_bet(self, game):
        bet = 0
        if self.winning_streak > 0:
            if self.round == 1:
                bet = game.initial_bet*3
                self.round = 3
            elif self.round == 3:
                bet = game.initial_bet*2
                self.round = 2
            elif self.round == 2:
                bet = game.initial_bet*6
                self.round = 6
            elif self.round == 6:
                bet = game.initial_bet*1
                self.round = 1
        else:
            bet = game.initial_bet
            self.round = 1
        self.bet = bet

class reverse_lab:
    '''
    The reverse Labouchere system is one of the most complicated gambling strategies. 
    But you should still be able to pick up this system within a few minutes.
    The reverse Labouchere starts with creating a sequence of numbers. 
    The numbers should add up to your desired profit for the betting string.
    You then add the first and last number in the sequence to determine your next bet.
    If you win the wager, you add the combined amount to the end of your sequence. 
    After a loss, you cross off both numbers and continue to the next wager.
    You start over with a new sequence whenever completing the number string.
    The drawback to this strategy is that it normally takes a while to complete your betting sequence. 
    But the upside is that you can win solid profits after completing the number string.
    '''
    def __init__(self, profit, seq, winning_streak, bet):
        self.profit = profit #number wanted profit (int)
        self.seq = seq # sequence of betting int
        self.winning_streak = winning_streak
        self.bet = bet


    def create_seq(self):
        p = self.profit
        seq = []
        first = 0
        while p > 0:
            first = random.randint(1, p)
            seq.append(first)
            p = p-first
        self.seq = seq
            
    
    def set_bet(self, game):
        self.bet = 0
        # if sequence is empty, create new one
        if len(self.seq) == 0:
            self.create_seq()
            print('dolzina 0')
            if len(self.seq) == 1:
                bet = self.seq[0]
            else:
                bet = self.seq[0] + self.seq[-1]
        else: 
            if self.winning_streak > 0:
                print('w')
                if len(self.seq) == 1:
                    self.seq = self.seq + [self.seq[0]]
                else:
                    print('else')
                    self.seq = self.seq + [self.seq[0] + self.seq[-1]]
                bet = self.seq[0] + self.seq[-1]
            else:
                if len(self.seq) == 1 or len(self.seq) == 2:
                    self.create_seq()
                    print('dolzina 0')
                    if len(self.seq) == 1:
                        bet = self.seq[0]
                    else:
                        bet = self.seq[0] + self.seq[-1]
                else:
                    self.seq = self.seq[1:-1]
                    if len(self.seq) == 1:
                        bet = self.seq[0]
                    else:
                        bet = self.seq[0] + self.seq[-1]
        print(self.seq)
        print(bet)
        
        self.bet = bet

class one_half_increase:
    '''
    The one half increase system is aptly named, 
    because you increase your betting unit by one half after a two-hand winning streak. 
    You continue this half unit increase for every subsequent win.
    The one half increase is my favorite positive progression system, 
    because it allows you to capitalize on win streaks without risking the majority of your profits.
    '''
    def __init__(self, winning_streak, bet):
        self.winning_streak = winning_streak
        self.bet = bet

    def set_bet(self, game):
        initial = game.initial_bet
        bet = 0
        if self.winning_streak <= 1:
            bet = initial
        elif self.winning_streak >= 2:
            bet = initial + initial/2*(self.winning_streak - 1)
        self.bet = bet


############################################3 card counting

class martingale:
    '''
    The Martingale is easy to use because the only requirement involves doubling bets after every loss.
    You start off by wagering the table minimum. 
    You double this amount every time you lose, and return to the table minimum after any win.
    The upside is that this system actually gives you an advantage in theory. 
    As long as you always win to end a losing streak, you’ll earn back your losses plus a small profit.
    The major downside is that you can lose your entire bankroll during long losing runs. 
    Another problem is that you’ll eventually hit the table betting limit if you lose enough hands.
    This is why I suggest finding tables with a low minimum bet and generous max wager if you’re going to use the Martingale.
    '''
    def __init__(self, losing_streak, bet):
        self.losing_streak = losing_streak
        self.bet = bet

    def set_bet(self, game):
        if self.losing_streak == 0:
            bet = game.initial_bet
        else:
            bet = self.bet*2
        self.bet = bet

class oscars_grind:
    '''
    Oscar’s Grind is a fairly complicated strategy that involves increasing your bets following a losing streak.
    You start out by choosing a unit size, such as $10 or $20. You then wager one unit until you run into a losing streak.
    As soon as your losing streak ends, you increase your bet size by one unit. This continues until you’ve earned a one-unit profit.
    My favorite thing about Oscar’s Grind is that you don’t have to risk much money after a losing streak. 
    This allows you to win back your money in a more conservative manner.
    The drawback is that some blackjack players won’t be happy with how slowly this system works.
    '''

    def __init__(self, unit, bet, losing_streak, bankroll):
        self.unit = unit
        self.bet = bet
        self.losing_streak = losing_streak
        self.bankroll = bankroll

    def set_bet(self, game):
        print(self.bet)
        if self.bet == 0:
            self.bet = self.unit
        else:
            if self.losing_streak > 0:
                self.bankroll = self.bankroll - 1
                #bet stays the same
            else:
                if self.bankroll == 0: # we won so it is acutaly 1
                    # back to begining
                    self.bankroll = 0
                    self.bet = self.unit
                else:
                    self.bankroll += 1
                    self.bet = self.bet + self.unit
