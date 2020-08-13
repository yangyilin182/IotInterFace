from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import time

#主机管理类，用于任务派发
class Master:

    def __init__(self):
        # 派发出去的任务队列
        self.dispatched_task_queue = Queue()
        # 完成的任务队列
        self.finished_task_queue = Queue()

    def get_dispatched_task_queue(self):
        return self.dispatched_task_queue

    def get_finished_task_queue(self):
        return self.finished_task_queue


    #开始任务
    def start(self):

        # 把派发作业队列和完成作业队列注册到网络上
        BaseManager.register('get_dispatched_task_queue', callable=self.get_dispatched_task_queue)
        BaseManager.register('get_finished_task_queue', callable=self.get_finished_task_queue)

        # 监听端口和启动服务，authkey为验证码，自己随便取的，address改成自己的ip
        manager = BaseManager(address=('127.0.0.1', 8888), authkey='taimei'.encode("utf-8"))
        manager.start()

        # 使用上面注册的方法获取队列
        dispatched_tasks = manager.get_dispatched_task_queue() #获取派发队列
        finished_tasks = manager.get_finished_task_queue() #获取返回队列

        while True:
            #待处理任务：data_test=[{"name":"张三"},{"name":"李四"},{"name":"王五"},{"name":"麻子"},{"name":"如花"},{"name":"西施"}]
            data_test=[{"name":"张三"},{"name":"李四"},{"name":"王五"},{"name":"麻子"},{"name":"如花"},{"name":"西施"}]
            for index,item in enumerate(data_test):
                dispatched_tasks.put(item)
                print("派发任务： "+str(index))

            #监听返回结果
            while not dispatched_tasks.empty():
                result = finished_tasks.get()
                print("-------返回数据----------")
                print(result)

            #暂停10秒后继续进行下一轮的任务派发
            time.sleep(10)
        manager.shutdown()
#测试：首先执行master.py派发任务,然后我再运行slave.py去从队列中获取任务
#这个slave可以复制很多份到不同的主机上去同时运行，它们都会共享一个队列，从master中获取任务执行。

#在python中的多线程，它其实从严格意义上来讲，并不是真正的多线程
#用多线程我们还不如使用多进程。使用多进程的好处，它可以实现分布式多机并行。多个客户端共享一个任务队列
if __name__ == "__main__":
    master = Master()
    master.start()
