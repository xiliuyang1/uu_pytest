import allure
import pytest
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml


@allure.feature("任务模块")
class TestTask:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/sign_task.yml'))
    def test_sign_task(self, caseinfo):
        allure.dynamic.title("签到任务接口")
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/accept_task.yml'))
    def test_accept_task(self, caseinfo):
        allure.dynamic.title("领取任务接口")
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/get_task_list.yml'))
    def test_get_task_list(self, caseinfo):
        allure.dynamic.title("获取任务列表接口")
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/receive_task_reword.yml'))
    def test_receive_task_reword(self, caseinfo):
        allure.dynamic.title("领取任务奖励接口")
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_task/task_receive_record.yml'))
    def test_task_receive_record(self, caseinfo):
        allure.dynamic.title("查看用户任务领取记录接口")
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers)


if __name__ == '__main__':
    TestTask().test_sign_task()
