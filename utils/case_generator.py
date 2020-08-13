import json
import re
import os
import sys
from pprint import pprint
from requests import Session
import requests

#swagger version:2.0
from utils.Template import Template

'''
总结一下解包：
1.自动解包支持一切可迭代对象。eg:a, b, c = [1,2,3]   a,b,c = "abc"   a,b,c = (1,2,3)
2.python3中，支持更高级的解包操作，用星号操作使得等号左边的变量个数可以少于右边迭代对象中元素的个数。eg:a, b, *c = [1,2,3,4]
3.函数调用时，可以用 * 或者 ** 解包可迭代对象，作为参数传递
  eg:函数定义-->def func(a,b,c)，函数调用-->func(*[1,2,3]),func(*(1,2,3)),func(*"abc"),func(params, **params_params)
4.python3.5，函数调用和表达式中可支持更多的解包操作,可以使用任意多个解包操作（解包操作除了用在函数调用，还可以作用在表达式中）
  eg：{'x': 1, **{'y': 2}}， {*range(4), 4}， [*range(4), 4]， *range(4), 4
  eg:print(*[1], *[2], 3)
'''

'''
os.getcwd()、sys.path[0]、sys.argv[0]和__file__的区别：
总结一下：
1.os.getcwd() 指的是当前工作目录，绝对路径
2.sys.path[0] sys.path 指的是path，sys.path[0]为主模块所在目录的绝对路径，在模块运行的时候被自动添加进去
3.sys.argv[0] 就是你运行时 python 后面跟的参数
4.__file__ 表示所在模块文件的路径，和系统找到该模块的方式有关，你是用绝对路径去加载该模块，那么__file__就为绝对模块文件路径，
  如果你给系统提供相对路径去加载该模块，那么该文件路径为相对路径
'''

# 获取当前工作目录,也就是在哪个目录下运行这个程序
# workspace = os.getcwd()
# 获取当前所在模块绝对路径
# abspath=os.path.abspath(__file__)
# 切分当前所在模块绝对路径为目录+文件名
# filedir,filename=os.path.split(abspath)

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
#swagger网页首页
web_url= 'http://openapi.qas.uml-tech.com/doc.html'
#swagger_url可在访问swagger的首页控制台抓包获得api-docs
swagger_url='http://openapi.qas.uml-tech.com/v2/api-docs'

appId = '481960543d21419497bef8bd8d5715ba'
token = '58f1bc232da8ae07c5a63e5e75d81e5b'
def test_auto_gen_cases():
    #auto_gen_cases(swagger_url, project_name)
    """
    根据swagger返回的json数据自动生成yml测试用例模板
    :param swagger_url:
    :param project_name:
    :return:
    """
    project_name=r"\openapi_qas"
    res = Session().request('get', swagger_url).json()
    #提取接口url
    base_url="http://" + res.get("host")
    #提取api paths
    data = res.get('paths')
    #提取定义的变量字典, body参数
    definitions = res.get('definitions')
    # pprint(data)

    #获取当前工作目录,也就是在哪个目录下运行这个程序
    # workspace = os.getcwd()
    # 获取当前所在模块绝对路径
    # abspath=os.path.abspath(__file__)
    #切分当前所在模块绝对路径为目录+文件名
    # filedir,filename=os.path.split(abspath)

    #获取当前所在模块目录的父目录
    filepath=os.path.dirname(os.path.dirname(__file__))
    #拼接自动生成用例存放路径，没有就自动创建
    filepath = filepath + project_name + r'\testcase'
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    #遍历paths路径下的接口
    for k, v in data.items():
        pa_res = re.split(r'/+', k)
        #可将api路径的第一个部分作为一个模块名，即测试模块，例如：/echo/farm中，echo为模块，测试用例文件名可以为test_echo.py
        module_name, *file = pa_res[1:]
        filename = "test_" + module_name + '.py'
        filename = os.path.join(filepath, filename)

        #todo 思路：动态判断有什么参数，有什么就提取什么，最后组装到**kwargs中，在模板文件代码中，解包使用
        #TODO 模板文件中只写必填参数，可变参数通过**kwargs传递，可使用模板技术 pystache实现变量替换

        for _k, _v in v.items():
            method = _k
            api = k
            url = base_url + api
            caseName = _v.get('operationId')
            dict1 = {'method': method, 'api': api, 'caseName': caseName}
            print("method and api...为",dict1)
            parameters = _v.get('parameters')
            # print("----------------parameters",parameters)
            #kwargs 存储最终请求参数，只包括数据部分，不包括headers
            data = {}
            #存放api多个参数的列表
            api_param_list = []
            if not parameters:
                data={}
            else:
                for each in parameters:
                    #存放参数列表中的某一个字典对象参数，将来添加到参数列表
                    each_parameter={}
                    if each.get('in') == 'body':
                        schema = each.get('schema')
                        if schema:
                            ref = schema.get('$ref')
                            if ref:
                                param_key = ref.split('/',2)[-1]  # 这个uri拆分，根据实际情况来取第几个/反斜杠
                                #请求参数字典
                                param = definitions[param_key]['properties']
                                for key, value in param.items():
                                    #appid、token之类的动态输入，无需取example值
                                    if key in ['appId']:
                                        each_parameter[key] = appId
                                    elif key in ['token','tokenId']:
                                        each_parameter[key] = token
                                    elif value.__contains__('example'):
                                        each_parameter[key] = value['example']
                                    else:
                                        #todo 不存在example字段，暂时置为空字符串
                                        each_parameter[key] = ''

                        else:
                            pass
                        api_param_list.append(each_parameter)

                    elif each.get('in') == 'query':
                        #todo query 参数数据处理
                        pass

                    elif each.get('in') == 'formData':
                        #todo formData数据处理
                        pass

                    elif each.get('in') == 'header':
                        #todo head数据处理
                        pass

            #示例：发送请求
            # print("api_param_list",api_param_list)
            for each_param_api in api_param_list:
                data.update(each_param_api)
            print("关键字参数传递，----------------", data)


            # r=requests.request(method,url,json=kwargs).json()
            r= requests.request(method, url, json= data).json()
            print("执行结果,",r)

            #模板文件中字典类型存在{}符号，直接用字典数据替换模板文件存在一个问题：测试用例中多一对{}，需要处理下
            data= json.dumps(data)[1:-1]

            #空文件模板
            nullfile_template={
                "moduleName": module_name,
                "caseName": caseName,
                "method": method,
                "url": url,
                "json": data,
            }

            #非空文件模板
            notnullfile_template = {
                "caseName": caseName,
                "method": method,
                "url": url,
                "json": data,
            }
            # 利用模板技术，拼装测试用例部分
            # 待写入的测试用例内容
            testcase_code_null = Template.render("emptyfile_testcase_generator.mustache", nullfile_template)
            testcase_code_not_null = Template.render("notempty_testcase_generator.mustache", notnullfile_template)
            with open(filename,'a+',encoding='utf-8') as fp:
                filesize = os.path.getsize(filename)
                if filesize == 0:
                    fp.write(testcase_code_null)
                else:
                    fp.write(testcase_code_not_null)




