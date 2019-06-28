from Spider.Managers.MongoManager import *
from Config import *
import datetime


def deleteRedundant():
    mongo = DBManager()
    datas = mongo.get_data(MOVIE_INFO)
    count = 0
    for data in datas:
        types = data['types']
        for _type in types:
            if mongo.find_data(TYPE_TBL, 'name', _type) is False:
                tuple = {'id': count, 'name': _type}
                print("未插入的类型：\t", count, '\t', _type)
                mongo.save_data(MOVIE_TBL, tuple)
                count += 1
            else:
                print("重复", _type)
    print("总共的类型数量：", count)



def main():
    start = datetime.datetime.now()

    deleteRedundant()

    end = datetime.datetime.now()
    print("调度总时长：", end - start)


if __name__ == '__main__':
    main()