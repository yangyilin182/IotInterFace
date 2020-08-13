import base64

from utils.HashlibEncryptUtil import EncryptHashlib, Base64
from utils.HmacEncryptUtil import EncryptHmac


class TestEncrypt:
    def setup(self):
        self.enc=EncryptHmac()
        self.en=EncryptHashlib()
        self.b64=Base64()

    def test_encrypt(self):
        # a=self.enc.encrypt_md5_digest(b'fdf',b'fdf')
        # a=self.enc.encrypt_md5_hexdigest(b'fdf',b'fdf')
        # b=self.en.encrypt_md5_hexdigest(b'fdf')
        # c=self.en.encrypt_md5_digest(b'fdf')
        d=self.b64.encrypt_base64(b'fdf')
        a=self.b64.decrypt_base64(d.decode('utf-8'))

        # data = b'hello'
        # based_data1 = base64.b64encode(data)
        # plain_data1 = base64.b64decode(based_data1)
        # print(plain_data1)

        # print(type(b))
        # print(b)
        # print(c)
        # print(type(c))
        print(d)
        print(type(d))
        print(a)
        print(type(a))


    pass