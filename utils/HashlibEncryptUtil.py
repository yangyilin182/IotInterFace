
import hashlib

class  EncryptHashlib:
    def __init__(self):
        pass

    @classmethod
    def encrypt_md5_hexdigest(cls, message):
        """
        :函数功能: 实现MD5加密
        :参数:
            message: bytes 被加密的内容 eg:'how to use sha1 in '.encode("utf8")
        :返回值: str 加密后的内容
        """
        m5 = hashlib.md5()
        m5.update(message)
        return m5.hexdigest()

    @classmethod
    def encrypt_md5_digest(cls, message):
        """
        :函数功能: 实现MD5加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.md5()
        m5.update(message)
        return m5.digest()

    @classmethod
    def encrypt_sha1_digest(cls, message):
        """
        :函数功能: 实现sha1加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha1()
        m5.update(message)
        return m5.digest()

    @classmethod
    def encrypt_sha1_hexdigest(cls, message):
        """
        :函数功能: 实现sha1加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha1()
        m5.update(message)
        return m5.hexdigest()

    @classmethod
    def encrypt_sha256_digest(cls, message):
        """
        :函数功能: 实现sha256加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha256()
        m5.update(message)
        return m5.digest()

    @classmethod
    def encrypt_sha256_hexdigest(cls, message):
        """
        :函数功能: 实现sha256加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha256()
        m5.update(message)
        return m5.hexdigest()

    @classmethod
    def encrypt_sha384_digest(cls, message):
        """
        :函数功能: 实现sha384加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha384()
        m5.update(message)
        return m5.digest()

    @classmethod
    def encrypt_sha384_hexdigest(cls, message):
        """
        :函数功能: 实现sha384加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha384()
        m5.update(message)
        return m5.hexdigest()

    @classmethod
    def encrypt_sha512_digest(cls, message):
        """
        :函数功能: 实现sha512加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha512()
        m5.update(message)
        return m5.digest()

    @classmethod
    def encrypt_sha512_hexdigest(cls, message):
        """
        :函数功能: 实现sha256加密
        :参数:
            message: bytes 被加密的内容
        :返回值: bytes 加密后的内容
        """
        m5 = hashlib.sha512()
        m5.update(message)
        return m5.hexdigest()