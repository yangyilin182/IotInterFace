import json
import random
import string
import time
import urllib
from urllib.parse import quote

import pytest
from requests_toolbelt import MultipartEncoder
import requests


def test_post():
    # data = make_data(kwargs)
    server_url = "https://iotmessage-testing.cloudentify.com/v1/audio"
    data = {'devicesn': 'f14_4g_wifi_0010', 'method': 'push', 'push_template': '1', 'message': '1',
            'appkey': '989F23B783CBD649D25D', 'timestamp': '20200520174844', 'nonce': 'iAMd',
            'sign': 'MO4LihFfiLnY0ASbkEmobEqGrfj5UcsHyTp-S45gT9Y='}
    print('→◇ ' + json.dumps(data))
    print('←◆ ' + requests.post(server_url, data).text + '\n')


def test_urlencode():
    import urllib.parse
    values = {}
    values['username'] = '02蔡彩虹'
    values['password'] = 'ddddd?'
    # 将key=value结构的dict进行urlencode
    data = urllib.parse.urlencode(values)
    print(data)
    #将单个字符串进行urlencode
    s = '长春'
    urllib.parse.quote()
    s = urllib.parse.quote(s)
    print(s)


#multipart/form-data类型file上传
def test_file1():
    m = MultipartEncoder(
        fields={'field0': 'value', 'field1': 'value',
                # 'field2': ('filename', open('file.py', 'rb'), 'text/plain'
                'field2': ('filename', open('file.py', 'rb'), 'text/plain')}
    )
    print("=================", m.content_type)
    r = requests.post('http://httpbin.org/post', data=m,
                      headers={'Content-Type': m.content_type})
#添加模板
def upload_base64(params,headers):
    url="https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!uploadBase64TmpContent.action"
    r=requests.get(url,params=params,headers=headers,verify=False)
    print(r.json())
    return r.json()

def test_upload_base64():
    params={
           'speed': '50',
           'tempType': '1',
           'tmpContent': quote('开机')
    }
    headers={
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'keep-alive',
           'Cookie': 'JSESSIONID=CA7CD79F0AD0EEED7FD265971DAEA4AE',
           'Host': 'iotoperation-testing.cloudentify.com',
           'Referer': 'https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/add.jsp',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/77.0.3865.120 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'
    }
    upload_base64(params,headers)

#审核全企业开机模板
def audit_poweron_module(fields):
    url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!add.action"
    m=MultipartEncoder(fields=fields)
    r = requests.post(url, data=m, headers={'Content-Type': m.content_type}, verify=False)
    print(r.content)
    return

#审核开机模板
def test_audit_poweron_module():
    fields={'voiceFile': '', 'voiceInfo.companyId': '147', 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
            'voiceInfo.name': '开机', 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
            'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '1',
            'voiceInfo.tmpContent': '开机', 'voiceInfo.tmpType': '0',
            'voiceInfo.tmpVoice': 'IyFBTVIKBCsZN/CkyDn/wACCAARliVD0/+/xRf1vEJwEN+qE+/0t8htdRlvoBKVQlD7o46uJEf6UiAQ3KBuP+MibDkxou5IEkHgLX/rGUAaSISwWBACXEm+e22u71ATUCARbYBau5FPCdNgBLeIER98Wnf2xcoXYgpcABHH5FqzrgrZEIZK5FATUyxmt0czSGsxoBtYE5+Ys+DvIpsDgmRqCBFMjhjrnZrBzwTRiigRLcQ5cykhbW5knK14EFEeMzI2xg/6B5+aKBKvU+g/KQjtsbnHs4ARImhvemGPeiUUIvVwEcc0irLj3b6JJSIHkBEjKIq7D3kLosMMajgRx0iKr+J1/CsKgAdAESM0iivOd0qMoWLogBHHSKD3o5y8a0HSjPARIzSK+s4ITaT8CBfwEpvIiy4JlItQif4SABNNRXfMAEjmx1AGRog==',
            'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'}
    audit_poweron_module(fields)


