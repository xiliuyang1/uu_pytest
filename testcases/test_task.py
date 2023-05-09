import allure
import pytest

from api.user_api import sign_task
from utils.log_util import LogUtil
from utils.yaml_util import read_yaml


@allure.feature("任务模块")
class TestTask:
    # @pytest.mark.run(order=4)
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/task_datas.yml'))
    def test_sign_task(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        # print("签到任务的传参：{}".format(caseinfo))
        req = sign_task(caseinfo)
        if req.json()['status'] == 200:
            if req.json()['data']['sign_in_reward'] == 200:
                LogUtil().set_log().info("签到成功，获得" + req.json()['data']['sign_in_reward'] + "豆子")
            else:
                LogUtil().set_log().info("您已领取过签到奖励")
        else:
            LogUtil().set_log().error("{}接口请求失败，请检查：{}".format(caseinfo['url'], req.json()))


if __name__ == '__main__':
    TestTask().test_sign_task()
