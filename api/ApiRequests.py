import base64
import json

import requests

#封装ApiRequests,支持多环境、多协议、加解密
class ApiRequest:
    '''
    将请求发送出去
    '''
    def send(self, data: dict):
        if data["schema"] ==  "http":
            #把host修改为ip，并附加host header
            env={
                "docker.testing-studio.com": {
                    "dev": "1.1.1.1",
                    "test": "1.1.1.2"
                },
                "default": "dev"
            }
            # 将请求域名替换为对应环境的url
            data["url"]=str(data["url"]).replace(
                "docker.testing-studio.com",
                env["docker.testing-studio.com"][env["default"]]
            )
            # 发送请求时，将头信息host添加为域名
            data["headers"]["Host"]="docker.testing-studio.com"

            res=requests.request(data["method"], data["url"], headers=data["headers"])
            # 响应结果是加密数据的处理
            if data["encoding"]=="base64":
                return json.loads(base64.b64decode(res.content))
            if data["encoding"]=="private":
                return json.loads(requests.post("url", data=res.content).content)
            else:
                return json.loads(res.content)


        elif "urllib" == data["schema"]:
            pass
        elif "dubbo" ==  data["schema"]:
            pass
        elif "websocket" == data["schema"]:
            pass
        else:
            pass