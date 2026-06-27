import random
class Coin:
    def __init__(self):
        self.__sideup = "Head"
    
    def toss(self):
        if random.randint(0,1) == 1:
            self.__sideup = "Tails"
        else:
            self.__sideup = "Heads"
    
    def get_sideup(self):
        return self.__sideup