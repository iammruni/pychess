
class Board:
    def __init__(self):
        # Initialize an 8x8 board with pieces in starting positions
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def display(self):
        # Print column labels (A-H)
        #print("  A | B | C | D | E | F | G | H")
        print("  _A_|_B_|_C_|_D_|_E_|_F_|_G_|_H_")

        # Print each row with the corresponding row number (1-8)
        for index, row in enumerate(self.board, start=1):
            print(f"{index}| " + "   ".join(row))


    def validate_move(self, start, end):
        """Validates the moves and return 1,
        if the moves are valid and 0 otherwise."""
        
        start_row, start_col = start
        end_row, end_col = end
        # Basic out of bounds validation
        if not (0 <= start_row < 8 and 0 <= start_col < 8):
            print("Invalid starting position!")
            return 0
        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            print("Invalid ending position!")
            return 0

        return 1

    def move_piece(self, start, end):
        # Validate move??
        if self.validate_move(start, end):
            start_row, start_col = start
            end_row, end_col = end

            piece = self.board[start_row][start_col]
            self.board[start_row][start_col] = '.'
            self.board[end_row][end_col] = piece

            print(f"Moved {piece} from {start} to {end}")
            return 1
        return 0

