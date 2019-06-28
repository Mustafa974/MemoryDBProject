from Spider.Managers import ProxyManager, HeaderManager, MongoManager
import Config
import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import re
import datetime
import random
import csv


class Scheduler(object):

    def __init__(self, src_col, dest_result_col):
        """
        初始化
        :param src_col:
        :param dest_result_col:
        """
        self.src_col = src_col
        self.dest_col = dest_result_col
        self.mm = MongoManager.DBManager()
        self.pm = ProxyManager.Proxy()
        self.hm = HeaderManager.Headers()

    def get_page_index(self, url):
        """
        获取索引页信息并返回，使用偏移量改变对象
        :param keyword:
        :return:
        """
        # 禁用安全请求警告
        urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url)
        try:
            if response.status_code == 200:
                return response.text
            return None
        except RequestException:
            print('请求索引页失败')
            return None

    def parse_page_index(self, html):
        """
        解析索引页信息，从中获取并返回详情页url
        :return:
        """
        doc = pq(html)
        items = doc('body > div.wrap > div.wrapper > div.ss-3.clear a').items()
        for item in items:
            url = item.attr('href')
            data = {
                'url': 'http://www.imdb.cn' + url
            }
            self.mm.save_data(self.dest_col, data)

    def parse_page_detail(self, html):
        """
        根据html获取网页所需信息并将数据打包为dict文件返回
        :param html:
        :param page_type:
        :return: 返回每个细节网页中全部所需信息的dict数据
        """
        attrs = [
            '片名', '别名', '导演', '主演', '时长', '上映时间', '类型', '分级', '国家', '评分'
        ]
        title = ''
        alias = ''
        directors = []
        actors = []
        duration = []
        release_time = ''
        types = []
        rated = []
        region = []
        score = ''
        doc = pq(html)
        items = doc('body > div.wrap > div.wrapper > div.left-2.clear > div.fk.clear > div.fk-1 > div.fk-3 > '
                    'div.bdd.clear > ul li').items()
        for item in items:
            data = item.text()
            for attr in attrs:
                if attr in data:
                    if attr is not '分级':
                        value = data.replace(attr, '').replace('：', '')
                    if attr is '时长':
                        index = value.find('&')
                        value = value[0:index]
                        duration = self.split_arr(' / ', value)
                    elif attr is '上映时间':
                        index = value.find('&')
                        release_time = value[0:index]
                    elif attr is '主演':
                        actors = self.split_arr('  ', value)
                    elif attr is '国家':
                        index = value.find('声音')
                        value = value[0:index].replace('      ', '')
                        region = self.split_arr('  ', value)
                    elif attr is '评分':
                        score = item('i img').items()
                        tag = 0
                        for scorei in score:
                            if tag is 0:
                                score = scorei.attr('src').replace('/Public/images/goldstar', '').replace('.gif', '') + ' out of 10'
                            tag += 1
                    elif attr is '类型':
                        index = value.replace(' ', '').find('&') + 20
                        value = value[index:]
                        index = value.find('&')
                        types = self.split_arr('  ', value[0:index])
                    elif attr is '分级':
                        value = data.replace(attr, '').replace('：', ':')
                        index = value.replace(' ', '').find('&') + 20
                        value = value[index:]
                        index = value.find('&') + 41
                        value = value[index:]
                        index = value.find('颜色')
                        rated = self.split_arr('  ', value[0:index])
                    elif attr is '片名':
                        title = value
                    elif attr is '别名':
                        alias = value
                    elif attr is '导演':
                        directors = self.split_arr('）', value.replace('  ', ''))
        result = {
            'title': title,
            'alias': alias,
            'directors': directors,
            'actors': actors,
            'duration': duration,
            'release_time': release_time,
            'types': types,
            'rated': rated,
            'region': region,
            'score': score
        }
        return result

    def split_arr(self, symbol, _data):
        """
        处理字符串
        按照指定字符分割
        去除字串开头结尾的空格，替换换行符
        :param _data:
        :return:
        """
        results = []
        datas = re.split(symbol, _data)
        for data in datas:
            data = data.replace('\n', '').lstrip().rstrip()
            if data is not '' and data is not ' ':
                results.append(data)
        return results

    def save_page_detail(self):
        datas = self.mm.get_data(self.src_col)
        attrs = [
            'title', 'alias', 'directors', 'actors', 'duration', 'release_time', 'types', 'rated', 'region', 'score'
        ]
        count = 1
        for data in datas:
            print('')
            print('------------ page', count, self.src_col, '------------')
            print(data['url'])
            html = self.get_page_index(data['url'])
            result = self.parse_page_detail(html)
            for attr in attrs:
                if result[attr] is '' or len(result[attr]) is 0:
                    continue
                self.mm.update_attr(self.dest_col, data['url'], attr, result[attr])
                self.mm.delete_data(self.src_col, data['_id'])
                # print(attr, ':', result[attr])
            count += 1

    def get_director_name(self):
        datas = self.mm.get_data(Config.MOVIE_INFO)
        count = 0
        for data in datas:
            if 'directors' in data:
                directors = data['directors']
                for director in directors:
                    if '未知' in director:
                        # print('')
                        # print('############')
                        # print(data['url'])
                        count += 1
                        self.mm.update_attr(Config.MOVIE_INFO, data['url'], 'directors', None)

    def get_random_rating(self):
        ratings = [
            'PG',
            'R',
            'PG-13',
            'KT',
            'G',
            'U',
            'S'
        ]
        rating = 'NR'
        temp = random.randint(1, 10)
        if temp < 8:
            rating = ratings[temp-1]
        print(temp, ':', rating)
        return rating

    def create_null_data(self):
        datas = self.mm.get_data(Config.MOVIE_INFO)
        count = 0
        for data in datas:
            if 'rated' in data and data['rated'].replace(' ', '') == '':
                count += 1
                rated = self.get_random_rating()
                self.mm.update_attr(Config.MOVIE_INFO, data['url'], 'rated', rated)
            else:
                count += 1
                rated = self.get_random_rating()
                self.mm.update_attr(Config.MOVIE_INFO, data['url'], 'rated', rated)
        print(count)

    def write_to_csv(self, filename, data):
        csvfile = open(filename, 'wb')
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'url', 'title', 'alias', 'directors', 'actors', 'release_time', 'duration', 'types', 'rated', 'region', 'score'])
        writer.writerows(data)

    def export_data(self):
        datas = self.mm.get_data(Config.MOVIE_INFO)
        count = 0
        for data in datas:
            if count > 1:
                break
            count += 1
            list = data['directors']
            directors = '，'.join(list)
            list = data['actors']
            actors = '，'.join(list)
            list = data['types']
            types = '，'.join(list)
            list = data['region']
            region = '，'.join(list)
            row = str(data['_id'])+','+data['url']+','+data['title']+','+data['alias']+','+directors+','+actors
            row += str(data['release_time'])+','+str(data['duration'])+','+types+','+data['rated']+','+region+','+str(data['score'])
            print(row)
            self.write_to_csv('/Users/mustafa/Desktop/ImDB.csv', row)


    def run(self):
        start = datetime.datetime.now()

        self.export_data()

        end = datetime.datetime.now()
        print("调度总时长：", end - start)


if __name__ == '__main__':
    s = Scheduler(Config.MOVIE_URLS, Config.MOVIE_INFO)
    s.run()


# 导演 未知 34906
# 时长 伪造数据（80~140）约11w
# 类型 未分类 68470
# 演员 未知 30241
# 地区 未知 14758
# 评分 伪造浮点数据（1~10）保留一位小数 约8w
# 别名 无别名 255056
# 等级 PG R PG-13 KT G U S 各10%概率，NR 30%概率

