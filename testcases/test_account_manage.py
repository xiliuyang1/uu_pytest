import allure
import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml


@allure.feature("个人中心-账号管理")
class TestPassword:
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_login/change_password.yml"))
    def test_reset_psd(self, caseinfo):
        allure.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)

    def test_edit_nickname(self):
        pass

    def test_edit_head_image(self):
        pass

    def test_bind_phone(self):
        pass

    def test_unbind_phone(self):
        pass

    def test_bind_mail(self):
        pass

    def test_unbind_mail(self):
        pass

    def test_bind_parent(self):
        pass

    def test_identity_verify(self):
        pass

    def test_account_cancellation(self):
        pass
