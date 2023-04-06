import pygame
import sys
import constants
import random


# Block represents the individual block that is drawn on the tetris board
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x * constants.TILE_SIZE, self.y * constants.TILE_SIZE,
                                               constants.TILE_SIZE, constants.TILE_SIZE))

    def drop(self):
        self.y += 1

    def shift_left(self):
        self.x -= 1

    def shift_right(self):
        self.x += 1


# Piece represents a piece that is being controlled by the user and not part of the tetris board yet
class Piece:
    def __init__(self):
        self.color = random.choice(list(constants.COLORS.values()))
        self.piece_type = random.randrange(0, 7)  # picks random piece type

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
        for block in self.blocks:
            block.x = self.position[0] + constants.PIECES[self.piece_type][self.orientation][block][0]
            block.y = self.position[1] + constants.PIECES[self.piece_type][self.orientation][block][1]

    def drop(self):
        for block in self.blocks:
            block.drop()

    def shift_left(self):
        for block in self.blocks:
            block.shift_left()

    def shift_right(self):
        for block in self.blocks:
            block.shift_right()

    def rotate_clockwise(self):
        if self.orientation == 3:
            self.orientation = 0
        else:
            self.orientation += 1

    def rotate_counterclockwise(self):
        if self.orientation == 0:
            self.orientation = 3
        else:
            self.orientation -= 1


# board keeps track of the blocks on the tetris board and draws them
class Board:
    def __init__(self):
        self.state = []
        # populate empy board state
        for column in range(constants.PLAYFIELD_WIDTH):
            self.state.append([])
            for row in range(constants.PLAYFIELD_HEIGHT):
                self.state[column].append(" ")  # " " represents and empty tile on the board
        print("test")

    # loop through state and draw block when not " "
    def draw(self):
        pass


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(constants.PLAYFIELD_RES)
        self.clock = pygame.time.Clock()
        self.is_game_over = False
        self.piece = Piece()

    def run(self):
        while not self.is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill("black")
            self.piece.draw(self.screen)
            pygame.display.flip()
