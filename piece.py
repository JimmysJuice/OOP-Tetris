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

        # determines piece starting position based on piece type
        if self.piece_type == 0:
            self.position = [2, -3]
        elif self.piece_type == 6:
            self.position = [2, -2]
        else:
            self.position = [3, -2]

        self.blocks = []
        self.next_piece_blocks = []
        self.orientation = 0

        for block_num in range(4):
            self.blocks.append(
                Block(self.position[0] + constants.PIECES[self.piece_type][self.orientation][block_num][0],
                      self.position[1] + constants.PIECES[self.piece_type][self.orientation][block_num][1],
                      self.color)
            )
            if self.next_piece_type == 0 or self.next_piece_type == 6:
                self.next_piece_blocks.append(
                    Block(constants.PIECES[self.next_piece_type][0][block_num][0] - 0.5,
                          constants.PIECES[self.next_piece_type][0][block_num][1],
                          list(constants.COLORS.values())[self.next_piece_type])
                )
            else:
                self.next_piece_blocks.append(
                    Block(constants.PIECES[self.next_piece_type][0][block_num][0],
                          constants.PIECES[self.next_piece_type][0][block_num][1],
                          list(constants.COLORS.values())[self.next_piece_type])
                )

    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface)

    def draw_next_piece(self, surface):
        for block in self.next_piece_blocks:
            block.draw(surface)

    # updates block positions based on current piece position
    def update(self):
        i = 0
        for block in self.blocks:
            block.x = self.position[0] + constants.PIECES[self.piece_type][self.orientation][i][0]
            block.y = self.position[1] + constants.PIECES[self.piece_type][self.orientation][i][1]
            i += 1

    def move_down(self):
        self.position[1] += 1
        self.update()

    def move_left(self):
        self.position[0] -= 1
        self.update()

    def move_right(self):
        self.position[0] += 1
        self.update()

    def rotate_clockwise(self):
        if self.orientation == 3:
            self.orientation = 0
        else:
            self.orientation += 1
        self.update()

    def rotate_counterclockwise(self):
        if self.orientation == 0:
            self.orientation = 3
        else:
            self.orientation -= 1
        self.update()
