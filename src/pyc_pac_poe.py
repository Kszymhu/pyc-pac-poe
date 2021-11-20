"""Command line tic-tac-toe game.
"""

from board_data import BoardData
from board_logic import BoardLogic as logic
from board_graphics import BoardGraphics as graphics
from input_parser import InputParser as input_parser

def ask_for_valid_move(data: BoardData, prompt: str, failed_message: str) -> list[int]:
    """Asks the user for a valid move until either the flesh, or the machine breaks.
    """

    coords = input_parser.ask_for_cs_int_pair(prompt, failed_message)

    if logic.is_move_valid(data, coords[0] - 1, coords[1] - 1):
        return coords

    return ask_for_valid_move(data, prompt, failed_message)


def player_turn(player, data):
    """Calculates the turn of a given player.
    """

    print("Player {0}'s turn.".format(player))

    prompt = "Your move: (row, column) "
    failed_message = "Please input a valid integer pair. (a, b)"
    coords = ask_for_valid_move(data, prompt, failed_message)

    logic.execute_move(data, coords[0] - 1, coords[1] - 1, player)
    graphics.print(data)

    if logic.is_board_full(data):
        return " "

    winner_candidate = logic.look_for_winner(data)
    if winner_candidate != " ":
        return winner_candidate
    return None


def main():
    """Entry point for the game.
    """

    prompt = "Board size: "
    failed_message = "Please input a valid integer."
    size = input_parser.ask_for_int(prompt, failed_message)

    data = BoardData(size)

    players = input("List of players: (e.g. X, O, 0, *) ").split(", ")

    graphics.print(data)

    while True:
        for player in players:
            result = player_turn(player, data)
            if result is not None:
                if result == " ":
                    print("Game ended in a tie.")
                else:
                    print("{0} has won the game.".format(result))
                return


if __name__ == "__main__":
    main()
