import yaml

class yml:

    @classmethod
    def load_yaml(self,filename):
        '''
        #解析加载yaml文件
        :param filename: yaml文件带路径全名称
        :return: 返回Python对象
        '''
        try:
            with open(filename,'r') as fp:
                f = yaml.safe_load(fp.read())
        except Exception as e:
            raise e
        return f

    @classmethod
    def dump_yaml(self,filename,data):
        '''
        #将Python对象dump到yaml文件中
        :param filename:
        :param data:
        :return:
        '''
        try:
            with open(filename,'w') as fp:
                yaml.safe_dump(data,fp)
        except Exception as e:
            raise e
        return





