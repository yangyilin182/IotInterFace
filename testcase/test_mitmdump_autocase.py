
import requests



class TestHttp:
    def setup(self):
        pass

    def test_api_list_create_doc(self):
        r=requests.request(
            'POST',
            url='https://mubu.com/api/list/create_doc',
            params={
            },
            data={
                    "folderId": "0", "type": "0"
            },
            cookies={
                    "data_unique_id": "2ffd4eb4-62fe-4458-a1f9-15fd5ac6deee", "csrf_token": "284940f3-0a15-4591-b235-e9b9772c3cd7", "language": "en-US", "country": "US", "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1597138431", "_ga": "GA1.2.1252126428.1597138431", "_gid": "GA1.2.1969615226.1597138431", "reg_from": "https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DWcgt1WP-zRnyIEMT7ZaOyTYh0etdleuOaVuFElYv7OS%26wd%3D%26eqid%3Dddca6cf60006df43000000035f3265f6", "reg_entrance": "https%3A%2F%2Fmubu.com%2F", "s_v_web_id": "kdpr06sr_JELtNP7H_kPEP_4pvh_AADv_0MEDtkAMXpjs", "mubu_inner": "1", "SESSION": "78962f0c-cec9-40f5-80c5-d9a3c3dad3fc", "reg_prepareId": "173dce11890-173dce11605-406f-80a8-457c9ddd655a", "reg_focusId": "865eb708-a221-406f-80a8-173dce1323e", "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiNTYxNzEzMyIsImV4cCI6MTU5OTczMDYzMCwiaWF0IjoxNTk3MTM4NjMwfQ.IbEiLgEG6dUIu7ebvw5LZD6Ib66n616DOzM11Ag72ENw8ysWfi4nF10wwsiqIQWyPypz2Cl5WJ65vbBNGqacCw", "_gat": "1", "SLARDAR_WEB_ID": "a7d60483-a966-4fa7-b863-6de9adeb7537", "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1597139879"
            },
            verify =False
        )
        assert r.status_code == 200

    # def test_slardar_main_(self):
    #     r=requests.request(
    #         'GET',
    #         url='https://i.snssdk.com/log/sentry/v2/api/slardar/main/',
    #         params={
    #                 "ev_type": "ajax", "ax_status": "200", "ax_type": "post", "ax_request_header": "Content-Type: application/x-www-form-urlencoded; charset=UTF-8\r\nAccept: application/json, text/javascript, */*; q=0.01\r\nX-Requested-With: XMLHttpRequest", "ax_duration": "331", "ax_size": "49", "ax_response_header": "date: Tue, 11 Aug 2020 09:58:49 GMT\r\nvia: cache9.l2et15-1[83,0], cache11.cn763[114,0]\r\nx-tt-trace-tag: id=03;cdn-cache=miss;type=dyn\r\nserver: Tengine\r\ncontent-type: application/json;charset=UTF-8\r\nstatus: 200\r\nx-tt-trace-host: 016b4788cd88b1a2fb40ffa6714802d96e9c7ffb44510b6d782507db2affb6bcb421bffc004da8e8e4d810f554b9470d7c301ddb034be4da263c5e9f79af23e7e0515c287f035938f4919735329b0f41af\r\nserver-timing: inner; dur=28, cdn-cache;desc=MISS,edge;dur=31,origin;dur=83\r\ntiming-allow-origin: *\r\neagleid: 7cc8711f15971399295394935e\r\nx-application-context: ee.mubu.web_server:prod:9274\r\nx-tt-timestamp: 1597139929.625\r\n", "ax_protocol": "https", "ax_domain": "mubu.com", "ax_path": "/api/list/create_doc", "ax_url": "https://mubu.com/api/list/create_doc", "version": "2.1.21", "hostname": "mubu.com", "protocol": "https", "url": "https://mubu.com/list", "slardar_session_id": "7cd0ce21-0714-4090-8d14-baf7f6e3539c", "sample_rate": "1", "pid": "/list", "report_domain": "i.snssdk.com", "screen_resolution": "1920x1080", "network_type": "4g", "bid": "mubu_biz_monitor", "context": "{}", "slardar_web_id": "a7d60483-a966-4fa7-b863-6de9adeb7537", "timestamp": "1597139929290"
    #         },
    #         data={
    #         },
    #         cookies={
    #         },
    #         verify =False
    #     )
    #     assert r.status_code == 200

    def test__slardar_sdk_setting(self):
        r=requests.request(
            'GET',
            url='https://i.snssdk.com/slardar/sdk_setting',
            params={
                    "bid": "mubu_web"
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200

    def test_api_document_get(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/document/get',
            params={
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200

    def test_api_user_current_level(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/user/current_level',
            params={
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200

    def test_api_user_current_user(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/user/current_user',
            params={
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200



    def test_api_user_get_invite_count(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/user/get_invite_count',
            params={
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200

    def test_api_colla_register(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/colla/register',
            params={
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200

    def test_api_user_get_user_params(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/user/get_user_params',
            params={
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200


    def test_api_colla_members(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/colla/members',
            params={
                    "memberId": "8454148708517476", "documentId": "7lI4_WYKf2J"
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200

    # def test_slardar_batch_(self):
    #     r=requests.request(
    #         'POST',
    #         url='https://i.snssdk.com/log/sentry/v2/api/slardar/batch/',
    #         params={
    #         },
    #         data={
    #         },
    #         cookies={
    #                 "SLARDAR_WEB_ID": "a911735b-4add-4b7f-b2bf-542d1e7c9a26"
    #         },
    #         verify =False
    #     )
    #     assert r.status_code == 200


    def test_api_colla_message(self):
        r=requests.request(
            'OPTIONS',
            url='https://api2.mubu.com/v3/api/colla/message',
            params={
            },
            data={
            },
            cookies={
            },
            verify =False
        )
        assert r.status_code == 200

RequestsCookieJar()
