from utils import clear
from game_input import get_key

NOTHING = "0"
WALL = "1"
PLAYER = "2"
SCORE = "3"
START = "S"
END = "E"

character_mapping = {
    NOTHING: " ",
    WALL: "#",
    PLAYER: "O",
    SCORE: "$",
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
        if game_map[new_x][new_y] == SCORE:
           game["scores"] += 1
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
   game["map"] = read_map(file_name)

   while not game["finished"]:
       print_map()
       result = handle_input()
       if result == False:
           break