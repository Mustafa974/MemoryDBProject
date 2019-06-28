from Spider.Managers.MongoManager import *
from Config import *
import datetime


def getAss():
    mongo = DBManager()
    datas = mongo.get_data(MOVIE_INFO)
    count = 1
    time = 1
    for data in datas:
        movieID = data['movieID']
        types = data['types']
        for _type in types:
            typeID = mongo.find_id_by_name(TYPE_TBL, _type)
            row = {'typeID': typeID, 'movieID': movieID}
            print('电影：', time, "关系：", count, "电影id：", movieID, "类型id：", typeID)
            mongo.save_data(MOVIE_TYPE_TBL, row)
            count += 1
        time += 1
    print("总共的类型数量：", count)



def main():
    start = datetime.datetime.now()

    getAss()

    end = datetime.datetime.now()
    print("调度总时长：", end - start)


if __name__ == '__main__':
    main()