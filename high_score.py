from datetime import datetime
highscore_list = []
HIGHSCORE_BOARD = './highscore_board.csv'


def add_highscore(map_name, score):
    highscore = tuple([map_name, str(datetime.now().date()), score])
    highscore_list.append(highscore)
    highscore_list.sort(key=lambda x: x[2], reverse=True)
    save_highscore(highscore)
    return highscore_list


def print_highscore():
    print("10 top scores")
    for i in highscore_list[:10]:  # prints out only 10 best scores
        print('map: ' + str(i[0]) + ' | ' + 'date: ' + str(i[1]) +
              ' | ' + 'score: ' + str(i[2]))


def save_highscore(highscore):
    file = open(HIGHSCORE_BOARD, 'a')
    file.write(str(highscore[0]) + ',' + str(highscore[1]) + ',' +
               str(highscore[2]) + '\n')
    file.close()


def read_highscore():
    global highscore_list
    lines = open(HIGHSCORE_BOARD).readlines()[1:]
    for line in lines:
        line = line.strip().split(',')
        highscore = tuple([str(line[0]), str(line[1]), int(line[2])])
        highscore_list.append(highscore)
        highscore_list.sort(key=lambda x: x[2], reverse=True)
    return highscore_list
