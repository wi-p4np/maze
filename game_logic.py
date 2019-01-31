from colorama import Fore
from utils import clear
from game_input import get_key

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

colors_mapping = {
    WALL: Fore.YELLOW,
    SCORE_1: Fore.GREEN,
    SCORE_5: Fore.CYAN,
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
    DOOR: "▪"
}


game = {
    "finished": False,
    "scores": 0,
    "map": "",
    "x": 1,
    "y": 1,
    "door_x": None,
    "door_y": None
}


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
    for line in game["map"]:
        for c in line:
            color = colors_mapping.get(c, Fore.RESET)
            map_c = character_mapping[c]
            print(color + map_c, end="")
        print()
    print(Fore.RESET)


def move_player(move_x, move_y):
    game_map = game["map"]

    new_x = game['x'] + move_x
    new_y = game['y'] + move_y

    if game_map[new_x][new_y] not in (WALL, WALL_1, WALL_2, WALL_3, DOOR):
        if game_map[new_x][new_y] == SCORE_1:
            game["scores"] += 1
        if game_map[new_x][new_y] == SCORE_5:
            game["scores"] += 5
        if game_map[new_x][new_y] == POINTS_TRAP:
            game["scores"] -= 1
            if game["scores"] < 0:
                game["scores"] = 0
        if game_map[new_x][new_y] == KEY:
            game_map[game["door_x"]][game["door_y"]] = NOTHING
        if game_map[new_x][new_y] == END:
            game["finished"] = True

        game_map[game['x']][game['y']] = NOTHING
        game['x'] += move_x
        game['y'] += move_y
        game_map[game['x']][game['y']] = PLAYER

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
    game["finished"] = False
    game["map"] = read_map(file_name)

    while not game["finished"]:
        print_map()
        result = handle_input()
        if result == False:
            break
