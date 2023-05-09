import allure
import pytest

from api.activity_api import get_activity_base_datas, get_lucky_cases_datas
from utils.log_util import LogUtil
from utils.yaml_util import read_yaml


@allure.feature("巴黎major猜冠军活动")
class TestActivity:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_activity/get_activity_base_datas.yml'))
    def test_get_activity_datas(self, caseinfo):
        allure.dynamic.title(caseinfo["name"])
        req = get_activity_base_datas(caseinfo=caseinfo, activity_code='CSGO_IEM_RIO')
        if req.json()['status'] == 200:
            LogUtil().set_log().info("[{}]接口请求成功".format(caseinfo["name"]))
        else:
            LogUtil().set_log().error("[{}]接口请求失败，请检查".format(caseinfo["name"]))

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_activity/get_lucky_cases_datas.yml'))
    def test_get_activity_lucky_cases(self, caseinfo):
        allure.dynamic.title(caseinfo["name"])
        req = get_lucky_cases_datas(caseinfo=caseinfo, cases_code='CSGO_MAJOR_PARIS_JOIN')
        if req.json()['status'] == 200:
            LogUtil().set_log().info("[{}]接口请求成功".format(caseinfo["name"]))
        else:
            LogUtil().set_log().error("[{}]接口请求失败，请检查".format(caseinfo["name"]))

    # def test_activity_recharge(self):
    #     pass


if __name__ == '__main__':
    print(TestActivity().test_get_activity_datas())
