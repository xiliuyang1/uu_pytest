import time

import allure
import pytest

from common.get_token import get_token
from utils.log_util import LogUtils
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, write_extract_yaml


@allure.epic("项目名称：优优电竞项目")
@allure.feature("测试模块：登录模块")
class TestLogin:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_data/test_login_datas.yml'))
    @allure.story('登录测试')
    def test_mobile_login(self, caseinfo):
        allure.dynamic.title(caseinfo["name"])
        url = read_yaml("/config/host_config.yml")['host']['dev'] + caseinfo['url']
        headers = caseinfo['headers']
        method = caseinfo['method']
        json = caseinfo['datas']
        req = RequestsUtil().send_request(method=method, url=url, headers=headers, data=json)
        LogUtils().set_log().debug(req.json())
        LogUtils().set_log().debug(req.json()['status'])
        assert req.json()['status'] == 200
        LogUtils().set_log().debug("登录成功")

    @allure.story("退出登录")
    def test_quit_login(self):
        url = read_yaml("/config/host_config.yml")['host']['dev'] + '/api/user/user/loginOut'
        method = 'post'
        token = get_token()
        header = {'token': token}
        print(header)
        req = RequestsUtil().send_request(method=method, url=url, headers=header, data='')
        try:
            assert req.json()['status'] == 200
            LogUtils().set_log().debug(req.json())
            LogUtils().set_log().debug("退出登录成功")
        except AssertionError:
            LogUtils().set_log().debug(req.json())
            LogUtils().set_log().debug('退出登录失败')
