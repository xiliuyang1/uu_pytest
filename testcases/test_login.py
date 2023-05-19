import allure
import pytest
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml


@allure.feature("登录模块")
class TestLogin:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_login/login_datas.yml'))
    @pytest.mark.run(order=1)
    def test_mobile_login(self, caseinfo):
        allure.dynamic.title(caseinfo["name"])
        name = caseinfo['name']
        method = caseinfo['method']
        headers = read_variable_yaml(caseinfo['headers'])
        url = caseinfo['url']
        data = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=data)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_login/quit_login_datas.yml'))
    @pytest.mark.run(order=-1)
    def test_quit_login(self, caseinfo):
        allure.dynamic.title('退出登录')
        name = caseinfo['name']
        method = caseinfo['method']
        headers = read_variable_yaml(caseinfo['headers'])
        url = caseinfo['url']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers)