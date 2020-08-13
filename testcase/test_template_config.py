from urllib.parse import quote

from api.TemplateConfig import TemplateConfig


class TestTemplateConfig:
    @classmethod
    def setup_class(cls):
        cls.temp_config=TemplateConfig()

    def test_upload_base64(self):
        params = {
            'speed': '50',
            'tempType': '1',
            'tmpContent': quote('开机')
        }
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=1E528018B8B9CF0C9F09940121E247EE',
            'Host': 'iotoperation-testing.cloudentify.com',
            'Referer': 'https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/add.jsp',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.temp_config.upload_base64(params, headers)

    # 审核开机模板
    def test_audit_poweron_template(self):
        fields = {'voiceFile': '', 'voiceInfo.companyId': '147', 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
                  'voiceInfo.name': '开机', 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
                  'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '1',
                  'voiceInfo.tmpContent': '开机', 'voiceInfo.tmpType': '0',
                  'voiceInfo.tmpVoice': 'IyFBTVIKBCsZN/CkyDn/wACCAARliVD0/+/xRf1vEJwEN+qE+/0t8htdRlvoBKVQlD7o46uJEf6UiAQ3KBuP+MibDkxou5IEkHgLX/rGUAaSISwWBACXEm+e22u71ATUCARbYBau5FPCdNgBLeIER98Wnf2xcoXYgpcABHH5FqzrgrZEIZK5FATUyxmt0czSGsxoBtYE5+Ys+DvIpsDgmRqCBFMjhjrnZrBzwTRiigRLcQ5cykhbW5knK14EFEeMzI2xg/6B5+aKBKvU+g/KQjtsbnHs4ARImhvemGPeiUUIvVwEcc0irLj3b6JJSIHkBEjKIq7D3kLosMMajgRx0iKr+J1/CsKgAdAESM0iivOd0qMoWLogBHHSKD3o5y8a0HSjPARIzSK+s4ITaT8CBfwEpvIiy4JlItQif4SABNNRXfMAEjmx1AGRog==',
                  'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'}
        self.temp_config.audit_template(fields)

    def test_add_poweron_template_and_audit(self):
        '''
        全企业开机模板添加与审核
        :return:
        '''
        companyId = '147'
        template_Content = '开机'
        template_name = '开机'
        cookie = 'EE6475E36E798E3F6E2CC1A9777C785E'
        params = {
            'speed': '50',
            'tempType': '1',
            'tmpContent': quote(template_Content)
        }
        headers = {
            'Cookie': f'JSESSIONID={cookie}',
        }
        r = self.temp_config.upload_base64(params, headers)
        base64_str = r['object']
        print(base64_str)

        fields = {'voiceFile': '', 'voiceInfo.companyId': companyId, 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
                  'voiceInfo.name': template_name, 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
                  'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '1',
                  'voiceInfo.tmpContent': template_Content, 'voiceInfo.tmpType': '0',
                  'voiceInfo.tmpVoice': base64_str,
                  'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'}
        self.temp_config.audit_template(fields)

    def test_add_poweroff_template_and_audit(self):
        '''
        全企业关机模板添加与审核
        :return:
        '''
        companyId = '147'
        template_Content = '关机'
        template_name = '关机'
        cookie = 'EE6475E36E798E3F6E2CC1A9777C785E'
        params = {
            'speed': '50',
            'tempType': '1',
            'tmpContent': quote(template_Content)
        }
        headers = {
            'Cookie': f'JSESSIONID={cookie}',
        }
        r = self.temp_config.upload_base64(params, headers)
        base64_str = r['object']
        print(base64_str)

        fields = {'voiceFile': '', 'voiceInfo.companyId': companyId, 'voiceInfo.dOrgunitId': '', 'voiceInfo.id': '',
                  'voiceInfo.name': template_name, 'voiceInfo.orgunitNumber': '', 'voiceInfo.sloganVoiceRuleType': '1',
                  'voiceInfo.sloganVoiceRuleValue': '', 'voiceInfo.speed': '50', 'voiceInfo.tempType': '2',
                  'voiceInfo.tmpContent': template_Content, 'voiceInfo.tmpType': '0',
                  'voiceInfo.tmpVoice': base64_str,
                  'voiceInfo.upgradeScope': '0', 'voiceInfo.uploadMode': '0'}
        self.temp_config.audit_template(fields)

    def test_add_ad_template_and_audit(self):
        '''
        全企业广告模板添加与审核
        :return:
        '''
        companyId = '147'
        template_Content = '广告'
        template_name = '广告'
        cookie = 'EE6475E36E798E3F6E2CC1A9777C785E'
        params = {
            'speed': '50',
            'tempType': '1',
            'tmpContent': quote(template_Content)
        }
        headers = {
            'Cookie': f'JSESSIONID={cookie}',
        }
        r = self.temp_config.upload_base64(params, headers)
        base64_str = r['object']
        print(base64_str)
        fields = {
            'voiceFile': '',
            'voiceInfo.companyId': companyId,
            'voiceInfo.customVoiceRule': '0',
            'voiceInfo.dOrgunitId': '',
            'voiceInfo.enabled': '',
            'voiceInfo.id': '',
            'voiceInfo.name': template_name,
            'voiceInfo.orgunitNumber': '',
            'voiceInfo.sloganVoiceRuleType': '3',
            'voiceInfo.sloganVoiceRuleValue': '1',
            'voiceInfo.speed': '50',
            'voiceInfo.status': '',
            'voiceInfo.tempType': '3',
            'voiceInfo.tmpContent': template_Content,
            'voiceInfo.tmpType': '0',
            'voiceInfo.tmpVoice': base64_str,
            'voiceInfo.upgradeScope': '0',
            'voiceInfo.uploadMode': '0'
        }
        ad_params = {
            'voiceInfo.filterType': '1'
        }
        self.temp_config.audit_template(fields,ad_params)

    def test_add_prefix_template_and_audit(self):
        '''
        前缀模板添加与审核
        :return:
        '''
        companyId = '147'
        template_Content = '后缀'
        template_name = '后缀'
        # 'voiceInfo.customVoiceRule': '0',前缀
        # 'voiceInfo.customVoiceRule': '1',后缀
        # 'voiceInfo.customVoiceRule': '2',自定义播金额
        # 'voiceInfo.customVoiceRule': '3',自定义不播金额
        deviceId='2271383'
        cookie = 'BB5E771BF227C524FFD1C48843EEBFBB'
        params = {
            'speed': '50',
            'tempType': '4',
            'tmpContent': quote(template_Content)
        }
        headers = {
            'Cookie': f'JSESSIONID={cookie}',
        }
        r = self.temp_config.upload_base64(params, headers)
        base64_str = r['object']
        print(base64_str)
        fields = {
            'voiceFile': '',
            'voiceInfo.companyId': companyId,
            'voiceInfo.customVoiceRule': '1',
            'voiceInfo.deviceId': '2271383',
            'voiceInfo.id': '',
            'voiceInfo.name': template_name,
            'voiceInfo.speed': '50',
            'voiceInfo.tempType': '4',
            'voiceInfo.tmpContent': template_Content,
            'voiceInfo.tmpVoice': base64_str,
            'voiceInfo.uploadMode': '0'
        }
        pre_params = {
            'deviceId': deviceId
        }
        self.temp_config.audit_device_voice_temlate(fields,pre_params)


    def test_add_discount_temlate_and_audit(self):
        '''
        优惠金模板添加与审核
        :return:
        '''
        companyId = '147'
        template_Content = '打折啦打折啦'
        template_name = '打折啦打折啦'
        cookie = 'EE6475E36E798E3F6E2CC1A9777C785E'
        params = {
            'speed': '50',
            'tempType': '7',
            'tmpContent': quote(template_Content)
        }
        headers = {
            'Cookie': f'JSESSIONID={cookie}',
        }
        r = self.temp_config.upload_base64(params, headers)
        base64_str = r['object']
        print(base64_str)
        fields = {
            'voiceFile': '',
            'voiceInfo.companyId': companyId,
            'voiceInfo.id': '',
            'voiceInfo.name': template_name,
            'voiceInfo.speed': '50',
            'voiceInfo.tempType': '7',
            'voiceInfo.tmpContent': template_Content,
            'voiceInfo.tmpType': '0',
            'voiceInfo.tmpVoice': base64_str,
            'voiceInfo.upgradeScope': '0',
            'voiceInfo.uploadMode': '0'
        }
        self.temp_config.audit_discount_voice_temlate(fields)

    def test_add_verifycode_temlate_and_audit(self):
        '''
        验证码模板添加与审核
        :return:
        '''
        companyId = '147'
        template_Content = '验证码'
        template_name = '验证码'
        cookie = 'EE6475E36E798E3F6E2CC1A9777C785E'
        params = {
            'speed': '50',
            'tempType': '8',
            'tmpContent': quote(template_Content)
        }
        headers = {
            'Cookie': f'JSESSIONID={cookie}'
        }
        r = self.temp_config.upload_base64(params, headers)
        base64_str = r['object']
        print(base64_str)
        fields = {
            'voiceFile': '',
            'voiceInfo.companyId': companyId,
            'voiceInfo.id': '',
            'voiceInfo.name': template_name,
            'voiceInfo.speed': '50',
            'voiceInfo.tempType': '8',
            'voiceInfo.tmpContent': template_Content,
            'voiceInfo.tmpType': '0',
            'voiceInfo.tmpVoice': base64_str,
            'voiceInfo.upgradeScope': '0',
            'voiceInfo.uploadMode': '0'
        }
        self.temp_config.audit_verifycode_voice_temlate(fields)

        data = {
            'operType': '1',
            'page': '1',
            'pagesize': '20'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': f'JSESSIONID = {cookie}'
        }
        return self.temp_config.get_verifycode_info(data, headers)


    def test_get_verifycode_info(self):
        '''
        获取最新验证码id
        :return:
        '''
        data = {
            'operType': '1',
            'page': '1',
            'pagesize': '20'
        }
        cookies='EE6475E36E798E3F6E2CC1A9777C785E'
        headers = {
            'Cookie': f'JSESSIONID = {cookies}'
        }

        print("================================================")
        print(self.temp_config.get_verifycode_info(data, headers))

    def test_add_news_template_and_audit(self):
        '''
        消息模板添加与审核
        :return:
        '''
        companyId = '147'
        template_Content = '消息'
        template_name = '消息'
        cookie = '61B32ED9EE25419BE0D17B9CEE98697C'
        params = {
            'speed': '50',
            'tempType': '0',
            'tmpContent': quote(template_Content)
        }
        headers = {
            'Cookie': f'JSESSIONID={cookie}',
        }
        r = self.temp_config.upload_base64(params, headers)
        base64_str = r['object']
        print(base64_str)

        fields = {
            'voiceFile': '',
            'voiceInfo.companyId': companyId,
            'voiceInfo.dOrgunitId': '',
            'voiceInfo.id': '',
            'voiceInfo.name': template_name,
            'voiceInfo.orgunitNumber': '',
            'voiceInfo.sloganVoiceRuleType': '1',
            'voiceInfo.sloganVoiceRuleValue': '',
            'voiceInfo.speed': '50',
            'voiceInfo.tempType': '0',
            'voiceInfo.tmpContent': template_Content,
            'voiceInfo.tmpType': '',
            'voiceInfo.tmpVoice': base64_str,
            'voiceInfo.upgradeScope': '0',
            'voiceInfo.uploadMode': '0'
        }
        self.temp_config.audit_template(fields)