def test_addmudule_and_audit():
    '''
    全企业开机模板添加与审核
    :return:
    '''
    companyId = '147'
    template_Content = '开机'
    template__name = '开机'
    cookie = 'CA7CD79F0AD0EEED7FD265971DAEA4AE'
    params = {
        'speed': '50',
        'tempType': '1',
        'tmpContent': quote(template_Content)
    }
    headers = {
        'Cookie': f'JSESSIONID={cookie}',
    }
    r = upload_base64(params, headers)
    base64_str = r['object']
    print(base64_str)

    fields = {'voiceFile': '', 'voiceInfo.companyId': companyId, 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
              'voiceInfo.name': template__name, 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
              'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '1',
              'voiceInfo.tmpContent': template_Content, 'voiceInfo.tmpType': '0',
              'voiceInfo.tmpVoice': base64_str,
              'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'}
    audit_poweron_module(fields)

def test_addmudule_and_audit():
    '''
    全企业关机模板添加与审核
    :return:
    '''
    companyId = '147'
    template_Content = '关机'
    template__name = '关机'
    cookie = 'CA7CD79F0AD0EEED7FD265971DAEA4AE'
    params = {
        'speed': '50',
        'tempType': '1',
        'tmpContent': quote(template_Content)
    }
    headers = {
        'Cookie': f'JSESSIONID={cookie}',
    }
    r = upload_base64(params, headers)
    base64_str = r['object']
    print(base64_str)

    fields = {'voiceFile': '', 'voiceInfo.companyId': companyId, 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
              'voiceInfo.name': template__name, 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
              'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '2',
              'voiceInfo.tmpContent': template_Content, 'voiceInfo.tmpType': '0',
              'voiceInfo.tmpVoice': base64_str,
              'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'}
    audit_poweron_module(fields)

#审核关机模板接口
def test_file3():
    url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!add.action"
    m = MultipartEncoder(
        fields={'voiceFile': '', 'voiceInfo.companyId': '147', 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
                'voiceInfo.name': '关机', 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
                'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '2',
                'voiceInfo.tmpContent': '关机', 'voiceInfo.tmpType': '0',
                'voiceInfo.tmpVoice': 'IyFBTVIKBP8UM/Br/DX/oAAAIAROUedBaMXLtEduKb4ENCdXBSSwaPPjY82eBCMUYQQ7qOQwBRUuhgQ86ZcASD+dyp3wvUIEGqhswf96F+NdUtuwBEfoCQXFxJi+W06Z9ARnwRqv6/5D1UqErAAE1twereqfssyOS0MyBKB0Hq76336CJGIYfgSPYB5t1qaH8NkiGvgEsJceu/YrJqxQRl1QBKb0HpnbhzQLtSCsgASmLx6q24RkRDNAEI4Epj0elaxH0lriKypKBLDwICib4VRwcOggVAQ8yw9+gG2oeOyQkFoE3H/Q/Ic11LMJ0NxmBDHaHg/DEgiZrgUbKgRulRXr+oM7QaCUTKYErPIN6Op5y3KSbYjeBHHNIa34zF8zsMFJcgRIyiKt2Oi+LIQelYoEccoirdPukrarkIFuBEjNIq3jnoLOgk5vsgRx0iK+4+pSItkKCFAESM0brejaDq8W2U3yBEjKInm4Qb/aQ5BkfgRid3V4OADv0uZkIsQE56L/8AgML325AI4A',
                'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'})
    r = requests.post(url, data=m, headers={'Content-Type': m.content_type},verify=False)

