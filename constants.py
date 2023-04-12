BLOCK_SIZE = 30  # pixels per block
DISPLAY_WIDTH = 15  # blocks
DISPLAY_HEIGHT = 20
DISPLAY_RES = (DISPLAY_WIDTH * BLOCK_SIZE, DISPLAY_HEIGHT * BLOCK_SIZE)
PLAYFIELD_WIDTH = 10
PLAYFIELD_HEIGHT = 20
PLAYFIELD_RES = (PLAYFIELD_WIDTH * BLOCK_SIZE, PLAYFIELD_HEIGHT * BLOCK_SIZE)
PREVIEW_WINDOW_WIDTH = 5
PREVIEW_WINDOW_HEIGHT = 5
PREVIEW_WINDOW_RES = (PREVIEW_WINDOW_WIDTH * BLOCK_SIZE, PREVIEW_WINDOW_HEIGHT * BLOCK_SIZE)
COLORS = {
    "red":  (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "gray": (128, 128, 128),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}
# PIECES represents the block coordinates for every piece and every possible piece rotation position
# PIECES[piece type][orientation][block number][block co-ords (x, y)]
PIECES = ((((1, 3), (2, 3), (3, 3), (4, 3)),  # I piece orientation 0 
           ((3, 1), (3, 2), (3, 3), (3, 4)),  #         orientation 1
           ((1, 3), (2, 3), (3, 3), (4, 3)),  #         orientation 2
           ((2, 1), (2, 2), (2, 3), (2, 4))), #         orientation 3
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
           ((1, 1), (1, 2), (2, 2), (3, 2)),
           ((2, 1), (3, 1), (2, 2), (2, 3))),
          (((2, 2), (3, 2), (1, 3), (2, 3)),  # S piece
           ((2, 1), (2, 2), (3, 2), (3, 3)),
           ((2, 2), (3, 2), (1, 3), (2, 3)),
           ((2, 1), (2, 2), (3, 2), (3, 3))),
          (((1, 2), (2, 2), (2, 3), (3, 3)),  # Z piece
           ((3, 1), (2, 2), (3, 2), (2, 3)),
           ((1, 2), (2, 2), (2, 3), (3, 3)),
           ((3, 1), (2, 2), (3, 2), (2, 3))),
          (((2, 2), (3, 2), (2, 3), (3, 3)),  # O piece
           ((2, 2), (3, 2), (2, 3), (3, 3)),
           ((2, 2), (3, 2), (2, 3), (3, 3)),
           ((2, 2), (3, 2), (2, 3), (3, 3))))