import json
from pprint import pprint

import requests
import yaml


class TestHttp:
    def setup(self):
        pass

    def test_request(self):
        r=requests.request(
            "get",
            url="https://testerhome.com/hogwarts",
            params={
            },
            cookies={
            }
        )
        assert r.status_code == 200
