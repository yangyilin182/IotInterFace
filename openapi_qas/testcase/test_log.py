
import requests

class Testlog:
    def setup(self):
        pass

    def test_getApiDayHourStatisticsUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/log/getApiDayHourStatistics",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "date": 20181213, "days": 7, "endDate": 20181213, "interfaceMethod": "", "startDate": 20181213, "tokenId": "58f1bc232da8ae07c5a63e5e75d81e5b"
            },
            cookies={
            }
        )
        assert r.status_code == 200

    def test_getApiDayStatisticsUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/log/getApiDayStatistics",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "date": 20181213, "days": 7, "endDate": 20181213, "interfaceMethod": "", "startDate": 20181213, "tokenId": "58f1bc232da8ae07c5a63e5e75d81e5b"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getApiTodayHourStatisticsUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/log/getApiTodayHourStatistics",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "date": 20181213, "days": 7, "endDate": 20181213, "interfaceMethod": "", "startDate": 20181213, "tokenId": "58f1bc232da8ae07c5a63e5e75d81e5b"
            },
            cookies={
            }
        )
        assert r.status_code == 200