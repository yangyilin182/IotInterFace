from api.ConfigApi import ConfigApi


class Test_config_template:
    @classmethod
    def setup_class(cls):
        cls.temp_config = ConfigApi()


    def test_config_poweron_template(self):
        '''
        开机模板
        :return:
        '''
        companyId = '147'
        template_name = '开机'
        template_Content = '开机'
        self.temp_config.config_poweron_template(companyId, template_name, template_Content)

    def test_onfig_poweroff_template(self):
        '''
        关机模板
        :return:
        '''
        companyId = '147'
        template_name = '关机'
        template_Content = '关机'
        self.temp_config.config_poweroff_template(companyId, template_name, template_Content)

    # VoiceRuleType：1 每次开机
    # VoiceRuleType：2  定时播报
    # VoiceRuleType：3  收款到账
    # VoiceRuleValue： 联动填写部分，定时播报和收款到账部分需要填写
    def test_config_ad_template(self):
        '''
        广告模板
        :return:
        '''
        companyId = '147'
        template_Content = '广告'
        template_name = '广告'
        VoiceRuleType = '2'
        #收款到账次数或者定时播报次数
        VoiceRuleValue='1'
        # 每次开机调用
        # self.temp_config.config_ad_template(companyId, template_name, template_Content, VoiceRuleType)
        # 定时播报和收款到账调用
        self.temp_config.config_ad_template(companyId, template_name, template_Content, VoiceRuleType,VoiceRuleValue)

    def test_config_message_template(self):
        '''
        消息模板
        :return:
        '''
        for i in range(1):
            companyId = '147'
            template_Content = '消息消息'
            template_name = '消息'
            self.temp_config.config_message_template(companyId, template_name, template_Content)

    # customVoiceRule': '0',前缀
    # customVoiceRule': '1',后缀
    # customVoiceRule': '2',自定义播金额
    # customVoiceRule': '3',自定义不播金额
    def test_config_device_voice_temlate(self):
        '''
        前后缀、自定义播金额、自定义不播金额模板
        :return:
        '''
        companyId = '147'
        template_Content = '自定义语音'
        template_name = '自定义语音'
        customVoiceRule = '3'
        device_sn = 'test_dev_qyy_0064'
        self.temp_config.config_device_voice_temlate(companyId, device_sn,template_name, template_Content,
                                                     customVoiceRule)

    def test_config_discount_voice_temlate(self):
        '''
        优惠金模板
        :return:
        '''
        for i in range(1):
            companyId = '147'
            template_Content = '优惠金'+str(i)
            template_name = '优惠金'+str(i)
            self.temp_config.config_discount_voice_temlate(companyId, template_name, template_Content)

    def test_config_verifycode_temlate(self):
        '''
        验证码模板
        :return:
        '''
        for i in range(1):
            companyId = '147'
            template_name = '验证码啊'+str(i)
            template_Content = '验证码啊'+str(i)
            self.temp_config.config_verifycode_temlate(companyId, template_name, template_Content)


