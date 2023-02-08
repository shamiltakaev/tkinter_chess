class Bishop:
    def __init__(self, color):
        self.row = 0
        self.col = 0
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def can_move(self, row, col):
        if (self.row, self.col) == (row, col):
            return False
        if 0 <= row < 8 and 0 <= col < 8:
            return abs(self.row - row) == abs(self.col - col)
        return False

    def __str__(self) -> str:
        return "B"