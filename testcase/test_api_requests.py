from api.ApiRequests import ApiRequest

def test_api(self):
    req = ApiRequest()
    req_data = {
        "schema": "http",
        "encoding": "base64",
        "method": "get",
        "url": "http://docker.testing-studio.com:10000/topics_encode.txt",
        "headers": None

    }
    j = req.send(req_data)
    assert len(j["topics"]) == 2

    req_data = {
        "schema": "http",
        "encoding": "",
        "method": "get",
        "url": "http://docker.testing-studio.com:10000/topics.txt",
        "headers": None

    }
    j = req.send(req_data)
    assert len(j["topics"]) == 2