#传文件分2种类型，一种是文件流file，一种是对文件编码后的字符串，平台上使用的字符串处理
#对于第一种，可通过post请求file参数传递文件对象，对于第2种，requests库本身不提供该功能，需要借助requests_toolbelt库来完成
#注意头信息content-type
def test_uploadfile():
    url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!add.action"
    files={'voiceFile': '', 'voiceInfo.companyId': '147', 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
            'voiceInfo.name': '开机', 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
            'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '1',
            'voiceInfo.tmpContent': '开机', 'voiceInfo.tmpType': '0',
            'voiceInfo.tmpVoice': 'IyFBTVIKBCsZN/CkyDn/wACCAARliVD0/+/xRf1vEJwEN+qE+/0t8htdRlvoBKVQlD7o46uJEf6UiAQ3KBuP+MibDkxou5IEkHgLX/rGUAaSISwWBACXEm+e22u71ATUCARbYBau5FPCdNgBLeIER98Wnf2xcoXYgpcABHH5FqzrgrZEIZK5FATUyxmt0czSGsxoBtYE5+Ys+DvIpsDgmRqCBFMjhjrnZrBzwTRiigRLcQ5cykhbW5knK14EFEeMzI2xg/6B5+aKBKvU+g/KQjtsbnHs4ARImhvemGPeiUUIvVwEcc0irLj3b6JJSIHkBEjKIq7D3kLosMMajgRx0iKr+J1/CsKgAdAESM0iivOd0qMoWLogBHHSKD3o5y8a0HSjPARIzSK+s4ITaT8CBfwEpvIiy4JlItQif4SABNNRXfMAEjmx1AGRog==',
            'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'}
    r = requests.post(url, headers={'Content-Type': 'multipart/form-data'},data=files,verify=False)

def test_time():
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # print(timestamp)
    # nonce = string.ascii_letters + string.digits
    # # random.choice(nonce)
    # l=[]
    # for i in range(32):
    #     s=random.choice(nonce)
    #     l.append(s)
    #     # print(nonce)
    # nonce=''.join(l)
    # print(nonce)
    # nonce=random.sample(string.ascii_letters + string.digits,random.randint(1,32))
    nonce=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,32)))
    print(nonce)

def test_aaa():
    data_to_sign = {
        'appkey': '989F23B783CBD649D25D',
        'method': 'push',
        'devicesn': 'f8_ms_double_0010',
        'message': '100',
        'push_template': '1',
    }
    a=sorted(data_to_sign.items(), key=lambda x: x[0], reverse=False)

    dict1={}
    # for k,v in a:
    #     dict1[k]=v
    print(type(a)),print(a)
    print(dict(a))
    # print(dict1)
    # a=urllib.parse.urlencode(dict1)
    # print(a)

data_1 = [
    {
        'user': 1,
        'pwd': 2
     },
    {
        'user': 3,
        'pwd': 4
    }
]
user=[(1,3),(2,4)]
pwd=[2,4]

@pytest.mark.parametrize('dic', data_1)
def test_parametrize_1(dic):
    print('\n测试数据为\n{}'.format(dic))

@pytest.mark.parametrize('user,pwd', user)
def test_parametrize_1(user,pwd):
    # print('\n测试数据为\n{}'.format(dic))
    print(user,pwd)

@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass

def test_aa():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b= {
        'z': 3,
        'x': 1,
        'y': 2,
    }
    print(a==b)
#各种结果比对方式（assert断言）：
#1.jsonschema: 不能包含任意代码，数据元素之间的关系上存在某些不能表达的约束。
# 因此，对于足够复杂的数据格式，任何 “验证工具” 都可能有两个验证阶段：一个在 schema (或结构)级别，一个在语义级别。
# 后一种检查可能需要使用更通用的编程语言来实现。
#2.jsonpath:适用于较少的字段验证
#3.diffy 新老版本的对比
#Diffy主要基于稳定版本和它的副本的输出，对候选版本的输出进行比较，以检查候选版本是否正确。
# 因此，Diffy首先假设候选版本应该和稳定版本有“相似”的输出。即不论候选版本和稳定版本系统模块是否相同，
# 他们的最终输出应该是“相似”的。这里一直使用“相似”，而不是使用相同，是因为相同请求可能会有一些Diffy不需要关心的干扰，比如：
#a.响应中包含服务器生成的时间戳；
#b.代码中使用了随机数；
#c.系统服务间有条件竞争。


