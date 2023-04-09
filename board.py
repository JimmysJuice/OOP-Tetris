import constants


# Board keeps track of the blocks on the tetris board and draws them
class Board:
    def __init__(self):
        self.state = []
        # populate empy board state
        for column in range(constants.PLAYFIELD_WIDTH):
            self.state.append([])
            for row in range(constants.PLAYFIELD_HEIGHT):
                self.state[column].append(0)  # 0 represents and empty tile on the board

    # draw all blocks in board state
    def draw(self, surface):
        for column in self.state:
            for row in column:
                if row != 0:
                    row.draw(surface)

    # has_block(x, y) checks if Block.state[x][y] has a block
    def has_block(self, x, y):
        if 0 <= x < constants.PLAYFIELD_WIDTH and 0 <= y < constants.PLAYFIELD_HEIGHT:
            if self.state[x][y] != 0:
                return True
            else:
                return False
        else:
            return False

    # add piece to board state
    def add_piece(self, piece):
        for block in piece.blocks:
            self.state[block.x][block.y] = block

    # detects if board state has a line to clear and returns the row number or -1 if no row is detected
    def detect_line(self):
        for row in range(0, constants.PLAYFIELD_HEIGHT):
            count = 0
            for column in range(constants.PLAYFIELD_WIDTH):
                if self.state[column][row] != 0:
                    count += 1
            if count == constants.PLAYFIELD_WIDTH:
                return row
        return -1

    def clear_line(self, row):
        for y in range(row, 0, -1):
            for x in range(0, constants.PLAYFIELD_WIDTH):
                if self.state[x][y-1] != 0:
                    self.state[x][y-1].y += 1
                self.state[x][y] = self.state[x][y-1]
                self.state[x][y-1] = 0
