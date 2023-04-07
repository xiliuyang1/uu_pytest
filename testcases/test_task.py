import logging

import allure
import pytest

from common.get_token import get_token
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml


class TestTask:
    @pytest.mark.parametrize("token_info", read_yaml('/test_data/test_login_datas.yml'))
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_data/test_task_datas.yml'))
    def test_sign_task(self, caseinfo, token_info):
        allure.story(caseinfo['name'])
        print(caseinfo)
        token = get_token()
        headers = {'token': token}
        url = read_yaml(r"/config/host_config.yml")['host']['dev'] + caseinfo['url']
        method = caseinfo['method']
        req = RequestsUtil().send_request(method=method, headers=headers, url=url, data="")
        print(req)
        assert req.json()['data']['sign_in_reward'] != 0
        logging.info("签到成功，获得" + req.json()['data']['sign_in_reward'] + "豆子")


if __name__ == '__main__':
    TestTask().test_sign_task()
