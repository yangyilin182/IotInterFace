import time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

#从机类
class Slave:

    def __init__(self):
        # 派发出去的任务队列
        self.dispatched_task_queue = Queue()
        # 完成的任务队列
        self.finished_task_queue = Queue()

    def start(self):
        # 把派发任务队列和完成任务队列注册到网络上
        BaseManager.register('get_dispatched_task_queue')
        BaseManager.register('get_finished_task_queue')

        # 连接master
        server = '127.0.0.1'
        print('连接主机服务器 %s...' % server)
        manager = BaseManager(address=(server,8888), authkey='taimei'.encode("utf-8"))
        manager.connect()

        # 使用上面注册的方法获取队列
        dispatched_tasks = manager.get_dispatched_task_queue()
        finished_tasks = manager.get_finished_task_queue()

        # 运行作业并返回结果，这里只是模拟作业运行，所以返回的是接收到的作业
        while True:
            try:
                task = dispatched_tasks.get(timeout=1)
                print("正在执行任务..."+str(task))
                #这里省略掉处理任务的过程
                time.sleep(1)
                finished_tasks.put(task["name"]+" 任务已经执行完毕！")
            except Exception:
                continue

if __name__ == "__main__":
    slave = Slave()
    slave.start()
