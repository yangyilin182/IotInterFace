import base64
import json
import random
import string
import time
from urllib.parse import quote

import redis
import requests
from requests_toolbelt import MultipartEncoder
from config.Constants import config
from utils.Base64 import Base64
from utils.HmacEncryptUtil import EncryptHmac
from utils.JsonPath import JsonPath



class BaseApi:
    # def __init__(self):
    #     '''
    #     初始化redis数据库
    #     '''
    #     self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    '''
    公用api
    eg:requests
    '''
    config_template_headers = {
        # 'Cookie': 'JSESSIONID={}'.format(self.get_cookie()),
        # 'Cookie': 'JSESSIONID={0}'.format(self.get_cookie()),#索引占位用法
        'Cookie': 'JSESSIONID={cookie}'.format(cookie=config.cookie),  # 变量名占位用法
    }


    # 构造添加模板获取语音文件base64
    def make_base64(self, template_Content,params, headers=config_template_headers,**kwargs):
        # url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!uploadBase64TmpContent.action"
        try:
            params_params = {
                'tmpContent': quote(template_Content)
            }
            params_params.update(kwargs)
            params.update(params_params)
            r = requests.get(config.base64_url, params=params, headers=headers, verify=False)
            return r.json()['object']
        except Exception as e:
            raise  e

    # 构造审核模板需要的请求参数
    def make_data_to_send(self,companyId,template_name,template_Content,base64_str,fields,**kwargs):
        #基础公共部分数据 fields
        #传参部分数据
        try:
            base_params_fields = {'voiceInfo.companyId': companyId,
                             'voiceInfo.name': template_name,
                             'voiceInfo.tmpContent': template_Content,
                             'voiceInfo.tmpVoice': base64_str,
                             }
            base_params_fields.update(kwargs)
            fields.update(base_params_fields)
        except Exception as e:
            raise  e
        return fields

    #获取最新添加的验证码记录id及模板编号
    #todo 使用jsonpath优化提取数据
    def get_verifycode_info(self, data, headers=None):
        url= "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/codeTmp!init.action"
        r=requests.post(url,data=data,headers=headers,verify=False)
        print(r.json())
        verifycode_info={}
        verifycode_info['row_id']=r.json()['items'][0]['id']
        verifycode_info['template_id']=r.json()['items'][0]['tmpType']
        return verifycode_info

    # # TODO 封装基类处理请求
    #传文件 multipart/form-data，通过field字典传递参数并发送出去
    def send_file_by_stream(self, url, fields, params=None):
        try:
            m = MultipartEncoder(fields=fields)
            r = requests.post(url, data=m, params=params,headers={'Content-Type': m.content_type}, verify=False)
        except Exception as e:
            raise e
        print(r.content)
        return

    #传文件 multipart/form-data类型,通过可变参数**kwargs接收参数，通过kwargs字典发送出去
    def send_file_by_stream_variable_param(self, url, params=None,**kwargs):
        try:
            m = MultipartEncoder(kwargs)
            r = requests.post(url, data=m, params=params,headers={'Content-Type': m.content_type}, verify=False)
        except Exception as e:
            raise e
        print(r.content)
        return

    # 通过设备序列号获取设备id
    def get_deviceid_by_sn(self, companyId, device_sn= config.device_sn,headers=config_template_headers):
        try:
            params = {
                'companyId': companyId
            }
            r = requests.post(config.get_deviceid_url, data=config.get_deviceid_data, params=params,headers=headers,verify=False).json()
            # eg:jsonpath("$.department[?(@.id==%s)]" % r["id"])[0]["name"]==name
            # eg: $.data.forecast[?(@.type == "小雨")].date 表示获取的是data下forecast数组中天气类型为“小雨”的日期

            # expr = "$..items[?(@.code == {0})].deviceid".format(device_sn)
            # expr = f"$..items[?(@.code == {device_sn})].deviceid"
            # 上面两种表达式执行结果：$..items[?(@.code == f8_ms_double_0010)].deviceid, 取到的code内容未加'',取不到值
            # $..book[?(@.price < 10)]
            # expr = "$..items[?(@.code == 'f8_ms_double_0010')].deviceid"
            # 执行结果: $..items[?(@.code == 'f8_ms_double_0010')].deviceid

            expr = "$..items[?(@.code == '%s')].deviceid" % device_sn
            result=JsonPath.jsonpath(r,expr)
            print('================================================')
            print(result)
        except Exception as e:
            raise  e
        # 注意此处 jsonpath提取到的数据是list类型，需要取第一个值，取到的值为int，需要再次转换为str
        #todo redis存储依赖数据
        # self.r.hset('deviceid',config.device_sn,str(result[0]))
        # return
        return str(result[0])

    #签名
    def sign(self,data,app_secret=config.app_secret):
        try:
            ##排序后的参数，得到list[tuple]类型的结构，dict()函数转化为dict字典类型
            sorted_data = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
            # 将key:value结构字典编码为key1=value1&key2=value2&key3=value3键值对
            # data_to_sign=urllib.parse.urlencode(data) 注意，此方法在此不可用，经验证，会打乱已经排序后的字典顺序
            signvalue = ''
            for k, v in sorted_data.items():
                signvalue += (k + '=' + v + '&')
            #  data_to_sign=signvalue[:-1] 切片也可去掉结尾&字符
            data_to_sign = signvalue.strip('&')
            #获取bytes类型加密结果
            sign = EncryptHmac.encrypt_sha256_digest(app_secret.encode('utf-8'), data_to_sign.encode('utf-8'))
            # signature = Base64.encrypt_base64(sign)
            # signature = base64.urlsafe_b64encode(sign)
            #服务端做了签名结果校验，注意需要用urlsafe_b64encode,否则可能会验签不通过
            signature = Base64.encrypt_urlsafe_base64(sign)
        except Exception as e:
            raise e
        return signature
    #构造发送的post请求推送数据
    def make_data(self,message,push_template):
        try:
            timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
            nonce = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 32)))
            data = {
                'appkey': config.appkey,
                'method': 'push',
                'devicesn': config.device_sn,
                'message': message,
                'push_template': push_template,
                'timestamp': timestamp,
                'nonce': nonce
            }
            signature = self.sign(data)
            data['sign'] = signature.decode('utf-8')
            print('data to send is %s' % data)
        except Exception as e:
            raise  e
        return data




