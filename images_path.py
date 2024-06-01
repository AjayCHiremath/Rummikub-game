# Constants
import pygame

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 750
RACK_SIZE = (850, 80)
BG_TEXT = ("RUMMIKUB GAME", (0, 0, 0), None)
LINE_COLOR = (193, 154, 107)
GRID_WIDTH = 52
GRID_HEIGHT = 73
GRID_COLOR_DARK = (0, 0, 255)
GRID_COLOR_LIGHT = (0, 0, 255)
BIG_BOX_WIDTH = 1198
BIG_BOX_HEIGHT = 510
BIG_BOX_POSITION = ((WINDOW_WIDTH - BIG_BOX_WIDTH - 100) // 2, 20)
CURRENT_POSITION = {}
BIG_BOX = pygame.Rect(BIG_BOX_POSITION[0], BIG_BOX_POSITION[1], BIG_BOX_WIDTH, BIG_BOX_HEIGHT)
ICON_PATH = "images/game_icon.jpg"
BG_IMAGE_PATH = "images/default_theme.png"
TABLE_IMAGE_PATH = "images/tile_rack_icon.png"
ADD_CARDS_PATH = "images/add_cards_icon.png"
REARRANGE_TILES_ICON_PATH = "images/rearrange_tiles_icon.png"
REARRANGE_COLORS_ICON = "images/rearrange_colors_icon.png"
MENU_ICON_PATH = "images/return_to_menu_icon.png"
FONT_PATH = "texts/super_bubble.ttf"
CHECK_LOGIC_BUTTON = "images/check_logic_button.png"
BLACK_TILES_PATH = {i: "images/tiles/1-15 BLACK/BLACK_1_{0}.png".format(i) for i in range(1, 16)}
BLUE_TILES_PATH = {i: "images/tiles/1-15 BLUE/BLUE_2_{0}.png".format(i) for i in range(1, 16)}
GREEN_TILES_PATH = {i: "images/tiles/1-15 GREEN/GREEN_3_{0}.png".format(i) for i in range(1, 16)}
RED_TILES_PATH = {i: "images/tiles/1-15 RED/RED_4_{0}.png".format(i) for i in range(1, 16)}
YELLOW_TILES_PATH = {i: "images/tiles/1-15 YELLOW/YELLOW_5_{0}.png".format(i) for i in range(1, 16)}
PERMUTATIONS = []
OCCUPIED_SPACE = {}
BOX_TILES = {}
IMG_PATHS = [ADD_CARDS_PATH, REARRANGE_TILES_ICON_PATH, MENU_ICON_PATH, CHECK_LOGIC_BUTTON]
TILES_IMAGES_PATHS = [BLACK_TILES_PATH, BLUE_TILES_PATH, GREEN_TILES_PATH, RED_TILES_PATH, YELLOW_TILES_PATH]

PLAYER_1 = {}
PLAYER_2 = {}
PLAYERS = [PLAYER_1, PLAYER_2]
