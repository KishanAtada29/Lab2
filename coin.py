import random
class Coin:
    def __init__(self, sideup):
        self._sideup = sideup
    
    def toss(self):
        self._sideup = random.randint(0,1)
        if self._sideup == 1:
            return 'Head'
        else:
            return 'Tails'
    
    def get_sideup(self):
        return self._sideup