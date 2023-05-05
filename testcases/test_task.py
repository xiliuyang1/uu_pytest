import allure
import pytest

from utils.log_util import LogUtil
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml


@allure.feature("任务模块")
class TestTask:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/task_datas.yml'))
    def test_sign_task(self, caseinfo, login_token):
        allure.dynamic.title(caseinfo['name'])
        print(caseinfo)
        headers = {
            'token': login_token,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'lang': 'zh-CN'
        }
        url = read_yaml("/common/host_config_datas.yml")['host'] + caseinfo['url']
        method = caseinfo['method']
        req = RequestsUtil().send_request(method=method, headers=headers, url=url, data='')
        print(req)
        if req.json()['data']['sign_in_reward'] == 200:
            LogUtils().set_log().info("签到成功，获得" + req.json()['data']['sign_in_reward'] + "豆子")
        else:
            LogUtils().set_log().info("您已领取过签到奖励")


if __name__ == '__main__':
    TestTask().test_sign_task()
