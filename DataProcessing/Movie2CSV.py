from Spider.Managers.MongoManager import *
from Config import *
import datetime
import random
import csv

def supplementYear():
    mongo = DBManager()
    datas = mongo.get_data(MOVIE_INFO)
    count = 1
    for data in datas:
        # if count > 500:
        #     break
        if 'release_time' in data:
            year = data['release_time']
            # print(year, count)
            if year < 1800 or year > 2019:
                print('###########', year)
                time = random.randint(1990, 2018)
                mongo.update_attr(MOVIE_INFO, data['url'], 'release_time', time)
            count += 1
        else:
            time = random.randint(1990, 2018)
            print('random year is ', time)
            mongo.update_attr(MOVIE_INFO, data['url'], 'release_time', time)


def movieProcess():
    mongo = DBManager()
    datas = mongo.get_data(MOVIE_INFO)
    count = 1
    for data in datas:
        tuple = {'id': data['movieID'], 'name': data['title'], 'year': data['release_time'], 'length': data['duration'], 'rating': data['rated'], 'score': data['score']}
        mongo.save_data(MOVIE_TBL, tuple)
        print(count)
        count += 1


def main():
    start = datetime.datetime.now()

    movieProcess()

    end = datetime.datetime.now()
    print("调度总时长：", end - start)


if __name__ == '__main__':
    main()
