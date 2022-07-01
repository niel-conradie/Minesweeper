from board import Board


class Minesweeper:
    """A class to represent a minesweeper game."""

    def __init__(self):
        """Initialize class attributes."""
        self.round = 1
        self.round_won = 0
        self.round_lost = 0

    @staticmethod
    def user_input():
        """Requesting user input and validating choice."""
        while True:
            try:
                user_input = int(input("Enter: "))
            except ValueError:
                print("\nThat is not a number.\n")
                continue

            choices = [1, 2, 3]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!\n")
                continue
            else:
                return user_input

    @staticmethod
    def user_input_allocation(user_input):
        """Assign user input to appropriate difficulty."""
        if user_input == 1:
            return 10, 10
        if user_input == 2:
            return 16, 40
        if user_input == 3:
            return 30, 99

    @staticmethod
    def display_difficulty():
        """Display difficulty options."""
        print("\nSelect your difficulty.")
        print("\nBeginner: Type '1'")
        print("Intermediate: Type '2'")
        print("Expert: Type '3'")

    @staticmethod
    def user_input_row():
        """Requesting user input and validating number."""
        while True:
            try:
                user_input = int(input("\nSelect row: "))
                if user_input < 0:
                    print("\nThat is a negative number.")
                else:
                    return user_input
            except ValueError:
                print("\nThat is not a number.")
                continue

    @staticmethod
    def user_input_column():
        """Requesting user input and validating number."""
        while True:
            try:
                user_input = int(input("\nSelect column: "))
                if user_input < 0:
                    print("\nThat is a negative number.")
                else:
                    return user_input
            except ValueError:
                print("\nThat is not a number.")
                continue

    def add_round(self):
        """Add point to round played."""
        self.round += 1

    def add_round_won(self):
        """Add point to round won."""
        self.round_won += 1

    def add_round_lost(self):
        """Add point to round lost."""
        self.round_lost += 1

    def display_scoreboard(self):
        """Display the round played/won/lost."""
        print(
            f"\nROUND: {self.round} | WON: {self.round_won} | LOST: {self.round_lost}"
        )

    def start_game(self, dimension_size, number_bombs):
        """Start Minesweeper game."""
        # Creating the board.
        board = Board(dimension_size, number_bombs)
        safe = True

        while len(board.dug) < board.dimension_size**2 - number_bombs:
            print()
            print(board)

            print("\nWhere would you like to dig?")

            # Requesting user input and validating number.
            row = self.user_input_row()
            column = self.user_input_column()
            if (
                row < 0
                or row >= board.dimension_size
                or column < 0
                or column >= dimension_size
            ):
                print("\nInvalid location. Please try again.")
                continue

            # Verifying a valid dig.
            safe = board.dig(row, column)
            if not safe:
                break

        # Win conditions.
        if safe:
            print()
            board.dug = [
                (r, c)
                for r in range(board.dimension_size)
                for c in range(board.dimension_size)
            ]
            print(board)
            print("\nWINNER!")
            self.add_round_won()
        else:
            print()
            board.dug = [
                (r, c)
                for r in range(board.dimension_size)
                for c in range(board.dimension_size)
            ]
            print(board)
            print("\nGAME OVER!")
            self.add_round_lost()

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nRestart? Yes/No: ").lower()
            choices = ["yes", "no"]
            if user_input not in choices:
                print("\nPlease type 'yes' or 'no'")
                continue

            # User input conditions.
            if user_input == "yes":
                return
            if user_input == "no":
                print("\nThank you for playing!")
                quit()
