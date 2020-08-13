import json
import re
import os

from requests import Session
from utils.Template import Template

#  swagger version:2.0

class CaseGenerate:

    @classmethod
    def auto_gen_cases(cls, swagger_url, project_name, appId, token):
        """
        根据swagger返回的json数据自动生成pytest测试用例模板
        :param swagger_url:
        :param project_name:
        :return:
        """
        res = Session().request('get', swagger_url).json()
        # 提取接口base_url
        base_url = "http://" + res.get("host")
        # 提取api paths
        data = res.get('paths')
        # 提取定义的变量字典, body参数
        definitions = res.get('definitions')

        filepath = cls._create_casefile(project_name)
        # # 获取当前所在模块目录的父目录
        # filepath = os.path.dirname(os.path.dirname(__file__))
        # # 拼接自动生成用例存放路径，没有就自动创建
        # filepath = filepath + '\\' + project_name + r'\testcase'
        # if not os.path.exists(filepath):
        #     os.makedirs(filepath)

        # 遍历paths路径下的接口
        for k, v in data.items():
            pa_res = re.split(r'/+', k)
            # 可将api路径的第一个部分作为一个模块名，即测试模块，例如：/echo/farm中，echo为模块，测试用例文件名可以为test_echo.py
            module_name, *file = pa_res[1:]
            filename = "test_" + module_name + '.py'
            filename = os.path.join(filepath, filename)

            # todo 思路：动态判断有什么参数，有什么就提取什么，最后组装到**kwargs中，在模板文件代码中，解包使用
            #  模板文件中只写必填参数，可变参数通过**kwargs传递

            for _k, _v in v.items():
                method = _k
                api = k
                url = base_url + api
                caseName = _v.get('operationId')
                dict1 = {'method': method, 'api': api, 'caseName': caseName}
                print("method and api...为", dict1)
                parameters = _v.get('parameters')
                # print("----------------parameters",parameters)
                # kwargs 存储最终请求参数，只包括数据部分，不包括headers
                data = {}
                # 存放api多个dict结构参数的列表
                api_param_list = []
                if not parameters:
                    data = {}
                else:
                    cls._traverse_parameters(parameters, definitions, api_param_list, appId, token)

                for each_param_api in api_param_list:
                    data.update(each_param_api)
                print("json参数传递，----------------", data)

                # 将从swagger中提取出来的dict请求参数数据进行处理,便于后续传递给模板文件进行渲染
                data=cls._data_handle(data)
                # 为模板文件构造dict结构数据
                filedata_to_template = {
                    "moduleName": module_name,
                    "caseName": caseName,
                    "method": method,
                    "url": url,
                    "json": data,
                }
                # 待写入的测试用例内容
                testcase_code_newfile, testcase_code_not_newfile = cls._template_to_code(filedata_to_template)
                # 将测试用例写入py文件
                cls._write_casefile(filename, testcase_code_newfile, testcase_code_not_newfile)

    # 遍历文档中的parameters参数中参数，提取参数
    @classmethod
    def _traverse_parameters(cls, parameters, definitions: dict, api_param_list, appId, token):
        for each in parameters:
            # 存放参数列表中的某一个字典对象参数，将来添加到参数列表
            each_parameter = {}
            if each.get('in') == 'body':
                schema = each.get('schema')
                if schema:
                    ref = schema.get('$ref')
                    if ref:
                        param_key = ref.split('/', 2)[-1]  # 这个uri拆分，根据实际情况来取第几个/反斜杠
                        # 请求参数字典
                        param = definitions[param_key]['properties']
                        for key, value in param.items():
                            # appid、token之类的动态输入，无需取example值
                            if key in ['appId']:
                                each_parameter[key] = appId
                            elif key in ['token', 'tokenId']:
                                each_parameter[key] = token
                            elif value.__contains__('example'):
                                each_parameter[key] = value['example']
                            else:
                                # todo 不存在example字段，暂时置为空字符串
                                each_parameter[key] = ''


                else:
                    pass
                api_param_list.append(each_parameter)

            elif each.get('in') == 'query':
                # todo query 参数数据处理
                pass

            elif each.get('in') == 'formData':
                # todo formData数据处理
                pass

            elif each.get('in') == 'header':
                # todo head数据处理
                pass

    # 将模板文件转化为代码内容
    @classmethod
    def _template_to_code(cls, filedata_to_template):

        # 获取模板文件父目录
        filepath_to_template = os.path.join(os.path.dirname(os.path.dirname(__file__)),'templates')
        # 使用pystache模板技术，拼装测试用例
        testcase_code_to_emptyfile = Template.render(
            os.path.join(filepath_to_template, "emptyfile_testcase_generator.mustache"), filedata_to_template)

        testcase_code_to_notemptyfile = Template.render(
            os.path.join(filepath_to_template, "notempty_testcase_generator.mustache"), filedata_to_template)
        return testcase_code_to_emptyfile, testcase_code_to_notemptyfile

    # 将测试用例内容写入Python文件
    @staticmethod
    def _write_casefile(filename, testcase_code_to_emptyfile, testcase_code_to_notemptyfile):
        with open(filename, 'a+', encoding='utf-8') as fp:
            filesize = os.path.getsize(filename)
            if filesize == 0:
                fp.write(testcase_code_to_emptyfile)
            else:
                fp.write(testcase_code_to_notemptyfile)

    #将从swagger中提取出来的dict请求参数数据进行处理,便于后续传递给模板文件进行渲染
    @classmethod
    def _data_handle(cls,data):
        # 模板文件中字典类型存在{}符号，直接用字典数据替换模板文件存在一个问题：测试用例中多一对{}，需要处理下
        data = json.dumps(data)[1:-1]
        # 因为Python类型转为json后数据类型的变化，bool类型需要处理
        if 'false' in data:
            data = re.sub('false', 'False', data)
        if 'true' in data:
            data = re.sub('true', 'True', data)
        return data

    #创建测试用例目录
    @classmethod
    def _create_casefile(cls,project_name):
        # 获取当前所在模块目录的父目录
        filepath = os.path.dirname(os.path.dirname(__file__))
        # 拼接自动生成用例存放路径，没有就自动创建
        filepath = filepath + '\\' + project_name + r'\testcase'
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        return filepath

