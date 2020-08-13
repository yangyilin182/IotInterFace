import random
import string
import time
import urllib

import requests
import hmac
import base64
from hashlib import sha256

from api.BaseApi import BaseApi
from config.Constants import config
from utils.Base64 import Base64
from utils.HmacEncryptUtil import EncryptHmac


class PushApi(BaseApi):
    def push(self,message,push_template):
        data=self.make_data(message,push_template)
        # r = requests.post(config.push_url, data=data, verify=False)
        r=requests.post(config.push_url,data=data,verify=False).json()
        print(r)
        return r

    def pushByPaycode(self):
        pass

    def pushdiscount(self):
        pass

    def pushbypaycodediscount(self):
        pass

    def pushverifycode(self):
        pass

    def pushverifycodebypaycode(self):
        pass

    def refreshQr(self):
        pass

    def syncOrder(self):
        pass

    def bindDevice(self):
        pass

    def unbindDevice(self):
        pass

    def pushTTS(self):
        pass

    def pushTTSByPayCode(self):
        pass
