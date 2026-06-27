import coin as c
class Player:
    def __init__(self,name, wallet, coin):
        self._name = name
        self._wallet = wallet
        self._coin = c.Coin()

    def toss_coin(self):
        toss = self._coin.toss()
        return toss

    def get_coin_side(self):
        sideup = self._coin.get_sideup()
        return sideup
    
    def win_coin(self):
        self._wallet += 1

    def lose_coin(self):
        self._wallet -= 1

    def get_wallet(self):
        return self._wallet
    
    def get_name(self):
        return self._name
        