import allure
import pytest

from utils.log_util import LogUtils
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml


@allure.feature("任务模块")
class TestTask:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_data/test_task/test_task_datas.yml'))
    def test_sign_task(self, caseinfo, get_token):
        allure.dynamic.title(caseinfo['name'])
        print(caseinfo)
        token = get_token
        headers = {
            'token': token,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'lang': 'zh-CN'
        }
        url = read_yaml("/test_data/common/host_config_datas.yml")['host'] + caseinfo['url']
        method = caseinfo['method']
        req = RequestsUtil().send_request(method=method, headers=headers, url=url, data='')
        print(req)
        if req.json()['data']['sign_in_reward'] == 200:
            LogUtils().set_log().info("签到成功，获得" + req.json()['data']['sign_in_reward'] + "豆子")
        else:
            LogUtils().set_log().info("您已领取过签到奖励")


if __name__ == '__main__':
    TestTask().test_sign_task()
