import string
import time
import random
from unittest import mock

import pytest

from api.BaseApi import BaseApi
from api.PushApi import PushApi
from utils.YamlUtil import yml
from utils.JsonPath import JsonPath

class Test_push_api:
    @classmethod
    def setup_class(cls):
        cls.push_api = PushApi()

    # s = yml.load_yaml('1.yml')
    '''
    message = []
    for i in range(10):
        # message.append(str(random.randint(0,100000)))
        random_list=random.sample(string.digits,random.randint(0,9))
        random_str=''.join(random_list)
        print("===============================",random_str)
        message.append(random_str)
    '''

    #参数化方案一 @pytest.mark.parametrize
    # @pytest.mark.parametrize("message",yml.load_yaml('1.yml')['message'])
    '''
    @pytest.mark.parametrize("message",message)
    @pytest.mark.parametrize("push_template",yml.load_yaml('1.yml')['push_template'])
    # @pytest.mark.parametrize("message,push_template",[('100','1'),("101","2"),("102","3")])
    def test_push(self,message,push_template):
        self.push_api.push(message,push_template)
        time.sleep(7)
    '''
    #参数化方案二 @pytest.fixture
    # 字典类型 datautil=[{"message":"100","push_template":"1"},{"message":"101","push_template":"2"}]
    # @pytest.fixture(params=[("100","1"),("101","2")])
    # def data_set(self,request):
    #     return request.param

    #@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)]) 标记跳过执行测试用例
    #参数request固定，不可更改，经验证，是个pytest的fixture
    #fixture优点1：可根据是否需要定制化的添加类似setup功能
    #优点2：可跨类或者跨模块使用（在conftest文件实现）
    def test_push(self, push_data):
        r=self.push_api.push(push_data[0], push_data[1])
        time.sleep(7)
        expr = '$..code'
        assert JsonPath.jsonpath(r, expr)[0] == 0
        # assert r['code'] == 0
        assert r['msg'] == '推送成功'

    #mock试验（requests.post）,测试用例中含有fixture参数，先从下到上传递mock参数对象，最后传递fixture参数
    #eg:test_mock_push(self,mock_push,push_data)
    # @mock.patch("requests.post")
    def test_mock_push(self,push_data):
        #为mock对象赋值，调用mock对象返回该结果
        # mock_push.return_value={'msg':'设备离线','code':'1009'}
        r = self.push_api.push(push_data[0], push_data[1])
        time.sleep(7)
        expr = '$..code'
        assert JsonPath.jsonpath(r, expr)[0] == 0
        # assert r['code'] == 0
        assert r['msg'] == '推送成功'


    def test_pushByPaycode(self):
        pass

    def test_pushbypaycodediscount(self):
        pass

    def test_pushverifycode(self):
        pass

    def test_pushverifycodebypaycode(self):
        pass

    def test_refreshQr(self):
        pass

    def test_syncOrder(self):
        pass

    def test_bindDevice(self):
        pass

    def test_unbindDevice(self):
        pass

    def test_pushTTS(self):
        pass

    def test_pushTTSByPayCode(self):
        pass