from Spider import Scheduler
import Config


def main():
    scheduler = Scheduler.Scheduler(Config.MOVIE_URLS, Config.MOVIE_INFO)
    scheduler.run()


if __name__ == '__main__':
    main()


# class myThread(Thread):
#     def __init__(self, src_tag, dest):
#         Thread.__init__(self)
#         self.tag = src_tag
#         self.src = Config.MOVIES[src_tag]
#         self.dest = dest
#
#     def run(self):
#         print("开始", (self.tag+1), "号线程")
#         my_spider = Scheduler.Scheduler(self.src, self.dest)
#         my_spider.run()
#
#
# my_threads = []
#
# for i in range(0, 1):
#     my_thread = myThread(i, Config.MOVIE_INFO)
#     my_threads.append(my_thread)
#     my_threads[i].start()
