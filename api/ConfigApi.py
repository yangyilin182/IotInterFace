from urllib.parse import quote

from api.BaseApi import BaseApi
from config.Constants import config

class ConfigApi(BaseApi):
    '''
    模板配置api
    '''

    # 企业级模板添加及审核（自定义语音除外，是设备级模板）
    def audit_template(self, companyId, template_name, template_Content, params_params, params_fields, params, fields,
                       url, pre_params=None):
        base64_str = self.make_base64(template_Content, params, **params_params)
        fields = self.make_data_to_send(companyId, template_name, template_Content, base64_str, fields, **params_fields)
        if pre_params:
            self.send_file_by_stream(url, fields, pre_params)
        else:
            self.send_file_by_stream(url, fields)

    '''

        # 方案1：通过字典的update函数更新参数，将fields字典发送出去
        # fields.update(params_fields)
        # self.send_file_by_stream(config.message_url, fields)

        #方案2：将基础部分以及传参部分通过**解包，传递给**kwargs参数，组装kwargs字典后发送出去
        # self.send_file_by_stream_variable_param(config.message_url,**fields,**params_fields)
    '''

    #开机模板
    def config_poweron_template(self, companyId, template_name, template_Content):
        params = config.message_params
        fields = config.message_fields
        url = config.message_url
        params_params = {
            'tempType': '1',
        }
        params_fields = {
            'voiceInfo.tempType': '1'
        }
        self.audit_template(companyId, template_name, template_Content, params_params, params_fields, params, fields,
                            url)

    #关机模板
    def config_poweroff_template(self, companyId, template_name, template_Content):
        params = config.message_params
        fields = config.message_fields
        url = config.message_url
        params_params = {
            'tempType': '1',
        }
        params_fields = {
            'voiceInfo.tempType': '2'
        }
        self.audit_template(companyId, template_name, template_Content, params_params, params_fields, params, fields,
                            url)


    # 消息模板
    def config_message_template(self, companyId, template_name, template_Content):
        params = config.message_params
        fields = config.message_fields
        url = config.message_url
        params_params = {
            'tempType': '0',
        }
        params_fields = {
            'voiceInfo.tempType': '0'
        }
        self.audit_template(companyId, template_name, template_Content, params_params, params_fields, params, fields,
                            url)


    #广告模板
    def config_ad_template(self,companyId,template_name,template_Content,VoiceRuleType,VoiceRuleValue=''):
        params=config.message_params
        fields = config.ad_fields
        url = config.message_url
        params_params={
            'tempType': '3'
        }
        params_fields = {
                         'voiceInfo.sloganVoiceRuleType': VoiceRuleType,
                         'voiceInfo.sloganVoiceRuleValue': VoiceRuleValue
                         }
        ad_params = {
            'voiceInfo.filterType': '1'
        }
        self.audit_template(companyId, template_name, template_Content, params_params, params_fields, params, fields,
                            url,ad_params)



    # 前后缀、自定义播金额、自定义不播金额
    # 'voiceInfo.customVoiceRule': '0',前缀
    # 'voiceInfo.customVoiceRule': '1',后缀
    # 'voiceInfo.customVoiceRule': '2',自定义播金额
    # 'voiceInfo.customVoiceRule': '3',自定义不播金额
    def config_device_voice_temlate(self, companyId, device_sn, template_name, template_Content, customVoiceRule):
        # 根据sn 获取设备id
        deviceId = self.get_deviceid_by_sn(companyId, device_sn)
        # todo redis存储依赖数据
        # self.get_deviceid_by_sn(companyId, device_sn)
        # deviceId=self.r.hget('deviceid',config.device_sn)
        params_params = {
            'tempType': '4',
        }
        params = config.message_params
        fields = config.custom_voice_fields
        url = config.custom_voice_url
        params_fields = {
            'voiceInfo.deviceId': deviceId,
            'voiceInfo.customVoiceRule': customVoiceRule
        }
        pre_params = {
            'deviceId': deviceId
        }
        self.audit_template(companyId, template_name, template_Content, params_params, params_fields, params, fields,
                            url,pre_params)

    #优惠金模板
    def config_discount_voice_temlate(self,companyId,template_name,template_Content):
        params = config.message_params
        fields = config.discount_fields
        url = config.discount_url
        params_params = {
            'tempType': '7'
        }
        params_fields = {
                         'voiceInfo.tempType': '7'
                         }
        self.audit_template(companyId, template_name, template_Content, params_params, params_fields, params, fields,
                            url)


    #验证码模板
    def config_verifycode_temlate(self,companyId,template_name,template_Content):
        params = config.message_params
        fields = config.discount_fields
        url = config.verifycode_url
        params_params= {
            'tempType': '8',
        }
        params_fields = {
                         'voiceInfo.tempType': '8'
                         }
        self.audit_template(companyId, template_name, template_Content, params_params, params_fields, params, fields,
                            url)