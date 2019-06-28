from Spider.Managers import MongoManager
from Config import *
import datetime

def generateMovieID():

    mongo = MongoManager.DBManager()
    datas = mongo.get_data(MOVIE_INFO)
    id = 0
    for data in datas:
        mongo.update_attr(MOVIE_INFO, data['url'], 'movieID', id)
        id += 1


def main():
    start = datetime.datetime.now()

    generateMovieID()

    end = datetime.datetime.now()
    print("调度总时长：", end - start)


if __name__ == '__main__':
    main()
