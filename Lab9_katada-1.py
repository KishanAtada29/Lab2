from player import Player

class main:

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    no_play_again = 'n'


    while no_play_again.casefold() != 'n':
        player1.toss_coin()
        player2.toss_coin()

        player1_side = player1.get_coin_side()
        player2_side = player2.get_coin_side()

        print(f"{player1.get_name} tossed {player1_side}")
        print(f"{player2.get_name()} tossed {player2_side}")

        if player1_side == player2_side:
            player1.win_coin()
            player2.lose_coin()
            print(f"{player1.get_name()} wins this round!")

        else:
            player1.lose_coin()
            player2.win_coin()
            print(f"{player1.get_name()} wins this round!")

            

