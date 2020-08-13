
import requests

class Testfarm:
    def setup(self):
        pass

    def test_getCoodinateFlagUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getCoodinateFlag",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "date": "2019-08-05", "dids": "NJHYBVHAS0000149", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "type": "day", "vins": "NJHYBVHAS0000149"
            },
            cookies={
            }
        )
        assert r.status_code == 200

    def test_getHistoryCanInfoUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getHistoryCanInfo",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "did": "homer 1810000304", "filterIfMissing": "", "gpsEndTime": 20181213235959, "gpsStartTime": 20181213000000, "pageSize": 10, "pageType": "", "requestColumns": "2602,2603", "reversed": False, "showColumns": "2602,2603", "startRowkey": "", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vin": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getHistoryGateWayInfoUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getHistoryGateWayInfo",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "did": "homer 1810000304", "filterIfMissing": "", "gpsEndTime": 20181213235959, "gpsStartTime": 20181213000000, "pageSize": 10, "pageType": "", "requestColumns": "2602,2603", "reversed": False, "showColumns": "2602,2603", "startRowkey": "", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vin": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getHistoryGpsInfoUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getHistoryGpsInfo",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "did": "homer 1810000304", "gpsEndTime": 20181213000000, "gpsStartTime": 20181213000000, "pageSize": 10, "pageType": 1, "reversed": "", "startRowkey": "", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vin": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getHistoryWorkInfoUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getHistoryWorkInfo",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "did": "homer 1810000304", "filterIfMissing": "", "gpsEndTime": 20181213235959, "gpsStartTime": 20181213000000, "pageSize": 10, "pageType": "", "requestColumns": "2602,2603", "reversed": False, "showColumns": "2602,2603", "startRowkey": "", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vin": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getImagesUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getImages",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "did": "homer 1810000304", "gpsEndTime": 20181213000000, "gpsStartTime": 20181213000000, "pageSize": 10, "reversed": False, "startRowkey": "", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vin": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getLastWorkInfoUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getLastWorkInfo",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "NJHYBVHAS0000149", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "NJHYBVHAS0000149"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getLocationUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getLocation",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getOnlineUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getOnline",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "onlineOffset": -5, "today": True, "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getRealTimeUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getRealTime",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "NJHYBVHAS0000149", "showColums": "GPSLat,GPSLon", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "NJHYBVHAS0000149"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getStatisticsUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getStatistics",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "day": 20181213, "dids": "NJHYBVHAS0000149", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "type": "day", "vins": "NJHYBVHAS0000149"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getTotalMileageUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getTotalMileage",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "NJHYBVHAS0000149", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "NJHYBVHAS0000149"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getVehicleInfoUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/getVehicleInfo",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "groupType": 1, "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_testUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/farm/test",
            params={
            },
            json={
            },
            cookies={
            }
        )
        assert r.status_code == 200