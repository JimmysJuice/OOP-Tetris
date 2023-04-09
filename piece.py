import constants
import random
from block import Block


# Piece represents a piece that is being controlled by the user and not part of the tetris board yet
class Piece:
    def __init__(self, piece_type=-1):
        if piece_type == -1:
            self.piece_type = random.randrange(0, 7)  # picks random piece type
        else:
            self.piece_type = piece_type
        self.next_piece_type = random.randrange(0, 7)
        self.color = list(constants.COLORS.values())[self.piece_type]

        # determines piece starting position base on piece type
        if self.piece_type == 0:
            self.position = [2, -3]
        elif self.piece_type == 6:
            self.position = [2, -2]
        else:
            self.position = [3, -2]

        self.blocks = []
        self.orientation = 0

        for block_num in range(4):
            self.blocks.append(
                Block(self.position[0] + constants.PIECES[self.piece_type][self.orientation][block_num][0],
                      self.position[1] + constants.PIECES[self.piece_type][self.orientation][block_num][1],
                      self.color)
            )

    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface)

    # updates block positions based on current piece position
    def update(self):
        i = 0
        for block in self.blocks:
            block.x = self.position[0] + constants.PIECES[self.piece_type][self.orientation][i][0]
            block.y = self.position[1] + constants.PIECES[self.piece_type][self.orientation][i][1]
            i += 1

    # drops piece by 1 block and updates blocks[] y values
    def drop(self):
        self.position[1] += 1
        self.update()

    # moves piece to the left by 1 block and updates blocks[] x values
    def shift_left(self):
        self.position[0] -= 1
        self.update()

    # moves piece to the right by 1 block and updates blocks[] x values
    def shift_right(self):
        self.position[0] += 1
        self.update()

    # rotates piece clockwise and updates blocks[] x and y values
    def rotate_clockwise(self):
        if self.orientation == 3:
            self.orientation = 0
        else:
            self.orientation += 1
        self.update()

    # rotates piece counterclockwise and updates blocks[] x and y values
    def rotate_counterclockwise(self):
        if self.orientation == 0:
            self.orientation = 3
        else:
            self.orientation -= 1
        self.update()
