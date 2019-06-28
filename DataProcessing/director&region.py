import threading

import pymongo


USER_str = 'localhost'
DB_str = 'InMemDBClass'
COL_str = 'MovieInfo'


def region():
    client = pymongo.MongoClient(USER_str)
    db = client[DB_str]
    col = db[COL_str]
    col_region = db['region']
    col_mr = db['movie_in_region']
    data = col.find()
    for movie in data:
        for region_name in movie['region']:
            found = col_region.find_one({'name_': region_name})
            if found is None:
                region_id = col_region.count()
                col_region.insert_one({'id_': region_id, 'name_': region_name})
            else:
                region_id = found['id_']
            # if col_mr.find_one({'movie_id': movie['movieID'], 'region_id': region_id}) is not None:
            try:
                col_mr.insert_one({'movie_id': movie['movieID'], 'region_id': region_id})
                print('region:', movie['movieID'])
            except:
                print('重复')


def director():
    client = pymongo.MongoClient(USER_str)
    db = client[DB_str]
    col = db[COL_str]
    col_director = db['director']
    col_dm = db['director_direct_movie']
    # data = col.find({'movieID': {'$gte': 137298}})
    data = col.find()
    for movie in data:
        for director_name in movie['directors']:
            if director_name.__len__() > 50:
                try:
                    director_name = director_name.split(' ', 2)[1]
                except:
                    director_name = director_name.split('/', 2)[0]

            found = col_director.find_one({'name_': director_name})
            if found is None:
                director_id = col_director.count()
                col_director.insert_one({'id_': director_id, 'name_': director_name})
            else:
                director_id = found['id_']
            # if col_dm.find_one({'movie_id': movie['movieID'], 'director_id': director_id}) is not None:
            try:
                col_dm.insert_one({'movie_id': movie['movieID'], 'director_id': director_id})
                print('director:', movie['movieID'])
            except:
                print('重复')


class Region(threading.Thread):
    def run(self):
        region()


class Director(threading.Thread):
    def run(self):
        director()


Region().start()
Director().start()
