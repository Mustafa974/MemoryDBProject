from Spider.Managers.MongoManager import *
from Config import *
import datetime


def getAss():
    mongo = DBManager()
    mongo.clear_db(MOVIE_ACTOR_TBL)
    datas = mongo.get_data(MOVIE_INFO)
    count = 1
    time = 1
    for data in datas:
        movieID = data['movieID']
        actors = data['actors']
        for actor in actors:
            if len(actor) < 49:
                actorID = mongo.find_id_by_name(ACTOR_TBL, actor)
                row = {'actorID': actorID, 'movieID': movieID}
                print('电影数：', time, "关系：", count, "电影id：", movieID, "演员id：", actorID)
                mongo.save_data(MOVIE_ACTOR_TBL, row)
                count += 1
        time += 1
    print("总共的关系数量：", count)



def main():
    start = datetime.datetime.now()

    getAss()

    end = datetime.datetime.now()
    print("调度总时长：", end - start)


if __name__ == '__main__':
    main()