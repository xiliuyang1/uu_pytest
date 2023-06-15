import allure
import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml, read_image_file


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

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/edit_nickname.yml"))
    def test_edit_nickname(self, caseinfo):
        allure.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        print(headers, datas)
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/edit_avatar.yml"))
    def test_edit_avatar(self, caseinfo):
        allure.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        files = {"image": ("1.png", read_image_file('1.png'), "image/png")}
        # files = {'image': read_image_file('1.jpg')}
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, files=files)

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
