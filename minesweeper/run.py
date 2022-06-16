from minesweeper import Minesweeper


def run():
    """ Minesweeper. """
    run = Minesweeper()

    while True:
        # Starting the game.
        run.start_game()
        # Requesting user input.
        run.restart()

        continue


if __name__ == '__main__':
    run()
