import pygame
import constants


# Block represents the individual block that is drawn on the tetris board
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x * constants.TILE_SIZE, self.y * constants.TILE_SIZE,
                                               constants.TILE_SIZE, constants.TILE_SIZE))
        pygame.draw.rect(surface, constants.COLORS["black"], (self.x * constants.TILE_SIZE,
                                                              self.y * constants.TILE_SIZE, constants.TILE_SIZE,
                                                              constants.TILE_SIZE), 1)
