import pygame
import constants
import sys
from piece import Piece
from board import Board


# Game is responsible for instantiating and managing all other objects as well as dealing with user input
class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Arial', 18)
        self.display = pygame.display.set_mode(constants.DISPLAY_RES)
        self.playfield = pygame.Surface(constants.PLAYFIELD_RES)
        self.info_panel = pygame.Surface(constants.INFO_PANEL_RES)
        self.clock = pygame.time.Clock()
        self.is_game_over = False
        self.board = Board()
        self.piece = Piece()
        self.clock = pygame.time.Clock()
        self.time_since_last_drop = 0
        self.drop_time = 1500  # milliseconds
        self.lines = 0
        self.score = 0

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
            if self.piece.orientation == 3:
                new_orientation = 0
            else: 
                new_orientation = self.piece.orientation + 1

            block_num = 0
            for block in self.piece.blocks:
                x = self.piece.position[0] + constants.PIECES[self.piece.piece_type][new_orientation][block_num][0]
                y = self.piece.position[1] + constants.PIECES[self.piece.piece_type][new_orientation][block_num][1]
                # check if block would be outside of playfield
                if x >= constants.PLAYFIELD_WIDTH or x < 0 or y >= constants.PLAYFIELD_HEIGHT:
                    return False
                # check if tile is already taken on board
                if self.board.has_block(x, y):
                    return False
                block_num += 1
            return True

        if move == "counterclockwise":
            if self.piece.orientation == 0:
                new_orientation = 3
            else: 
                new_orientation = self.piece.orientation - 1

            block_num = 0
            for block in self.piece.blocks:
                x = self.piece.position[0] + constants.PIECES[self.piece.piece_type][new_orientation][block_num][0]
                y = self.piece.position[1] + constants.PIECES[self.piece.piece_type][new_orientation][block_num][1]
                if x >= constants.PLAYFIELD_WIDTH or x < 0 or y >= constants.PLAYFIELD_HEIGHT:
                    return False
                if self.board.has_block(x, y):
                    return False
                block_num += 1
            return True

    # adds current piece to board state and replaces current piece with the next one
    def get_new_piece(self):
        self.board.add_piece(self.piece)
        self.piece = Piece(self.piece.next_piece_type)
        self.check_for_lines()
        self.detect_game_over()
        self.time_since_last_drop = 0

    # detect lines and change score and game speed accordingly
    def check_for_lines(self):
        initial_level = self.get_level()
        lines = 0
        while self.board.detect_line() != -1 and lines < 4:
            self.board.clear_line(self.board.detect_line())
            self.lines += 1
            lines += 1
        if lines > 0:
            self.update_score(lines)
            if self.get_level() > initial_level:
                self.decrease_drop_time()

    def update_score(self, lines):
        points_to_add = 0
        if lines == 1:
            points_to_add = 40
        elif lines == 2:
            points_to_add = 100
        elif lines == 3:
            points_to_add = 300
        elif lines == 4:
            points_to_add = 1200

        # add 10% increase to points_to_add per player level
        points_to_add = int(points_to_add + ((self.get_level() * 0.1) * points_to_add))

        self.score += points_to_add

    def get_level(self):
        return self.lines // 10

    def decrease_drop_time(self):
        self.drop_time *= 0.8

    # takes in user input and moves piece accordingly
    def get_user_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if self.is_valid_move("down"):
                    self.piece.move_down()
                    self.time_since_last_drop = 0
                else:
                    self.get_new_piece()
            if event.key == pygame.K_LEFT and self.is_valid_move("left"):
                self.piece.move_left()
            if event.key == pygame.K_RIGHT and self.is_valid_move("right"):
                self.piece.move_right()
            if event.key == pygame.K_UP:
                while self.is_valid_move("down"):
                    self.piece.move_down()
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
                self.piece.move_down()
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

    # draws all surfaces and text on pygame window
    def draw_displays(self):
        self.playfield.fill("black")
        self.info_panel.fill("gray19")
        self.board.draw(self.playfield)
        self.piece.draw(self.playfield)
        next_piece_text_surface = self.my_font.render('Next:', False, constants.COLORS["white"])
        self.info_panel.blit(next_piece_text_surface, (50, 10))
        level_text = self.my_font.render(f'Level: {self.get_level()}', False, constants.COLORS["white"])
        self.info_panel.blit(level_text, (10, 450))
        lines_text = self.my_font.render(f'Score: {self.lines}', False, constants.COLORS["white"])
        self.info_panel.blit(lines_text, (10, 500))
        score_text = self.my_font.render(f'Score: {self.score}', False, constants.COLORS["white"])
        self.info_panel.blit(score_text, (10, 550))
        self.piece.draw_next_piece(self.info_panel)
        self.display.blit(self.playfield, (0, 0))
        self.display.blit(self.info_panel, (constants.PLAYFIELD_WIDTH * constants.BLOCK_SIZE, 0))
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
        print(f"Level: {self.get_level()}")
        print(f"Lines: {self.lines}")
        print(f"Score: {self.score}")
