import os
import sys
import json
import re
from mitmproxy import http
from mitmproxy import ctx
#导包之前先将项目目录添加到环境变量

project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)

from utils.Template import Template


def write_casefile(filename, testcase_code_to_emptyfile, testcase_code_to_notemptyfile):
    with open(filename, 'a+', encoding='utf-8') as fp:
        filesize = os.path.getsize(filename)
        if filesize == 0:
            fp.write(testcase_code_to_emptyfile)
        else:
            fp.write(testcase_code_to_notemptyfile)


def data_handle(data):
    # 模板文件中字典类型存在{}符号，直接用字典数据替换模板文件存在一个问题：测试用例中多一对{}，需要处理下
    data = json.dumps(data)[1:-1]
    # 因为Python类型转为json后数据类型的变化，bool类型需要处理
    if 'false' in data:
        data = re.sub('false', 'False', data)
    if 'true' in data:
        data = re.sub('true', 'True', data)
    return data

def get_filename():
    # 获取当前所在模块目录的父目录(项目目录)
    filepath = os.path.dirname(os.path.dirname(__file__))
    # 拼接自动生成用例存放路径，没有就自动创建
    filepath = filepath + '\\' + r'\testcase'
    filename = os.path.join(filepath, "test_mitmdump_autocase.py")
    return filename

def request(flow: http.HTTPFlow):

    data_to_render = {}
    #过滤需要自动生成用例的host,排除无关host
    #https://mubu.com/list
    if flow.request.host in ['iotoperation-testing.cloudentify.com']:
    # if flow.request.host in ['mubu.com','mcs.snssdk.com','i.snssdk.com','api2.mubu.com']:
        path = flow.request.path
        #判断path中是否含有参数，如果有，先去除参数部分
        if '?' in path:
            path = path.split('?')[0]
        path = re.split('[/.!-]', path)
        caseName = path[-3] + '_' + path[-2] + '_' + path[-1]

        method = flow.request.method
        # info = ctx.log.info
        # info("=================url>>"+ flow.request.pretty_url)
        url = flow.request.pretty_url.split('?')[0]

        data={}
        for k,v in flow.request.urlencoded_form.fields:
            data[k]=v
        data= data_handle(data)

        params={}
        for k, v in flow.request.query.fields:
            params[k]=v
        params=data_handle(params)

        cookies={}
        for k, v in flow.request.cookies.fields:
            cookies[k]=v
        cookies=data_handle(cookies)

        # 当我们输出某个实例化对象时，其调用的就是该对象的 __repr__() 方法，输出的是该方法的返回值。
        # 执行 print(clangs) 等同于执行 print(clangs.__repr_)
        data_to_render["caseName"]= caseName
        data_to_render["method"] = method.__repr__()
        data_to_render["url"] = url.__repr__()
        data_to_render["params"] = params
        data_to_render["cookies"] = cookies
        data_to_render["data"] = data

        #过滤静态资源请求
        if  path[-1] in ['gif','png','jpg','css','ico','js']:
            data_to_render= None

        #处理非静态资源接口，渲染模板并写用例文件
        if data_to_render:
            filepath_to_template = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')

            testcase_code_to_emptyfile = Template.render(
                os.path.join(filepath_to_template, "emptyfile_testcase_by_mitm.mustache"), data_to_render)

            testcase_code_to_notemptyfile = Template.render(
                os.path.join(filepath_to_template, "notempty_testcase_by_mitm.mustache"), data_to_render)

            write_casefile(get_filename(), testcase_code_to_emptyfile, testcase_code_to_notemptyfile)
