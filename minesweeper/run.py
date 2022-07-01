from minesweeper import Minesweeper


def run():
    """Minesweeper."""
    run = Minesweeper()

    # Display difficulty options.
    run.display_difficulty()
    # Requesting user input.
    user_input = run.user_input()
    # Assign player to appropriate difficulty.
    size, bombs = run.user_input_allocation(user_input)

    while True:
        # Display scoreboard.
        run.display_scoreboard()
        # Starting game.
        run.start_game(size, bombs)
        # Add point to round.
        run.add_round()
        # Requesting user input.
        run.restart()

        continue


if __name__ == "__main__":
    run()
