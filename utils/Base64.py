import base64


class Base64:
    def __init__(self):
        pass

    @classmethod
    def encrypt_base64(self,message):
        '''
        编码base64
        :param message: bytes 被加密的内容
        :return: bytes 加密后的内容
        '''
        # base64.urlsafe_b64encode(message)
        return base64.b64encode(message)

    @classmethod
    def decrypt_base64(self,message):
        '''
        解码base64
        :param message: bytes 被解密的内容
        :return: bytes解密后的内容
        '''
        return base64.b64decode(message)

    @classmethod
    def encrypt_urlsafe_base64(self,message):
        '''
        编码urlsafe_base64
        :param message:
        :return:
        '''
        return base64.urlsafe_b64encode(message)

    @classmethod
    def decrypt_urlsafe_base64(self, message):
        '''
        解码urlsafe_base64
        :param message: bytes 被解密的内容
        :return: bytes解密后的内容
        '''
        return base64.urlsafe_b64decode(message)
