class Figure:
    def __init__(self, color):
        self.row = 0
        self.col = 0
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col


class Bishop(Figure):
    def can_move(self, board, target_row, target_col):
        if abs(self.row - target_row) == abs(self.col - target_col):
            step_r = 1 if target_row > self.row else -1
            step_c = 1 if target_col > self.col else -1
            for r in range(self.row + step_r, target_row + step_r, step_r):
                c = self.col + abs(r - self.row) if step_c == 1 else self.col - abs(r - self.row)
                if board[r][c] is not None:
                    return False
            return True
        return False
    def __str__(self) -> str:
        return "B"


class Rook(Figure):
    def can_move(self, board, target_row, target_col):
        if target_row == self.row or self.col == target_col:
            step = 1 if target_row > self.row else -1
            for r in range(self.row + step, target_row + step, step):
                if board[r][self.col] is not None:
                    return False
            step = 1 if target_col > self.col else -1
            for c in range(self.col + step, target_col + step, step):
                if board[self.row][c] is not None:
                    return False
            return True
        return False

    def __str__(self):
        return "R"


class Knight(Figure):
    def can_move(self, board, target_row, target_col):
        dx = abs(self.row - target_row)
        dy = abs(self.col - target_col)
        if (dx, dy) in ((1, 2), (2, 1)):
            if board[target_row][target_col] is None:
                return True
        return False

    def __str__(self) -> str:
        return "N"


class Queen(Figure):
    def can_move(self, board, target_row, target_col):
        if (abs(self.row - target_row) == abs(self.col - target_col) or
            self.row == target_row or self.col == target_col):
            if self.row == target_row or self.col == target_col:
                step = 1 if target_row > self.row else -1

                for r in range(self.row + step, target_row + step, step):
                    if board[r][self.col] is not None:
                        return False
                
                step = 1 if target_col > self.col else -1

                for c in range(self.col + step, target_col + step, step):
                    if board[self.row][c] is not None:
                        return False
            else:
                step_r = 1 if target_row > self.row else -1
                step_c = 1 if target_col > self.col else -1
                for r in range(self.row + step_r, target_row + step_r, step_r):
                    c = self.col + abs(r - self.row) if step_c == 1 else self.col - abs(r - self.row)
                    if board[r][c] is not None:
                        return False
        
        return True

    def __str__(self) -> str:
        return "Q"


class King(Figure):
    def can_move(self, board,  target_row, target_col):
        dx = abs(self.row - target_row)
        dy = abs(self.col - target_col)
        if (dx, dy) in [(0, 1), (1, 0), (1, 1)]:
            if board[target_row][target_col] is None:
                return True
        return False

    def __str__(self):
        return "K"


class Pawn(Figure):
    def can_move(self, board, target_row, target_col):
        if self.color == "white":
            if self.row - target_row == 1 and self.col == target_col:
                if board[target_row][target_col] is not None:
                    return False
                return True
            return False

    def __str__(self):
        return "P"
