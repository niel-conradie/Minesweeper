from board import Board


def play(dimension_size=10, number_bombs=10):
    """ Minesweeper. """
    # Creating the board.
    board = Board(dimension_size, number_bombs)
    safe = True

    while len(board.dug) < board.dimension_size ** 2 - number_bombs:
        print()
        print(board)

        # Requesting user input and validating input.
        user_input = input(
            "\nWhere would you like to dig? Input as row, column: ")
        user_input = user_input.split(' ')
        row, column = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dimension_size or column < 0 or column >= dimension_size:
            print("\nInvalid location. Please try again.")
            continue

        # Verifying a valid dig.
        safe = board.dig(row, column)
        if not safe:
            break

    # Game Won/Lost conditions.
    if safe:
        print()
        board.dug = [(r, c) for r in range(board.dimension_size)
                     for c in range(board.dimension_size)]
        print(board)
        print("\nWINNER!")
    else:
        print()
        board.dug = [(r, c) for r in range(board.dimension_size)
                     for c in range(board.dimension_size)]
        print(board)
        print("\nGAME OVER!")


if __name__ == '__main__':
    play()
