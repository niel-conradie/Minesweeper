from board import Board
from minesweeper import Minesweeper


def run():
    """Minesweeper."""
    run = Minesweeper()

    while True:
        # Display scoreboard.
        run.display_scoreboard()
        # Starting game.
        run.start_game()
        # Add point to round.
        run.add_round()
        # Requesting user input.
        run.restart()

        continue


if __name__ == "__main__":
    run()