import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
def test_redis():
    #加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
    print(r['name'])
    print(r.get('name'))  # 取出键name对应的值
    print(type(r.get('name')))

    r.hset("hash1", "k1", "v1")
    r.hset("hash1", "k2", "v2")
    print(r.hkeys("hash1"))  # 取hash中所有的key
    print(r.hget("hash1", "k1"))  # 单个取hash的key对应的值
    print(r.hmget("hash1", "k1", "k2"))  # 多个取hash的key对应的值
    r.hset("hash1", "k2", "v3")  # 只能新建
    print(r.hget("hash1", "k2"))
    device_sn="test_dev_0115"
    result=[102569]
    r.hset('deviceid', device_sn, str(result[0]))
    print(r.hget('deviceid', device_sn))

def test_ll():
    list1=[1,2]
    print(list1)
    list1.clear()
    print(list1)

#mock
import requests
from unittest import mock

def request_lemonfix():
    """

    :return:
    """
    res = requests.get('http://www.baidu1.com')
    return res.status_code.encode('utf-8')

def test_mock():
    request_lemonfix = mock.Mock(return_value="这里会显示论坛主页")
    print(request_lemonfix())
    print(type(request_lemonfix))

#接口diff
#接口Diff测试，简单来说就是比对相同接口在不同版本/不同环境下面的返回内容是否符合预期。
#对于日常迭代的接口来说，Diff测试是我们接口基本功能测试的有效补充，因为采用的是自动化的手段，
# 它可以利用线上大量的请求日志在新旧两个版本中进行回放，而我们手工/自动化的接口回归往往只局限于少量的测试数据，
# 很难覆盖到大量的、在生产环境真实会发生的异常请求数据。

#如果你曾有过大量的接口测试实践，相信对上面的说明会深有感触，单纯的依靠有限的CASE进行接口功能覆盖，上线后或多或少还是会发现一些异常。
def test_diff():
    from deepdiff import DeepDiff
    from pprint import pprint
    d1 = {"one": 1, "two": 2, "three": 3}
    d2 = {"one": 1, "three": 3, "two": 2}
    # t2 = {"one": 1, "three": "6","two": 4, }
    res = DeepDiff(d1, d2,ignore_order=False)
    print("============================")
    pprint(res.to_json())

    l1 = [1, 3, 1, 4]
    l2 = [4, 4, 1]
    #ignore_order忽略次序，TRUE为忽略，FALSE为不忽略
    #report_repetition 获得重复信息的数据,去重
    #ignore_order=True,report_repetition=True 这个参数对字典没用，因为无序
    ddiff = DeepDiff(l1, l2, ignore_order=True, report_repetition=False)
    pprint(ddiff)

    dict1 = {"1": 1, "2": 2, "3": 3, "2": 2}
    dict2 = {"2": 2, "3": 3, "2": 2, "4": 1}
    list1 = [1, 2, 3, 1]
    list2 = [1, 2, 3, 2]
    res = DeepDiff(dict1, dict2, ignore_order=True, report_repetition=True)
    res2 = DeepDiff(list1, list2, ignore_order=True, report_repetition=True)
    print(res)
    print(res2)

#测试用例失败重试rerun-failures插件
@pytest.mark.flaky(reruns=2,reruns_delay=2)
def test_rerun():
    a=1
    b=2
    # assert a==b
    try:
        assert a==b
    except Exception as  e:
        raise e

def test_mutiProcess():
    start_time=time.time()
    l=[]
    for i in range(1000000):
        l.append(i)
    end_time=time.time()
    result=end_time-start_time
    print("***************************")
    print(result)
    return l

#多进程运行
'''
并发和并行的区别：
https://www.cnblogs.com/f-ck-need-u/p/11161481.html
并行和串行：

串行：一次只能取得一个任务并执行这一个任务
并行：可以同时通过多进程/多线程的方式取得多个任务，并以多进程或多线程的方式同时执行这些任务
注意点：
如果是单进程/单线程的并行，那么效率比串行更差
如果只有单核cpu，多进程并行并没有提高效率
从任务队列上看，由于同时从队列中取得多个任务并执行，相当于将一个长任务队列变成了短队列
并发：

并发是一种现象：同时运行多个程序或多个任务需要被处理的现象
这些任务可能是并行执行的，也可能是串行执行的，和CPU核心数无关，是操作系统进程调度和CPU上下文切换达到的结果
解决大并发的一个思路是将大任务分解成多个小任务：
可能要使用一些数据结构来避免切分成多个小任务带来的问题
可以多进程/多线程并行的方式去执行这些小任务达到高效率
或者以单进程/单线程配合多路复用执行这些小任务来达到高效率
'''

