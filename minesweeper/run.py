from sys import exit

from minesweeper import Minesweeper


def run():
    """Minesweeper."""
    run = Minesweeper()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        exit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
