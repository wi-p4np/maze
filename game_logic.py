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

character_mapping = {
    NOTHING: " ",
    WALL: "#",
    PLAYER: "O",
    SCORE_1: "$",
    SCORE_5: "€",
    POINTS_TRAP: "T",
    START: "S",
    END: "⚑"
}


game = {
    "finished": False,
    "scores": 0,
    "map": "",
    "x": 1,
    "y": 1,
}


def read_map(file_name):
    lines = open(file_name).read().split('\n')
    raw_map = []
    for line in lines:
        row = []
        for c in line:
            row.append(c)
        if len(row) > 1:
            raw_map.append(row)
    return raw_map


def print_map():
    """Cleans the map and prints current map on the screen."""
    clear()
    print("Scores:", game["scores"])
    for line in game["map"]:
        for c in line:
            map_c = character_mapping[c]
            print(map_c, end="")
        print()


def move_player(move_x, move_y):
    game_map = game["map"]

    new_x = game['x'] + move_x
    new_y = game['y'] + move_y

    if game_map[new_x][new_y] != WALL:
        if game_map[new_x][new_y] == SCORE_1:
           game["scores"] += 1
        if game_map[new_x][new_y] == SCORE_5:
           game["scores"] += 5
        if game_map[new_x][new_y] == POINTS_TRAP:
            game["scores"] -= 1
            if game["scores"] < 0:
                game["scores"] == 0
        if game_map[new_x][new_y] == END:
           game["finished"] = True

        game_map[game['x']][game['y']] = NOTHING
        game['x'] += move_x
        game['y'] += move_y
        game_map[game['x']][game['y']] = PLAYER


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
