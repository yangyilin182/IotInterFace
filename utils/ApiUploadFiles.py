
import requests
from requests_toolbelt import MultipartEncoder


class ApiUploadFiles:

    # 流式传输（大）文件 multipart/form-data，通过field字典传递参数并发送出去
    def send_file_by_stream(self, url, fields, params=None):
        try:
            m = MultipartEncoder(fields=fields)
            r = requests.post(url, data=m, params=params, headers={'Content-Type': m.content_type}, verify=False)
        except Exception as e:
            raise e
        print(r.content)
        return

    # 流式传输(大)文件 multipart/form-data,通过可变参数**kwargs接收参数，通过kwargs字典发送出去
    def send_file_by_stream_variable_param(self, url, params=None, **kwargs):
        try:
            m = MultipartEncoder(kwargs)
            r = requests.post(url, data=m, params=params, headers={'Content-Type': m.content_type}, verify=False)
        except Exception as e:
            raise e
        print(r.content)
        return

    #传送 Multipart-Encoded 类型文件
    # eg:files = {'file': open('report.xls', 'rb')}
    def send_file(self,url,fileObj,params=None):
        try:
            r=requests.post(url,files=fileObj,params=params,verify=False)
        except Exception as e:
            raise  e
        return
