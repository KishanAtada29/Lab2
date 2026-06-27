""" 
Program Name: Coin
Name: Kishan Atada
Purpose: This program defines a Coin class that represents one tossable coin.
Starter code: No starter code is used
Resources: Uses Python's random module to randomly choose Heads or Tails. 
Date: 2026-06-27 
"""
import random

class Coin:
    """Represents a single tossable coin."""

    def __init__(self):
        """Initialize the coin with Heads facing up."""
        self.__sideup = "Head"
    
    def toss(self):
        """Randomly toss the coin and set it to Heads or Tails."""
        if random.randint(0,1) == 1:
            self.__sideup = "Tails"
        else:
            self.__sideup = "Heads"
    
    def get_sideup(self):
        """Return the current side of the coin."""
        return self.__sideup