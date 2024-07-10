# given_game_board = 'O   X   O' #example board
given_game_board = '         ' #input board to be analyze X's next move

MOVE_MAPPING = {
    0: 'Top Left', 1: 'Top Center', 2: 'Top Right',
    3: 'Middle Left', 4: 'Middle Center', 5: 'Middle Right',
    6: 'Bottom Left', 7: 'Bottom Center', 8: 'Bottom Right',
    -1: 'N/A. No available moves'
}

MINIMAX_VALUE_MAPPING = {
    1: 'X winning',
    0: 'a draw',
    -1: 'O winning'
}

class TicTacToe:
    minimax_counter = 0
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

    def minimax(self, depth: int, maximizing_player: bool, alpha: float = float('-inf'), beta: float = float('inf')) -> int:
        """
        Implement the minimax algorithm with alpha-beta pruning to find the optimal move.
        'X' is the maximizing player.

        Parameters:
        - depth: Current depth in the game tree (recursive calls).
        - maximizing_player: True if the current player is trying to maximize the score ('X'), False otherwise ('O').
        - alpha: The current best score that the maximizing player is assured of.
        - beta: The current best score that the minimizing player is assured of.

        Returns:
        - The minimax value for the current state of the board.
        """
        TicTacToe.minimax_counter += 1

        # Base cases
        if self.check_winner('X'):
            return 1
        elif self.check_winner('O'):
            return -1
        elif self.check_draw():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    eval = self.minimax(depth + 1, False, alpha, beta)
                    self.board[i] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Alpha-beta pruning
                    if max_eval == 1:
                        break # best possible evaluation
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    eval = self.minimax(depth + 1, True, alpha, beta)
                    self.board[i] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha-beta pruning
                    if min_eval == -1:
                        break # best possible evaluation
            return min_eval

    def find_best_move(self) -> int:
        """
        Find the best move for the 'X' player using the minimax algorithm.
        In case of multiple equally optimal moves, the tiebreaker is the lower index.

        Returns:
        - The index of the best move on the board. (-1 if no possible moves)
        - The minimax value of the best move given.
        """
        TicTacToe.minimax_counter = 0
        best_val = float('-inf')
        best_move = -1

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                move_val = self.minimax(0, False)
                self.board[i] = ' '

                if move_val > best_val:
                    best_val = move_val
                    best_move = i
        if best_move == -1:
            if self.check_winner('X'):
                return best_move, 1
            elif self.check_winner('O'):
                return best_move, -1
            elif self.check_draw():
                return best_move, 0

        return best_move, best_val

if __name__ == "__main__":
    game = TicTacToe(given_game_board)
    game.display_board()
    best_move, best_val = game.find_best_move()

    print(f"A best move for 'X' is: {MOVE_MAPPING[best_move]}.")
    print(f"With optimal play, this position leads to {MINIMAX_VALUE_MAPPING[best_val]}")
    print(f"Positions analyzed: {TicTacToe.minimax_counter}")