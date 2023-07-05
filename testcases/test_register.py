import allure
import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_variable_yaml, read_yaml


@allure.feature("个人中心-账号管理")
class TestRegister:
    # 手机号注册
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_login/phone_register.yml"))
    def test_phone_register(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = caseinfo['headers']
        datas = read_variable_yaml(caseinfo['datas'])
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)

    # 邮箱注册
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_login/email_register.yml"))
    def test_email_register(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = caseinfo['headers']
        datas = read_variable_yaml(caseinfo['datas'])
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)

    # steam账号登录
    def test_steam_register(self):
        pass
