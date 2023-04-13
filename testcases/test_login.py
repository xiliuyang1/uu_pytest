import allure
import pytest

from utils.log_util import LogUtils
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, write_extract_yaml


@allure.feature("登录模块")
class TestLogin:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_data/test_login/test_login_datas.yml'))
    @pytest.mark.run(order=1)
    def test_mobile_login(self, caseinfo):
        allure.dynamic.title(caseinfo["name"])
        url = read_yaml("/test_data/common/host_config_datas.yml")['host'] + caseinfo['url']
        headers = caseinfo['headers']
        method = caseinfo['method']
        json = caseinfo['datas']
        req = RequestsUtil().send_request(method=method, url=url, headers=headers, data=json)
        if req.json()['status'] == 200:
            LogUtils().set_log().info("登录成功")
            LogUtils().set_log().info(req.json())
            data = {'token': req.json()['data']['token']}
            write_extract_yaml('/test_data/common/token.yml', data)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_data/test_login/test_quit_login_datas.yml"))
    def test_quit_login(self, get_token, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        url = read_yaml("/test_data/common/host_config_datas.yml")['host'] + caseinfo['url']
        method = caseinfo['method']
        header = {'token': get_token,
                  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                  'lang': 'zh-CN'
                  }
        req = RequestsUtil().send_request(method=method, url=url, headers=header, data='')
        try:
            assert req.json()['status'] == 200
            LogUtils().set_log().debug(req.json())
            LogUtils().set_log().debug("退出登录成功")
        except AssertionError:
            LogUtils().set_log().debug(req.json())
            LogUtils().set_log().debug('退出登录失败')
