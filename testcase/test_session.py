import requests
def test_session():
    session = requests.session()
    url="http://www.baidu.com"
    res = session.post(url = url)
    print (res.text)
    print (session.cookies)

def test_session1():

    url = "http://?????.com/SvltLogin"
    s = requests.session()  # 建立一个Session
    response = s.post(url, data={"txtUsr_id": "00000001", "txtPassword": "mima"})  # session登录网站
    response = s.get("http://?????.com/SvltLogout")  # session浏览页面
    response.encoding = "GBK"
    print(response.text)

