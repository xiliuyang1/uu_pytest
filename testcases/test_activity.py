import allure
import pytest

from utils.log_util import LogUtil
from utils.yaml_util import read_yaml, read_variable_yaml


@allure.feature("赛事活动模块")
class TestActivity:
    @pytest.mark.parametrize("caseinfo", [read_variable_yaml(
        '/test_activity/get_activity_datas.yml')])  # read_variable_yaml('/test_activity/get_activity_datas.yml') 字典格式
    def test_get_activity_datas(self, caseinfo):
        allure.dynamic.title("获取活动的基本信息")
        LogUtil().set_log().info(caseinfo)
        url = caseinfo['url']
        method = caseinfo['method']
        headers = caseinfo['']


if __name__ == '__main__':
    print(TestActivity().test_get_activity_datas())
