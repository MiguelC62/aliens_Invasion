from game.casting.color import Color
import os

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Alien Invasion"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "alien_invasion/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "alien_invasion/assets/sounds/boing.wav"
WELCOME_SOUND = "alien_invasion/assets/sounds/start.wav"
OVER_SOUND = "alien_invasion/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
dir = os.getcwd()  # Get the current working directory (cwd)
cwd =dir.replace('\\','/')
#LEVEL_FILE = "d:/Documentos/BYU-Pathway/CSE210/batter-complete/batter/assets/data/level-{:03}.txt"
LEVEL_FILE = cwd + "/alien_invasion/assets/data/level-{:03}.txt" 
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# TANK
TANK_GROUP = "tanks"
TANK_IMAGES = [f"alien_invasion/assets/images/{n:03}.png" for n in range(100, 103)]
TANK_WIDTH = 106
TANK_HEIGHT = 62
TANK_RATE = 6
TANK_VELOCITY = 7

# BUNKER
BUNKER_GROUP = "bunkers"
BUNKER_IMAGES = [f"alien_invasion/assets/images/{n:03}.png" for n in range(105, 108)]
BUNKER_WIDTH = 106
BUNKER_RATE = 6
BUNKER_HEIGHT = 62

# PROJECTILS
PROJECTILS_GROUP = "projectils"
PROJECTILS_IMAGE = "alien_invasion/assets/images/000.png"
PROJECTILS_WIDTH = 28
PROJECTILS_HEIGHT = 28
PROJECTILS_RATE = 6
PROJECTILS_VELOCITY = 20
PROJECTILS_NUMBER = 4

# BOMBS
BOMBS_GROUP = "bombs"
BOMBS_IMAGE = "alien_invasion/assets/images/bomb.png"
BOMBS_WIDTH = 28
BOMBS_HEIGHT = 28
BOMBS_RATE = 6
BOMBS_VELOCITY = 10
BOMBS_NUMBER = 3

# ALIENS
ALIENS_GROUP = "aliens"
ALIENS_IMAGES = {
    "b": [f"alien_invasion/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"alien_invasion/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"alien_invasion/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"alien_invasion/assets/images/{i:03}.png" for i in range(40,49)]
}
ALIENS_WIDTH = 90
ALIENS_HEIGHT = 60
ALIENS_DELAY = 0
ALIENS_RATE = 25
ALIENS_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"