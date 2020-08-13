from unittest import mock
import unittest
from api import temple

class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''
    def test_01(self):
        '''测试支付成功场景'''
        # mock一个支付成功的数据
        temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    def test_02(self):
        '''测试支付失败场景'''
        # mock一个支付成功的数据
        temple.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues, "支付失败")


#用mock.patch实现
class Test_zhifu_statues_withpatch(unittest.TestCase):
    '''单元测试用例'''
    #面向过程的代码（要mock的对象为函数）
    # patch 的用法:它是一个装饰器，需要把你想模拟的函数写在里面，然后在后面的单元测试案例中为它赋一个具体实例，
    # 再用 return_value 来指定模拟的这个函数希望返回的结果就可以了，后面就是正常单元测试代码
    # 如果 patch 多个外部函数，那么调用遵循自下而上的规则，比如：
    '''
    @mock.patch("function_C")
    @mock.patch("function_B")
    @mock.patch("function_A")
    def test_check_cmd_response(self, mock_function_A, mock_function_B, mock_function_C):
        mock_function_A.return_value = "Function A return"
        mock_function_B.return_value = "Function B return"
        mock_function_C.return_value = "Function C return"
    
        self.assertTrue(re.search("A", mock_function_A()))
        self.assertTrue(re.search("B", mock_function_B()))
        self.assertTrue(re.search("C", mock_function_C()))
    '''
    @mock.patch("api.temple.zhifu")
    def test_01(self, mock_zhifu):
        '''测试支付成功场景'''
        # 方法一：mock一个支付成功的数据
        # temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})

        # 方法二：mock.path装饰器模拟返回结果
        mock_zhifu.return_value = {"result": "success", "reason":"null"}
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    @mock.patch("api.temple.zhifu")
    def test_02(self, mock_zhifu):
        '''测试支付失败场景'''
        # mock一个支付成功的数据

        mock_zhifu.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues, "支付失败")

# 面向对象代码风格 使用path.object进行mock
#面向对象的 mock 和面向过程的很相似，唯一就是把 mock.patch 替换成 mock.patch.object ，并且在里面列出类实例和方法名。
# 仔细观察，是类的实例 (不是字符串) 和方法名 (是字符串的方法名而不是方法对象)

# linux_tool.py
import re

class LinuxTool(object):
    def __init__(self):
        pass

    def send_shell_cmd(self):
        return "Response from send_shell_cmd function"

    def check_cmd_response(self):
        response = self.send_shell_cmd()
        print("response: {}".format(response))
        return re.search(r"mock_send_shell_cmd", response)

from unittest import TestCase, mock
# from linux_tool import LinuxTool

class TestLinuxTool(TestCase):
    def setUp(self):
        self.linux_tool = LinuxTool()

    def tearDown(self):
        pass

    @mock.patch.object(LinuxTool, "send_shell_cmd")
    def test_check_cmd_response(self, mock_send_shell_cmd):
        # mock_send_shell_cmd.return_value = "Response from emulated mock_send_shell_cmd function"
        #side_effect用法: 这个参数指向一个可调用对象，一般就是函数。当mock对象被调用时，
        # 如果该函数返回值不是DEFAULT时，那么以该函数的返回值作为mock对象调用的返回值。
        # mock_send_shell_cmd.side_effect=[
        #     "mock_send_shell_cmd function1",
        #     "mock_send_shell_cmd function2",
        #     "mock_send_shell_cmd function3",
        #     "Response from emulated mock_send_shell_cmd function4",
        #     "Response from emulated mock_send_shell_cmd function5"
        # ]
        #模拟异常，所有 raise 语句可以引发的异常都可以用 side_effect 引发
        mock_send_shell_cmd.side_effect = Exception("Raise Exception")
        status = self.linux_tool.check_cmd_response()
        print("check result: %s" % status)
        self.assertTrue(status)



if __name__ == "__main__":
    unittest.main()