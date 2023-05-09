import allure
import pytest

from api.user_api import mobile_login, quit_login
from utils.log_util import LogUtil
from utils.yaml_util import read_yaml


@allure.feature("登录模块")
class TestLogin:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_login/login_datas.yml'))
    @pytest.mark.run(order=1)
    def test_mobile_login(self, caseinfo):
        allure.dynamic.title(caseinfo["name"])
        try:
            req = mobile_login(caseinfo)
            if req.json()['status'] == 200:
                LogUtil().set_log().info("登录成功")
        except Exception as e:
            LogUtil().set_log().info("{}接口请求失败，请检查{}".format(caseinfo["name"], e))

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_login/quit_login_datas.yml'))
    @pytest.mark.run(order=-1)
    def test_quit_login(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        try:
            req = quit_login(caseinfo)
            if req.json()['status'] == 200:
                LogUtil().set_log().info("退出登录成功")
        except Exception as e:
            LogUtil().set_log().info("退出登录失败,请检查{}".format(caseinfo['name'], e))
