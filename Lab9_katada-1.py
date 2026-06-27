"""
Program Name: Heads or Tails Game
Name: Kishan Atada 
Purpose: This program runs the Coin Match Game using two Player objects.
Starter code: No starter code is used
Resources: Uses the Player class from player.py.
Date: 2026-06-27 
"""
from player import Player

def main():
    """Run the Coin Match Game."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    play_again = input("Do you want to toss the coins? (y/n): ")


    while play_again.casefold() == 'y':
        player1.toss_coin()
        player2.toss_coin()

        player1_side = player1.get_coin_side()
        player2_side = player2.get_coin_side()

        print('')
        print(f"{player1.get_name()} tossed {player1_side}")
        print(f"{player2.get_name()} tossed {player2_side}")
        print('')

        if player1_side == player2_side:
            player1.win_coin()
            player2.lose_coin()
            print('')
            print(f"{player1.get_name()} wins this round!")
            print(f"...It's a Match! {player1.get_name()} wins a coin.")
            print('')

        else:
            player1.lose_coin()
            player2.win_coin()
            print('')
            print(f"{player1.get_name()} wins this round!")
            print(f"...No Match! {player2.get_name()} wins a coin.")
            print('')

        play_again = input("Do you want to toss the coins? (y/n): ")
    
        print('')
        print("--- Final Score ---")
        print(f"{player1.get_name()}: {player1.get_wallet()}")
        print(f"{player2.get_name()}: {player2.get_wallet()}")

        if player1.get_wallet() > player2.get_wallet():
            print(f"{player1.get_name()} wins!")
        elif player2.get_wallet() > player1.get_wallet():
            print(f"{player2.get_name()} wins!")
        else:
            print("It's a draw!")
main()
