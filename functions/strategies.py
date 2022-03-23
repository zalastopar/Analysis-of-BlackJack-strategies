
# https://www.legitgamblingsites.com/blog/how-to-best-take-advantage-of-streaks-in-blackjack/



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

    def __init__(self, winning_streak, bet, length):
        self.winning_streak = winning_streak
        self.bet = bet
        self.length = length

    def set_bet(self, game):
        bet = 0
        if self.winning_streak >= 3:
            bet = game.initial_bet
        elif self.winning_streak == 2 or self.winning_streak == 1:
            bet = self.bet*2
        else:
            bet = game.initial_bet
        
        self.bet = bet
        game.balance = game.balance - self.bet


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
    def __init__(self) -> None:
        pass

class oscar:
    '''
    Oscar’s Grind is a fairly complicated strategy that involves increasing your bets following a losing streak.
    You start out by choosing a unit size, such as $10 or $20. You then wager one unit until you run into a losing streak.
    As soon as your losing streak ends, you increase your bet size by one unit. This continues until you’ve earned a one-unit profit.
    My favorite thing about Oscar’s Grind is that you don’t have to risk much money after a losing streak. 
    This allows you to win back your money in a more conservative manner.
    The drawback is that some blackjack players won’t be happy with how slowly this system works.
    '''

    def __init__(self) -> None:
        pass
