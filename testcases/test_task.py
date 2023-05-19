import allure
import pytest
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml


@allure.feature("任务模块")
class TestTask:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/task_datas.yml'))
    def test_sign_task(self, caseinfo):
        allure.dynamic.title("签到任务接口")
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        testcasename = caseinfo['name']
        RequestsUtil().send_request(testcasename=testcasename, method=method, url=url, headers=headers)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/accept_task_datas.yml'),
                             ids=['领取充值5豆任务', '领取盲盒消耗10000豆任务'])
    def test_accept_task(self, caseinfo):
        allure.dynamic.title("领取任务接口")
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['data']
        # verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name,url=url, method=method, headers=headers, data=datas)





if __name__ == '__main__':
    TestTask().test_sign_task()
