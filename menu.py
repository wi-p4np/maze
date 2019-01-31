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
        print("EXIT - exit the game")

        print()
        print("Which option do you want?")
        selected_value = input()
    
        try:
            map_index = int(selected_value)
            file_path = "./maps/" + maps[map_index]
            start_game(file_path)   
        except ValueError:
            pass

        if selected_value == 'EXIT':
            break


if __name__ == '__main__':
    main()