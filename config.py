from pygame import Color


SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (900, 680)
FPS = 60

MENU_BG_COLOR = Color('#333377')
MENU_BTN_SIZE = (MENU_BTN_WIDTH, MENU_BTN_HEIGHT) = (300, 100)
MENU_BTN_FONT_SIZE = 40

GAME_BG_COLOR = Color('#000000')

BTN_TXT_USUAL_COLOR = Color('#FFFFFF')
BTN_TXT_SELECTED_COLOR = Color('#FF8888')
BTN_TXT_INACTIVE_COLOR = Color('#AAAAAA')
BTN_BG_COLOR = Color('#555577')

LBL_TXT_DEFAULT_COLOR = Color('#FFFFFF')

WALL_SIZE = (WALL_WIDTH, WALL_HEIGHT) = (50, 50)
WALL_COLOR = Color('#703508')

PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT) = (64, 64)
PLAYER_SPEED = 7
PLAYER_COLOR = Color('#AAAAAA')
PLAYER_HP_MAX = 1000

ENEMY_SIZE = (ENEMY_WIDTH, ENEMY_HEIGHT) = (64, 64)
ENEMY_SPEED = 7
ENEMY_COLOR = Color('#17ff64')
ENEMY_BORDER = 20
ENEMY_FRAME_SIZE = (ENEMY_WIDTH + ENEMY_BORDER * 2, ENEMY_HEIGHT + ENEMY_BORDER * 2)
ENEMY_SHOOT_TIMEOUT = 20
ENEMY_VEER_TIMEOUT = (100, 300)

PLASMA_SIZE = (PLASMA_WIDTH, PLASMA_HEIGHT) = (16, 16)
PLASMA_SPEED = 15
PLASMA_COLOR = Color('#00ff3b')
PLASMA_DAMAGE = (15, 25)

BOMB_SIZE = (BOMB_WIDTH, BOMB_HEIGHT) = (22, 30)
BOMB_COLOR = Color('#22DD11')
BOMB_TIMEOUT = 120
