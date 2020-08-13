import pymysql


class Operation_Mysql():

    def __init__(self, host, user, password, db, charset='utf8'):
        '''
        初始化连接mysql的操作
        :param host: 传入mysql主机地址
        :param user: 传入连接mysql用户名
        :param password: 传入连接密码
        :param db: 指定数据库名
        :param charset: 字符编码格式  默认utf8编码
        '''
        self.connect = pymysql.connect(  # 连接mysql
            host=host,
            user=user,
            password=password,
            db=db,
            charset=charset,
        )

    def __execute_sql(self, sql):
        '''
        该方法是一个私有方法，主要用于执行sql语句
        :param sql: 传入要执行的sql语句
        :return: 如果是查询语句，将会返回查询的结果值。
        :return_type:返回tuple类型
        '''
        with self.connect.cursor() as cursor:  # 通过游标对象获取容器
            cursor.execute(sql)  # 通过游标对象执行sql语句
            data = cursor.fetchall()  # 获取执行sql后的返回数据，插入数据和创建表是没有返回数据的，结果为空元组
        self.connect.commit()  # 通过连接对象将对数据库的操作进行提交
        return data  # 返回查询后的数据

    def insert_data(self, table, *args):
        '''
        封装的插入数据的方法
        :param table: 传入要插入数据的表名
        :param args: 传入插入的数据值，传入类型是元组
        '''
        sql = "insert into %s values %s" % (table, tuple(*args))
        self.__execute_sql(sql)  # 调用私有方法，执行sql语句

    def create_table(self, tbale, table_type):
        '''
        封装创建表的方法
        :param tbale: 传入要创建的表名
        :param table_type: 传入要创建表的字段 数据类型和表约束；传入一个字符串的类型
        '''
        sql = "create table %s(%s)" % (tbale, table_type)
        self.__execute_sql(sql)  # 调用私有方法，执行sql语句

    def select_data(self, sql):
        '''
        封装的查询语句的方法
        :param sql: 因查询的方式太多，所以直接传入sql语句进行查询
        :return: 返回查询后的结果数据
        '''
        data = self.__execute_sql(sql)
        return data

    def execute_sql(self, sql):
        '''
        公有的执行sql语句方法；主要用于修改数据和删除数据
        :param sql: 传入需要执行的sql语句
        '''
        self.__execute_sql(sql)



def close_connect(self):
    '''
    主要用于关闭连接
    :return:
    '''
    self.connect.close()




if __name__ == '__main__':
    # 创建操作数据库对象
    operation = Operation_Mysql('localhost', 'root', '123456', 'hrdb')
    # 创建表
    type = 'name varchar(20),age int,sex char(10)'
    operation.create_table('userInfo', type)
    # 插入数据
    tuple1 = ['zhangsan', 18, 'man']
    operation.insert_data('userInfo', tuple1)
    # 查询数据，并输出
    sql = 'select * from userInfo'
    print(operation.select_data(sql))
    # 删除数据
    sql = "delete from userInfo"
    operation.execute_sql(sql)
    operation.close_connect()