class TicTacToe:
    def __init__(self, board_str: str = None) -> None:
        """
        Initialize a Tic-Tac-Toe game.

        Parameters:
        - board_str: Optional string representing the initial state of the board.
                          Must be a string of 9 characters (X, O, or space).

        Raises:
        - ValueError: If the provided board_str is invalid.
        """
        valid_values = {'X', 'O', ' '}

        if board_str is None:
            self.board = [' '] * 9
        else:
            if len(board_str) == 9 and all(cell in valid_values for cell in board_str):
                self.board = list(board_str)
            else:
                raise ValueError("Invalid board format. Must be a string of 9 characters (X, O, or space).")

    def display_board(self) -> None:
        """
        Display the current state of the Tic-Tac-Toe board.
        """
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def check_winner(self, player: str) -> bool:
        """
        Checks if the specified player wins on the board.

        Parameters:
        - player: must be 'X' or 'O'

        Returns:
        True if the specified player wins, False otherwise.
        """
        for i in range(3):
            if all(self.board[i*3 + j] == player for j in range(3)) or \
            all(self.board[i + j*3] == player for j in range(3)):
                return True
        if all(self.board[i] == player for i in [0, 4, 8]) or \
        all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def check_draw(self) -> bool:
        """
        Checks if the game is a draw.

        Pre-Condition:
        This method assumes that a win has already been checked.

        Returns:
        True if the board is full (thus a draw by pre-condition), False otherwise.
        """
        return ' ' not in self.board

game = TicTacToe('XOXOOXOX ')

game.display_board()
