from utils.CaseGenerateBySwagger import CaseGenerate

#swagger网页首页
web_url= 'http://openapi.qas.uml-tech.com/doc.html'
#swagger_url可在访问swagger的首页控制台抓包获得api-docs
swagger_url='http://openapi.qas.uml-tech.com/v2/api-docs'

appId = '481960543d21419497bef8bd8d5715ba'
token = '58f1bc232da8ae07c5a63e5e75d81e5b'
project_name = 'openapi_qas'

class Testautogen:
    def setup(self):
        pass

    def test_auto_gen_cases(self):
        CaseGenerate.auto_gen_cases(swagger_url, project_name, appId, token)