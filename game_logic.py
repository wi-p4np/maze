from colorama import Fore
from utils import clear
from game_input import get_key
import copy

NOTHING = "0"
WALL = "1"
PLAYER = "2"
SCORE_1 = "3"
SCORE_5 = "4"
START = "S"
END = "E"
POINTS_TRAP = "T"
WALL_3 = "C"
WALL_2 = "B"
WALL_1 = "A"
KEY = "K"
DOOR = "D"
PRESSURE_PLATE = "P"
CRATE = "Q"
LIFE = "L"
ARROW_RIGHT = "R"
ARROW_LEFT = "L"


colors_mapping = {
    WALL: Fore.YELLOW,
    SCORE_1: Fore.GREEN,
    SCORE_5: Fore.CYAN,
    LIFE: Fore.MAGENTA,
    END: Fore.RED
}

character_mapping = {
    NOTHING: " ",
    WALL: "▇",
    PLAYER: "O",
    SCORE_1: "$",
    SCORE_5: "€",
    POINTS_TRAP: "T",
    START: "S",
    END: "⚑",
    WALL_3: "▓",
    WALL_2: "▒",
    WALL_1: "░",
    KEY: "⚷",
    DOOR: "▪",
    CRATE: "⧈",
    LIFE: "♥",
    PRESSURE_PLATE: "P",
    CRATE: "⧈",
    CRATE: "⧈",
    ARROW_RIGHT: "»",
    ARROW_LEFT: "«"
}


game = {
    "finished": False,
    "scores": 0,
    "map": "",
    "original_map": "",
    "x": 1,
    "y": 1,
    "door_x": None,
    "door_y": None,
    "lives": 3,
    "timer": 0
}


REAPPEARING_BLOCKS = [
    POINTS_TRAP,
    PRESSURE_PLATE
]


def read_map(file_name):
    lines = open(file_name).read().split('\n')
    raw_map = []
    for r, line in enumerate(lines):
        row = []
        for c, col in enumerate(line):
            row.append(col)
            if col == START:
                game['x'] = r
                game['y'] = c
            if col == DOOR:
                game["door_x"] = r
                game["door_y"] = c
        if len(row) > 1:
            raw_map.append(row)
    return raw_map


def print_map():
    """Cleans the map and prints current map on the screen."""
    clear()
    print("Scores:", game["scores"])
    print("Lives", game["lives"])
    for line in game["map"]:
        for c in line:
            color = colors_mapping.get(c, Fore.RESET)
            map_c = character_mapping[c]
            print(color + map_c, end="")
        print()
    print(Fore.RESET)


def move_player(move_x, move_y):
    game_map = game["map"]
    original_map = game["original_map"]

    x = game['x']
    y = game['y']
    new_x = x + move_x
    new_y = y + move_y    

    if game_map[new_x][new_y] == CRATE:
        if game_map[new_x + move_x][new_y + move_y]==NOTHING:
            game_map[new_x + move_x][new_y + move_y] = CRATE
            game_map[new_x][new_y] = NOTHING

    if game_map[new_x][new_y] not in (CRATE, WALL, WALL_1, WALL_2, WALL_3, DOOR):
        while game_map[new_x][new_y] == ARROW_RIGHT:
            new_y = new_y + 1
        while game_map[new_x][new_y] == ARROW_LEFT:
            new_y = new_y - 1
        if game_map[new_x][new_y] == SCORE_1:
            game["scores"] += 1
        if game_map[new_x][new_y] == SCORE_5:
            game["scores"] += 5
        if game_map[new_x][new_y] == POINTS_TRAP:
            game["scores"] -= 1
            game["lives"] -= 1
            if game["scores"] < 0:
                game["scores"] = 0
        if game_map[new_x][new_y] == LIFE:
            game["lives"] += 1
            if game["lives"] > 3:
                game["lives"] = 3
            if game["lives"] < 0:
                game["lives"] = 0
        if game_map[new_x][new_y] == KEY:
            game_map[game["door_x"]][game["door_y"]] = NOTHING
        if game_map[new_x][new_y] == END or game["lives"] == 0:
            game["finished"] = True
          
        if game_map[new_x][new_y] == PRESSURE_PLATE:
            game["timer"] = 10
            game_map[game["door_x"]][game["door_y"]] = NOTHING

        if game["timer"] > 0:
            game["timer"] -= 1
            if game["timer"] == 0:
                game_map[game["door_x"]][game["door_y"]] = DOOR

        if game_map[new_x][new_y] == END:
            game["finished"] = True
            
        if original_map[x][y] in REAPPEARING_BLOCKS:
            game_map[x][y] = original_map[x][y]
        else:
            game_map[x][y] = NOTHING

        x = new_x
        y = new_y
        game_map[x][y] = PLAYER

        game["x"] = new_x
        game["y"] = new_y

    if game_map[new_x][new_y] == WALL_1:
        game_map[new_x][new_y] = NOTHING

    if game_map[new_x][new_y] == WALL_2:
        game_map[new_x][new_y] = WALL_1

    if game_map[new_x][new_y] == WALL_3:
        game_map[new_x][new_y] = WALL_2


def handle_input():
    player_input = get_key()

    if player_input == "up":
        move_player(-1, 0)
    elif player_input == "down":
        move_player(1, 0)
    elif player_input == "right":
        move_player(0, 1)
    elif player_input == "left":
        move_player(0, -1)
    elif player_input == "exit":
        return False
    return True


def start_game(file_name):
    game["x"] = 1
    game["y"] = 1
    game["timer"] = 0
    game["finished"] = False
    game["map"] = read_map(file_name)
    game["original_map"] = copy.deepcopy(game["map"])

    while not game["finished"]:
        print_map()
        result = handle_input()
        if not result:
            break



def start_game(file_name):
    game["x"] = 1
    game["y"] = 1
    game["finished"] = False
    game["scores"] = 0
    game["lives"] = 3
    game["map"] = read_map(file_name)
    game["original_map"] = copy.deepcopy(game["map"])

    while not game["finished"]:
        print_map()
        result = handle_input()
        if not result:
            return None
    return game["scores"]
