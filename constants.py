TILE_SIZE = 30
DISPLAY_WIDTH = 20
DISPLAY_HEIGHT = 20
DISPLAY_RES = [DISPLAY_WIDTH * TILE_SIZE, DISPLAY_HEIGHT * TILE_SIZE]
PLAYFIELD_WIDTH = 10
PLAYFIELD_HEIGHT = 20
PLAYFIELD_RES = [PLAYFIELD_WIDTH * TILE_SIZE, PLAYFIELD_HEIGHT * TILE_SIZE]
PREVIEW_WINDOW_WIDTH = 5
PREVIEW_WINDOW_HEIGHT = 5
PREVIEW_WINDOW_RES = [PREVIEW_WINDOW_WIDTH * TILE_SIZE, PREVIEW_WINDOW_HEIGHT * TILE_SIZE]
FPS = 60
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
# PIECES[piece type][piece orientation][block number][block co-ords (x or y)]
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