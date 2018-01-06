import libtcodpy as libtcod
import math
import textwrap
import shelve

# settings.py
def init():
	#actual size of the window
	global SCREEN_WIDTH
	global SCREEN_HEIGHT
	#size of the map
	global MAP_WIDTH
	global MAP_HEIGHT
	#size for rooms
	global ROOM_MAX_SIZE
	global ROOM_MIN_SIZE
	global MAX_ROOMS
	#FOV stuff
	global FOV_ALGO
	global FOV_LIGHT_WALLS
	global TORCH_RADIUS
	global INVENTORY_WIDTH
	global HEAL_AMOUNT
	#maximun fps
	global LIMIT_FPS
	#sizes and coordinates relevant for the GUI
	global BAR_WIDTH
	global PANEL_HEIGHT
	global PANEL_Y
	#sizes and coorinates relevent for the message system
	global MSG_X
	global MSG_WIDTH
	global MSG_HEIGHT
	#Spell Declarations
	global LIGHTNING_RANGE
	global LIGHTNING_DAMAGE
	global CONFUSE_NUM_TURNS
	global CONFUSE_RANGE
	global FIREBALL_DAMAGE
	global FIREBALL_RADIUS
	#experience and level-ups
	global LEVEL_UP_BASE
	global LEVEL_UP_FACTOR
	global LEVEL_SCREEN_WIDTH
	global CHARACTER_SCREEN_WIDTH
	#set colors of the wall and ground
	global color_dark_wall
	global color_light_wall
	global color_dark_ground
	global color_light_ground

	#actual size of the window
	SCREEN_WIDTH = 80
	SCREEN_HEIGHT = 50

	#size of the map
	MAP_WIDTH = 80
	MAP_HEIGHT = 43

	#size for rooms
	ROOM_MAX_SIZE = 9
	ROOM_MIN_SIZE = 5
	MAX_ROOMS = 20

	#FOV stuff
	FOV_ALGO = 0  #default FOV algorithm
	FOV_LIGHT_WALLS = True
	TORCH_RADIUS = 6

	INVENTORY_WIDTH = 50
	HEAL_AMOUNT = 4

	#maximun fps
	LIMIT_FPS = 60

	#sizes and coordinates relevant for the GUI
	BAR_WIDTH = 20
	PANEL_HEIGHT = 7
	PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT

	#sizes and coorinates relevent for the message system
	MSG_X = BAR_WIDTH + 2
	MSG_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
	MSG_HEIGHT = PANEL_HEIGHT - 1

	#Spell Declarations
	LIGHTNING_RANGE = 5
	LIGHTNING_DAMAGE = 20
	CONFUSE_NUM_TURNS = 10
	CONFUSE_RANGE = 8
	FIREBALL_DAMAGE = 12
	FIREBALL_RADIUS = 3

	#experience and level-ups
	LEVEL_UP_BASE = 200
	LEVEL_UP_FACTOR = 150
	LEVEL_SCREEN_WIDTH = 40
	CHARACTER_SCREEN_WIDTH = 30

	#set colors of the wall and ground
	color_dark_wall = libtcod.Color(0, 0, 100)
	color_light_wall = libtcod.Color(130, 110, 50)
	color_dark_ground = libtcod.Color(50, 50, 150)
	color_light_ground = libtcod.Color(200, 180, 50)