import requests
from requests_toolbelt import MultipartEncoder
from config.Constants import config


class TemplateConfig:
    # TODO 封装基类处理请求
    # 添加模板获取语音文件base64
    def upload_base64(self,params, headers):
        # url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!uploadBase64TmpContent.action"
        r = requests.get(config.base64_url, params=params, headers=headers, verify=False)
        print(r.json())
        return r.json()

    # 审核开关机、广告、消息模板
    def audit_template(self, fields,params=None):
        # url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!add.action"
        m = MultipartEncoder(fields=fields)
        r = requests.post(config.message_url, data=m, params=params,headers={'Content-Type': m.content_type}, verify=False)
        print(r.content)
        return

    #审核自定义语音前、后缀、只播报自定义等模板
    def audit_device_voice_temlate(self,fields,params=None):
        url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/company/device/manager/confinfo/voice/voice!addDeviceVoiceTemplate.action"
        m = MultipartEncoder(fields=fields)
        r = requests.post(url, data=m, params=params, headers={'Content-Type': m.content_type}, verify=False)
        print(r.content)
        return

    #优惠金模板
    def audit_discount_voice_temlate(self,fields,params=None):
        # url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/concessions!add.action"
        m = MultipartEncoder(fields=fields)
        r = requests.post(config.discount_url, data=m, params=params, headers={'Content-Type': m.content_type}, verify=False)
        print(r.content)
        return

    # 验证码模板
    def audit_verifycode_voice_temlate(self, fields, params=None):
        # url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/codeTmp!add.action"
        m = MultipartEncoder(fields=fields)
        r = requests.post(config.verifycode_url, data=m, params=params, headers={'Content-Type': m.content_type}, verify=False)
        print(r.content)
        return



    #获取最新添加的验证码记录id及模板编号
    #todo 使用jsonpath优化提取数据
    def get_verifycode_info(self, data, headers=None):
        url= "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/codeTmp!init.action"
        r=requests.post(url,data=data,headers=headers,verify=False)
        print(r.json())
        verifycode_info={}
        verifycode_info['row_id']=r.json()['items'][0]['id']
        verifycode_info['template_id']=r.json()['items'][0]['tmpType']
        return verifycode_info