import allure
import jsonpath
import pytest

from testcases.test_login import TestLogin
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml, read_image_file, write_extract_yaml


@allure.feature("个人中心-账号管理")
class TestAcountManage:
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_login/change_password.yml"))
    def test_change_password(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/edit_nickname.yml"))
    def test_edit_nickname(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/edit_avatar.yml"))
    def test_edit_avatar(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        files = {"image": ("1.png", read_image_file('1.png'), "image/png")}
        # files = {'image': read_image_file('1.jpg')}
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, files=files)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/bind_phone.yml"))
    def test_bind_phone(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)
        write_extract_yaml({"unbind_mobile": caseinfo['datas']['mobile']})

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/unbind_phone.yml"))
    def test_unbind_phone(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/bind_mail.yml"))
    def test_bind_mail(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)
        if str(caseinfo['name']) == "绑定邮箱--当前账号未绑定邮箱":
            write_extract_yaml({"unbind_mail": caseinfo['datas']['mail']})

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/unbind_mail.yml"))
    def test_unbind_mail(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/bind_parent.yml"))
    def test_bind_parent(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_account_manage/identity_verify.yml"))
    def test_identity_verify(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                          verify=verify)
        if str(caseinfo['url']) == "/api/user/IdentityCertify/create" and res.json()['status'] == 200:
            write_extract_yaml({"query_id": jsonpath.jsonpath(res.json(), "$.data.query_id")})
