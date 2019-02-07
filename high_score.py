from datetime import datetime
highscore_list = []

def add_highscore(map_name, score):
    highscore = tuple([map_name, str(datetime.now().date()), score])
    highscore_list.append(highscore)
    highscore_list.sort(key=lambda x: x[2], reverse=True)
    return highscore_list


def print_highscore():
    for i in highscore_list:
        print(str(i) + '\n')