'''
时间：2020-02-17 11:04:34
日志级别：INFO
ip: 182.168.3.111
认证邮箱： 110232123@qq.com
状态码： 1
客户端获取到的数据大小： 12931KB
'''
def test_regular():
    import re
    # pattern = r"0$|100$|[1-9]\d{0,1}$"
    # # 测试数据为0,3,27,100,123
    # result = re.match(pattern, "27")
    # result.group()
    timeregular=r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}'
    loglevelregular=r'[(.*)]'
    loglevelregular1=r'[INFO]'
    ipregular=r'(?P<first>\d{1,3}.){3}\d{1,3}'
    emailregular=r'\w+@\w+.\w+'
    statusregular=r'\d+'
    datasizeregular=r'\d+KB'
    #将各个字段的正则各自写成一个分组，分组之间填充其余元字符，把匹配整行日志的正则写出来如下,可以通过组号取数据了：
    reg=r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+([INFO])\s+.*:((\d{1,3}.){3}d{1,3}).*:(\w+@\w+.\w+)\D*(\d+)\D*(\d+)KB'
    s=  r'(\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\[(INFO)\]\s*.*:((\d{1,3}\.){3}\d{1,3}).*:(\w+@\w+\.\w+)\D*(\d+)\D*(\d+)KB'
    #对每个分组命名，正则如下
    regwithgroupname=r'(?P<Time>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(?P<LogLevel>[INFO])\s+.*:(?P<IP>(\d{1,3}.){3}d{1,3}).*:(?P<Email>\w+@\w+.\w+)\D*(?P<status>\d+)\D*(?P<data_size>\d+)KB'
    swithgroupname=r'(?P<Time>\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\[(?P<LogLevel>INFO)\]\s*.*:(?P<IP>(\d{1,3}\.){3}\d{1,3}).*:(?P<Email>\w+@\w+\.\w+)\D*(?P<status>\d+)\D*(?P<data_size>\d+)KB'

    text="2020-02-17 11:04:34 [INFO] 接收到来自IP: 182.168.3.111的访问，访问的认证方式为邮箱:110232123@qq.com，获取数据状态码1，获取数据12931KB"
    text1="192.168.1.163 数据"
    match_obj=re.search(ipregular,text1).groupdict()
    print("=================================")
    print(match_obj)
    #在字符串内查找模式匹配,只要找到第一个匹配然后返回
    print(re.search('com', 'www.runoob.com').span())

    #re.sub用于替换字符串中的匹配项。
    # 删除非数字(-)的字符串
    phone = "2004-959-559 # 这是一个国外电话号码"
    num = re.sub(r'\D', " ", phone)
    print("电话号码是 : ", num)

    #findall，在字符串中找到正则表达式所匹配的所有子串，并返回一个列表
    pattern = re.compile(r'\d+')  # 查找数字
    #返回值['123', '456']
    result1 = pattern.findall('runoob 123 google 456')
    print(result1)

    #split 方法按照能够匹配的子串将字符串分割后返回列表
    #返回 ['runoob', 'runoob', 'runoob', '']
    re.split('\W+', 'runoob, runoob, runoob.')


    #从头匹配一个符合规则的字符串
    m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    # 返回'Isaac Newton'，整个匹配串
    print(m.group(0))
    # 返回'Isaac',第一个括号分隔的子串
    print(m.group(1))
    #返回 ('Isaac', 'Newton')，返回一个包含所有匹配子群的元组
    print(m.groups())

    #返回一个字典，包含所有经命名的匹配子群，键值是子群名
    m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'myname@hackerrank.com')
    #返回 {'user': 'myname', 'website': 'hackerrank', 'extension': 'com'}
    print(m.groupdict())
    s = '1102231990xxxxxxxx'
    res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
    print(res.groupdict())


if __name__=="__main__":
    pytest.main(['-s','-m', 'test_mutiProcess','-n=2'])



