import unittest
from api.MockStudy import Payment
from unittest import mock


class TestPayment(unittest.TestCase):
    """
    测试支付接口
    """

    def setUp(self):
        self.payment = Payment()

    def test_success(self):
        """
        测试支付成功
        :return:
        """
        self.payment.authe = mock.Mock(return_value=200)
        res = self.payment.pay(user_id=10001, card_num="123444", amount=1000)
        self.assertEqual("success", res)

    def test_fail(self):
        """
        测试支付成功
        :return:
        """
        self.payment.authe = mock.Mock(return_value=500)
        res = self.payment.pay(user_id=10002, card_num="1233444", amount=1000)
        self.assertEqual("fail", res)

    def test_retry_success(self):
        """
                测试支付失败重试在成功
                side_effect 可以为序列类型 异常类型，对象
                如果为序列类型 每次调用mock对象，会依次将side effcet中的元素返回
                :return:
                """
        self.payment.authe = mock.Mock(side_effect=[500,200])
        print(self.payment.authe(card_num="1233444", amount=1000))
        res = self.payment.pay(user_id=10003, card_num="1234444", amount=1000)
        self.assertEqual("success", res)


if __name__ == '__main__':
    unittest.main()