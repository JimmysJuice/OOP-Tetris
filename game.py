import pygame
import constants
import sys
from piece import Piece


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
                    self.state[x][y-1].drop()
                self.state[x][y] = self.state[x][y-1]
                self.state[x][y-1] = 0


# Game is responsible for instantiating and managing all other objects as well as dealing with user input
class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(constants.DISPLAY_RES)
        self.playfield = pygame.Surface(constants.PLAYFIELD_RES)
        self.clock = pygame.time.Clock()
        self.is_game_over = False
        self.board = Board()
        self.piece = Piece()
        self.clock = pygame.time.Clock()
        self.time_since_last_drop = 0
        self.drop_time = 2000  # milliseconds

    # check if move is valid and returns true or false accordingly
    def is_valid_move(self, move):
        if move == "down":
            for block in self.piece.blocks:
                if block.y + 1 >= constants.PLAYFIELD_HEIGHT or self.board.has_block(block.x, block.y + 1):
                    return False
            else:
                return True
        if move == "left":
            for block in self.piece.blocks:
                if block.x - 1 < 0 or self.board.has_block(block.x - 1, block.y):
                    return False
            else:
                return True
        if move == "right":
            for block in self.piece.blocks:
                if block.x + 1 >= constants.PLAYFIELD_WIDTH or self.board.has_block(block.x + 1, block.y):
                    return False
            else:
                return True
        if move == "clockwise":
            self.piece.rotate_clockwise()
            for block in self.piece.blocks:
                if block.x >= constants.PLAYFIELD_WIDTH or block.x < 0 or block.y >= constants.PLAYFIELD_HEIGHT or \
                        self.board.has_block(block.x, block.y):
                    self.piece.rotate_counterclockwise()
                    return False
            self.piece.rotate_counterclockwise()
            return True

        if move == "counterclockwise":
            self.piece.rotate_counterclockwise()
            for block in self.piece.blocks:
                if block.x >= constants.PLAYFIELD_WIDTH or block.x < 0 or block.y >= constants.PLAYFIELD_HEIGHT or \
                        self.board.has_block(block.x, block.y):
                    self.piece.rotate_clockwise()
                    return False
            self.piece.rotate_clockwise()
            return True

    # adds current piece to board state and replaces current piece with a new one
    def get_new_piece(self):
        self.board.add_piece(self.piece)
        lines = 0
        while self.board.detect_line() != -1 and lines < 4:
            self.board.clear_line(self.board.detect_line())
            lines += 1
        self.piece = Piece()
        self.detect_game_over()
        self.time_since_last_drop = 0

    # takes in user input and moves piece accordingly
    def get_user_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if self.is_valid_move("down"):
                    self.piece.drop()
                    self.time_since_last_drop = 0
                else:
                    self.get_new_piece()
            if event.key == pygame.K_LEFT and self.is_valid_move("left"):
                self.piece.shift_left()
            if event.key == pygame.K_RIGHT and self.is_valid_move("right"):
                self.piece.shift_right()
            if event.key == pygame.K_UP:
                while self.is_valid_move("down"):
                    self.piece.drop()
                self.get_new_piece()
            if event.key == pygame.K_z and self.is_valid_move("counterclockwise"):
                self.piece.rotate_counterclockwise()
            if event.key == pygame.K_x and self.is_valid_move("clockwise"):
                self.piece.rotate_clockwise()

    # tracks milliseconds since last piece drop and drops again when time reaches drop_time
    def drop_timer(self):
        dt = self.clock.tick()
        self.time_since_last_drop += dt
        if self.time_since_last_drop >= self.drop_time:
            if self.is_valid_move("down"):
                self.piece.drop()
            else:
                self.get_new_piece()
            self.time_since_last_drop = 0

    # returns true if game over is detected or false if not
    def detect_game_over(self):
        for block in self.piece.blocks:
            if self.board.has_block(block.x, block.y):
                self.is_game_over = True
            else:
                self.is_game_over = False

    def draw_displays(self):
        self.display.fill("grey")
        self.playfield.fill("black")
        self.board.draw(self.playfield)
        self.piece.draw(self.playfield)
        self.display.blit(self.playfield, ((constants.DISPLAY_WIDTH / 2 - constants.PLAYFIELD_WIDTH / 2) *
                                           constants.TILE_SIZE, 0))
        pygame.display.flip()

    # starts game loop
    def run(self):
        while not self.is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.get_user_input(event)
            self.drop_timer()
            self.draw_displays()
        print("Game Over!")
