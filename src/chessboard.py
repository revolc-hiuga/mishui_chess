import const

class Piece:
    color = const.NONE_COLOR
    ptype = const.NONE

    def __init__(self, color_:int, ptype_:int):
        self.color = color_
        self.ptype = ptype_

class Coord:
    x = 0
    y = 0

    def __init__(self, x_:int, y_:int):
        self.x = x_
        self.y = y_

    def is_in_range(self) -> bool:
        if self.x < 0 or self.x >= const.X_SIZE:
            return False

        if self.y < 0 or self.y >= const.Y_SIZE:
            return False

        return True

class Chessboard:
    pieces:list[list[Piece]] = [[]]
    side_to_move = const.BLUE

    def __init__(self):
        self.pieces = [[]]
        for _ in range(0, const.Y_SIZE):
            piece_list:list[Piece] = []
            for _ in range(0, const.X_SIZE):
                piece_list.append(Piece(const.NONE, const.NONE_COLOR))
            self.pieces.append(piece_list)