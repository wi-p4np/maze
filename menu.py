from colorama import init
init()
import os
from game_logic import start_game
import utils


def main():
    maps = os.listdir("./maps")

    while True:
        utils.clear()

        print("  MENU")
        print("********")

        for i in range(len(maps)):
            name = maps[i]
            print(i, "-", name[:-4])

        print()
        print("Which map do you want?")
        map_index = int(input())

        file_path = "./maps/" + maps[map_index]

        start_game(file_path)


if __name__ == '__main__':
    main()
