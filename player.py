""" 
Program Name: Player
Name: Kishan Atada 
Purpose: This program defines a Player class for the Coin Match Game.
Starter code: No starter code is us
Resources: Uses the Coin class from coin.py.
Date: 2026-06-27
 """
from coin import Coin
class Player:
    """Represents a player in the Coin Match Game."""

    def __init__(self,name):
        """Initialize the player's name, wallet, and coin."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Toss the player's coin."""
        return self.__coin.toss()

    def get_coin_side(self):
        """Return the current side of the player's coin."""
        return self.__coin.get_sideup()
    
    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Subtract one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the number of coins in the player's wallet."""
        return self.__wallet
    
    def get_name(self):
        """Return the player's name."""
        return self.__name
        