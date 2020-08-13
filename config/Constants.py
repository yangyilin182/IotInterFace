
class config:
    '''
    添加配置模板
    '''
    # 测试时候待输入部分
    # cookie 执行测试前需要抓包获取cookie值
    cookie = '7C775E05C8FB568F532EF48DCD4B0EE8'

    # 设备 sn
    device_sn = 'test_dev_qyy_0064'

    #推送消息相关配置
    #预发
    push_url = "https://iotmessage-testing.cloudentify.com/v1/audio/"
    appkey = '989F23B783CBD649D25D'
    app_secret = "F3354DD2F7B847D5CF8B27CBF7DF2BEFFA86432D"

    #预演：
    # push_url = "https://iotmessage-inter.cloudentify.com/v1/audio"
    # appkey = 'C015B9AE28A09BFD989D'
    # app_secret = "16DA41FB7DB75313F9B56887171C55D811B4D9E5"


    #获取语音文件base64 url
    base64_url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!uploadBase64TmpContent.action"
    #开关机、广告、消息基础 url
    message_url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/voice!add.action"
    #前缀、后缀、自定义播金额、自定义不播金额 url
    custom_voice_url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/company/device/manager/confinfo/voice/voice!addDeviceVoiceTemplate.action"
    #优惠金 url
    discount_url = "https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/concessions!add.action"
    #验证码 url
    verifycode_url="https://iotoperation-testing.cloudentify.com/operationflat/manager/confinfo/voice/codeTmp!add.action"
    #获取设备id url
    get_deviceid_url="https://iotoperation-testing.cloudentify.com/operationflat/manager/company/companyinfo/phoneDevice!init.action"
    #开关机、广告、消息基础 params
    message_params = {
        'speed': '50',
    }
    #开关机、消息基础 fields
    message_fields = {
              'voiceFile': '',
              'voiceInfo.dOrgunitId': '',
              'voiceInfo.id': '',
              'voiceInfo.orgunitNumber': '',
              'voiceInfo.sloganVoiceRuleType': '1',
              'voiceInfo.sloganVoiceRuleValue': '',
              'voiceInfo.speed': '50',
              'voiceInfo.tmpType': '0',
              'voiceInfo.upgradeScope': '0',
              'voiceInfo.uploadMode': '0'
    }

    #广告基础fields
    ad_fields={'voiceFile': '',
              'voiceInfo.status': '',
              'voiceInfo.enabled': '',
              'voiceInfo.startPlay': "480,1320",
              'voiceInfo.dOrgunitId': '',
              'voiceInfo.id': '',
              'voiceInfo.orgunitNumber': '',
              'voiceInfo.speed': '50',
              'voiceInfo.tmpType': '0',
              'voiceInfo.upgradeScope': '0',
              'voiceInfo.uploadMode': '0',
              'voiceInfo.tempType': '3'
    }

    #前后缀、自定义播金额、自定义不播金额基础 fields
    custom_voice_fields = {
        'voiceFile': '',
        'voiceInfo.id': '',
        'voiceInfo.speed': '50',
        'voiceInfo.tempType': '4',
        'voiceInfo.uploadMode': '0'
    }
    #优惠金、验证码基础 fields
    discount_fields = {
                'voiceFile': '',
                'voiceInfo.id': '',
                'voiceInfo.speed': '50',
                'voiceInfo.tmpType': '0',
                'voiceInfo.upgradeScope': '0',
                'voiceInfo.uploadMode': '0'
            }

    #获取设备id data
    get_deviceid_data={
        'deviceQueryForm.code': '',
        'deviceQueryForm.endCreateTime': '',
        'deviceQueryForm.endDeviceSn': '',
        'deviceQueryForm.endInitTime': '',
        'deviceQueryForm.firmwareCode': '-1',
        'deviceQueryForm.imei': '',
        'deviceQueryForm.initStatus': '-1',
        'deviceQueryForm.orderNumber': '',
        'deviceQueryForm.orgunitNumber': '',
        'deviceQueryForm.paycodeCode': '',
        'deviceQueryForm.shipmentCode': '',
        'deviceQueryForm.specId': '',
        'deviceQueryForm.startCreateTime': '',
        'deviceQueryForm.startDeviceSn': '',
        'deviceQueryForm.startInitTime': '',
        'deviceQueryForm.state': '-1',
        'page': '1',
        'pagesize': '20'
    }


