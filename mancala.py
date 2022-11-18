#The game Mancala is one of the oldest games in recorded
#history. You can read more about it here:
#https://www.thesprucecrafts.com/how-to-play-mancala-409424


# The function check_winner takes a 2-dimensional list
# representing a game board.
#
# The function returns one of four strings depending on the values of the list:
#
# - If the game is not over (that is, there are stones
#   in any bucket except for the top-left or bottom-
#   right), return "Keep playing!"
# - If the game is over and the top player wins (that is,
#   there are more stones in top-left than bottom-right),
#   return "Player 1 wins!"
# - If the game is over and the bottom player wins (that
#   is, there are more stones in the bottom-right than
#   the top-left), return "Player 2 wins!"
# - If the game is over but the score is tied (that is,
#   there is an equal number of stones in the top-left
#   and bottom-right), return "Draw!"

def check_winner(scores):

    if sum(scores[0][1:]) != 0 or sum(scores[1][:-1]) != 0:
        return 'Keep playing!'
    sc1 = scores[0][0]
    sc2 = scores[1][-1]

    if sc1 < sc2:
        return 'Player 2 wins!'
    if sc1 > sc2:
        return 'Player 1 wins!'
    return 'Draw!'


keep_playing = [[5, 3, 0, 2, 6, 8, 1], [1, 6, 8, 0, 4, 1, 4]]
player1_wins = [[27, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 21]]
player2_wins = [[16, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 32]]
game_is_tied = [[24, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 24]]
print(check_winner(keep_playing))
print(check_winner(player1_wins))
print(check_winner(player2_wins))
print(check_winner(game_is_tied))
