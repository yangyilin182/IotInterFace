import re
import os
import sys
import requests
from requests import Session
from pprint import  pprint

template ="""
args:
  - {method}
  - {api}
kwargs:
  -
    caseName: {caseName}
    {data_or_params}:
        {data}
validator:
  -
    json:
      successed: True
"""

'''
总结一下解包：
1.自动解包支持一切可迭代对象。eg:a, b, c = [1,2,3]   a,b,c = "abc"   a,b,c = (1,2,3)
2.python3中，支持更高级的解包操作，用星号操作使得等号左边的变量个数可以少于右边迭代对象中元素的个数。eg:a, b, *c = [1,2,3,4]
3.函数调用时，可以用 * 或者 ** 解包可迭代对象，作为参数传递
  eg:函数定义-->def func(a,b,c)，函数调用-->func(*[1,2,3]),func(*(1,2,3)),func(*"abc")
4.python3.5，函数调用和表达式中可支持更多的解包操作,可以使用任意多个解包操作（解包操作除了用在函数调用，还可以作用在表达式中）
  eg：{'x': 1, **{'y': 2}}， {*range(4), 4}， [*range(4), 4]， *range(4), 4
  eg:print(*[1], *[2], 3)
'''
#swagger网页首页
web_url= 'http://openapi.qas.uml-tech.com/doc.html'
#swagger_url可在访问swagger的首页控制台抓包获得api-docs
swagger_url= 'http://openapi.qas.uml-tech.com/v2/api-docs'
def test_auto_gen_cases():
    '''
    auto_gen_cases(swagger_url, project_name)
    '''
    """
    根据swagger返回的json数据自动生成yml测试用例模板
    :param swagger_url:
    :param project_name:
    :return:
    """
    # res=requests.get(swagger_url).json()
    res = Session().request('get', swagger_url).json()
    # pprint(res['paths'])
    data = res.get('paths')
    pprint(data)
    # workspace = os.getcwd()
    #
    # project_ = os.path.join(workspace, project_name)
    #
    # if not os.path.exists(project_):
    #     os.mkdir(project_)
    #
    # for k, v in data.items():
    #     pa_res = re.split(r'[/]+', k)
    #     dir, *file = pa_res[1:]
    #
    #     if file:
    #         file = ''.join([x.title() for x in file])
    #     else:
    #         file = dir
    #
    #     file += '.yml'
    #
    #     dirs = os.path.join(project_, dir)
    #
    #     if not os.path.exists(dirs):
    #         os.mkdir(dirs)
    #
    #     os.chdir(dirs)
    #
    #     if len(v) > 1:
    #         v = {'post': v.get('post')}
    #     for _k, _v in v.items():
    #         method = _k
    #         api = k
    #         caseName = _v.get('description')
    #         data_or_params = 'params' if method == 'get' else 'data'
    #         parameters = _v.get('parameters')
    #
    #         data_s = ''
    #         try:
    #             for each in parameters:
    #                 data_s += each.get('name')
    #                 data_s += ': \n'
    #                 data_s += ' ' * 8
    #         except TypeError:
    #             data_s += '{}'
    #
    #     file_ = os.path.join(dirs, file)
    #
    #     with open(file_, 'w', encoding='utf-8') as fw:
    #         fw.write(template.format(
    #             method=method,
    #             api=api,
    #             caseName=caseName,
    #             data_or_params=data_or_params,
    #             data=data_s
    #         ))
    #
    #     os.chdir(project_)