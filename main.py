import pygame
import sys

# Constants
TILE_SIZE = 30
PLAYFIELD_WIDTH = 10
PLAYFIELD_HEIGHT = 20
PLAYFIELD_RES = [PLAYFIELD_WIDTH * TILE_SIZE, PLAYFIELD_HEIGHT * TILE_SIZE]
FPS = 60
COLORS = {
    "white": (255, 255, 255),
    "red":  (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "gray": (128, 128, 128),
}
# PIECES represents the block coordinates for every piece and every possible piece rotation position
# PIECES[piece type][piece orientation][block coordinates][x or y]
PIECES = ((((1, 3), (2, 3), (3, 3), (4, 3)),  # I piece
           ((3, 1), (3, 2), (3, 3), (3, 4)),
           ((1, 3), (2, 3), (3, 3), (4, 3)),
           ((2, 1), (2, 2), (2, 3), (2, 4))),
          (((1, 2), (2, 2), (3, 2), (2, 3)),  # T piece
           ((2, 1), (2, 2), (2, 3), (1, 2)),
           ((2, 1), (1, 2), (2, 2), (3, 2)),
           ((2, 1), (2, 2), (3, 2), (2, 3))),
          (((1, 2), (2, 2), (3, 2), (1, 3)),  # L piece
           ((1, 1), (2, 1), (2, 2), (2, 3)),
           ((3, 1), (1, 2), (2, 2), (3, 2)),
           ((2, 1), (2, 2), (2, 3), (3, 3))),
          (((1, 2), (2, 2), (3, 2), (3, 3)),  # J piece
           ((2, 1), (2, 2), (1, 3), (2, 3)),
           ((1, 2), (1, 3), (2, 3), (3, 3)),
           ((2, 1), (3, 1), (2, 2), (2, 3))),
          (((2, 2), (3, 2), (1, 3), (2, 3)),  # S piece
           ((2, 1), (2, 2), (3, 2), (3, 3)),
           ((2, 2), (3, 2), (1, 3), (2, 3)),
           ((1, 1), (1, 2), (2, 2), (2, 3))),
          (((1, 2), (2, 2), (2, 3), (3, 3)),  # Z piece
           ((3, 1), (2, 2), (3, 2), (2, 3)),
           ((1, 2), (2, 2), (2, 3), (3, 3)),
           ((2, 1), (1, 2), (2, 2), (1, 3))),
          (((2, 2), (3, 2), (2, 3), (3, 3)),  # O piece
           ((2, 2), (3, 2), (2, 3), (3, 3)),
           ((2, 2), (3, 2), (2, 3), (3, 3)),
           ((2, 2), (3, 2), (2, 3), (3, 3))))


class Block:
    def __init__(self, color):
        self.color = color

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self.color,(x, y, TILE_SIZE, TILE_SIZE))


# class Piece:
#     def __init__(self, x, y, ):

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(PLAYFIELD_RES)
        self.clock = pygame.time.Clock()
        self.is_game_over = False

    def run(self):
        while not self.is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill("black")
            pygame.display.flip()


game = Game()
game.run()
