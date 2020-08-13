import requests


class Payment:
    """
    定义第三方支付类
    """
    def authe(self, card_num, amount):
        """
        请求第三方支付接口，并返回响应码
        :param card_num: 卡号
        :param amount: 金额
        :return: 返回状态码200 代表支付成功，500 代表支付异常
        """
        url = "https://www.dd.com"  # 第三方的url
        data = {"card_num": card_num, "amount": amount}
        response = requests.post(url, data=data)
        return response.status_code

    def pay(self, user_id, card_num, amount):
        """
        支付
        :param user_id: 用户id
        :param card_num: 卡号
        :param amount: 金额
        :return:
        """
        try:
            status_code = self.authe(card_num, amount)
        except TimeoutError:
            status_code = self.authe(card_num, amount)

        if status_code == 200:
            print("支付成功")
            return "success"
        if status_code == 500:
            print("支付失败")
            return "fail"