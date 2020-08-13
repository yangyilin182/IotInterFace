
import requests

class Testecho:
    def setup(self):
        pass

    def test_echoFarmServiceUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/echo/farm",
            params={
            },
            json={
            },
            cookies={
            }
        )
        assert r.status_code == 200

    def test_echoLogServiceUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/echo/log",
            params={
            },
            json={
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_echoNeServiceUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/echo/ne",
            params={
            },
            json={
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_echoTokenServiceUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/echo/token",
            params={
            },
            json={
            },
            cookies={
            }
        )
        assert r.status_code == 200