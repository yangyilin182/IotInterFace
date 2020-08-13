import hmac
import hashlib

class EncryptHmac:
    '''
    密钥加密
    '''
    def __init__(self):
        pass

    @classmethod
    def encrypt_sha1_digest(cls,key,message):
        '''
        #获取bytes类型加密结果
        :param key: bytes类型 加密密钥
        :param message: bytes 类型 待加密内容
        :return: bytes类型 加密后的内容
        '''
        return hmac.new(key, message, digestmod=hashlib.sha1).digest()

    @classmethod
    def encrypt_sha1_hexdigest(cls, key, message):
        '''
        #获取16进制加密结果
        :param key: bytes类型 加密密钥
        :param message: bytes类型 待加密内容
        :return: str类型 加密后的内容
        '''
        return hmac.new(key, message, digestmod=hashlib.sha1).hexdigest()

    @classmethod
    def encrypt_sha256_digest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: bytes类型
        '''
        return hmac.new(key, message, digestmod=hashlib.sha256).digest()

    @classmethod
    def encrypt_sha256_hexdigest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: str类型
        '''
        return hmac.new(key, message, digestmod=hashlib.sha256).hexdigest()

    @classmethod
    def encrypt_sha384_digest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: bytes类型
        '''
        return hmac.new(key, message, digestmod=hashlib.sha384).digest()

    @classmethod
    def encrypt_sha384_hexdigest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: str类型
        '''
        return hmac.new(key, message, digestmod=hashlib.sha384).hexdigest()

    @classmethod
    def encrypt_sha512_digest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: bytes类型
        '''
        return hmac.new(key, message, digestmod=hashlib.sha512).digest()

    @classmethod
    def encrypt_sha512_hexdigest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: str类型
        '''
        return hmac.new(key, message, digestmod=hashlib.sha512).hexdigest()

    @classmethod
    def encrypt_md5_digest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: bytes类型
        '''
        return hmac.new(key, message, digestmod=hashlib.md5).digest()

    @classmethod
    def encrypt_md5_hexdigest(cls, key, message):
        '''
        :param key: bytes类型
        :param message: bytes类型
        :return: str类型
        '''
        return hmac.new(key, message, digestmod=hashlib.md5).hexdigest()

