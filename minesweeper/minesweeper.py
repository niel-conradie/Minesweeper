from board import Board


class Minesweeper:
    """ A class to represent a minesweeper game. """

    @staticmethod
    def user_input_row():
        """ Requesting user input and validating number. """
        while True:
            try:
                user_input = int(input("\nSelect row: "))
                return user_input
            except ValueError:
                print(f"\nThat is not a number.")
                continue

    @staticmethod
    def user_input_column():
        """ Requesting user input and validating number. """
        while True:
            try:
                user_input = int(input("\nSelect column: "))
                return user_input
            except ValueError:
                print(f"\nThat is not a number.")
                continue

    def start_game(self, dimension_size=10, number_bombs=10):
        """ Start Minesweeper game. """
        # Creating the board.
        board = Board(dimension_size, number_bombs)
        safe = True

        while len(board.dug) < board.dimension_size ** 2 - number_bombs:
            print()
            print(board)

            print("\nWhere would you like to dig?")

            # Requesting user input and validating number.
            row = self.user_input_row()
            column = self.user_input_column()
            if row < 0 or row >= board.dimension_size or column < 0 or column >= dimension_size:
                print("\nInvalid location. Please try again.")
                continue

            # Verifying a valid dig.
            safe = board.dig(row, column)
            if not safe:
                break

        # Win conditions.
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
