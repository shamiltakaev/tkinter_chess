class Board:
    def __init__(self):
        self.board = []

        for _ in range(8):
            self.board.append([None] * 8)

    def print_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(f"{str(self.board[row][col]):^4}", end="|")
            print()

    def move_piece(self, piece, target_row, target_col):
        piece = self.board[piece.row][piece.col]
        self.print_board()
        if piece.can_move(self.board, target_row, target_col) is False:
            return False

        self.board[piece.row][piece.col] = None
        self.board[target_row][target_col] = piece
        piece.set_position(target_row, target_col)
        return True