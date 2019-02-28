import os
import utils
from colorama import init
from game_logic import start_game
from high_score import (
    add_highscore, print_highscore, read_highscore
)
init()
read_highscore()


def main():
    maps = os.listdir("./maps")

    while True:
        utils.clear()
        print_highscore()

        print("  MENU")
        print("********")

        for i in range(len(maps)):
            name = maps[i]
            print(i, "-", name[:-4])
        print("EXIT - exit the game")

        #print()
        print("Which option do you want?")
        selected_value = input()
  
        try:
            map_index = int(selected_value)
            file_path = "./maps/" + maps[map_index]
            score = start_game(file_path)  
            if score:
                highscore = add_highscore(maps[map_index][:-4], score)
                print(highscore) 
        except ValueError:
            pass

        if selected_value == 'EXIT':
            break


if __name__ == '__main__':
    main()
