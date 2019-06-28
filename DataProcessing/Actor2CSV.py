from Spider.Managers.MongoManager import *
from Config import *
import datetime


def findTooLong():
    mongo = DBManager()
    datas = mongo.get_data(MOVIE_INFO)
    row = 0
    for data in datas:
        for actor in data['actors']:
            if len(actor) > 49:
                print(row, actor)
        row += 1


def deleteRedundant():
    mongo = DBManager()
    mongo.clear_db(ACTOR_TBL)
    datas = mongo.get_data(MOVIE_INFO)
    row = 1
    count = 0
    for data in datas:
        actors = data['actors']
        for actor in actors:
            if mongo.find_data(ACTOR_TBL, 'name', actor) is False and len(actor) < 49:
                tuple = {'id': count, 'name': actor}
                print("未插入的类型：\t", count, '\t', actor, row)
                mongo.save_data(ACTOR_TBL, tuple)
                count += 1
            else:
                print(row, "重复", actor)
        row += 1
    print("总共的类型数量：", count)



def main():
    start = datetime.datetime.now()

    deleteRedundant()

    end = datetime.datetime.now()
    print("调度总时长：", end - start)


if __name__ == '__main__':
    main()