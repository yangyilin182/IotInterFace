
import requests

class Testne:
    def setup(self):
        pass

    def test_getAlarmDetailUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/getAlarmDetail",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "thresholdTime": 10, "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200

    def test_getCanUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/getCan",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dataType": "REALTIME", "did": "BYN1010160900116", "gb": False, "gpsEndTime": 20181227235959, "gpsStartTime": 20181227000000, "httpShowColumns": "2602,2603", "interfaceName": "", "pageSize": 10, "pageType": "", "prefix": "SUBMIT", "reverse": False, "startRowKey": "", "statusCode": "", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vin": "053821611224372"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getGatewayLogsUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/getGatewayLogs",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dataType": "REALTIME", "did": "BYN1010160900116", "gb": False, "gpsEndTime": 20181227235959, "gpsStartTime": 20181227000000, "httpShowColumns": "2602,2603", "interfaceName": "", "pageSize": 10, "pageType": "", "prefix": "SUBMIT", "reverse": False, "startRowKey": "", "statusCode": "", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vin": "053821611224372"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getLocationUsingPOST_1(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/getLocation",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getRealTimeUsingPOST_1(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/getRealTime",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "NJHYBVHAS0000149", "showColums": "GPSLat,GPSLon", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "NJHYBVHAS0000149"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getTotalMileageUsingPOST_1(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/getTotalMileage",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "NJHYBVHAS0000149", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "NJHYBVHAS0000149"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_getVehicleInfoUsingPOST_1(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/getVehicleInfo",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "groupType": 1, "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_lockUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/lock",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200
    def test_unlockUsingPOST(self):
        r=requests.request(
            "post",
            url="http://openapi.qas.uml-tech.com/ne/unlock",
            params={
            },
            json={
                    "appId": "481960543d21419497bef8bd8d5715ba", "dids": "homer 1810000304", "token": "58f1bc232da8ae07c5a63e5e75d81e5b", "vins": "homer 1810000304"
            },
            cookies={
            }
        )
        assert r.status_code == 200