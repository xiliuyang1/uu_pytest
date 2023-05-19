import allure
import pytest
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml, write_extract_yaml, read_extract_yaml, clear_extract_yaml


@allure.feature("CSGO巴黎major赛事活动相关")
class TestActivity:
    @pytest.mark.parametrize("caseinfo", read_yaml('/test_activity/get_activity_base_datas.yml'))
    def test_get_activity_datas(self, caseinfo):
        allure.dynamic.title('获取活动的基本信息')
        name = caseinfo['name']
        url = caseinfo['url']
        method = caseinfo['method']
        headers = read_variable_yaml(caseinfo['headers'])
        data = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers, data=data)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_activity/get_lucky_cases_datas.yml'))
    def test_get_activity_lucky_cases(self, caseinfo):
        allure.dynamic.title('获取活动箱子')
        name = caseinfo['name']
        url = caseinfo['url']
        method = caseinfo['method']
        headers = read_variable_yaml(caseinfo['headers'])
        data = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers, data=data)

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_activity/activity_recharge_datas.yml'))
    def test_activity_recharge(self, caseinfo):
        allure.dynamic.title('生成活动页充值订单')
        name = caseinfo['name']
        url = caseinfo['url']
        method = caseinfo['method']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        req = RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers, data=datas)
        data = {"order_id": req.json()['data']['order_id']}
        write_extract_yaml(data, file_name='/common/extract_datas.yml')

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_activity/common_recharge_datas.yml'))
    def test_common_recharge(self, caseinfo):
        allure.dynamic.title('生成普通充值订单')
        name = caseinfo['name']
        url = caseinfo['url']
        method = caseinfo['method']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        req = RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers, data=datas)
        # common_data = {"order_id": req.json()['data']['order_id']}
        # write_extract_yaml(common_data, file_name='/common/extract_datas.yml')

    @pytest.mark.parametrize("caseinfo", read_yaml('/test_activity/set_recharge_success.yml'))
    def test_set_recharge_success(self,caseinfo):
        allure.dynamic.title('手动设置充值订单成功')
        name = caseinfo['name']
        url = caseinfo['url']
        datas = read_variable_yaml(caseinfo['datas'])
        method = caseinfo['method']
        headers = caseinfo['headers']
        # datas = {
        #     'order_id': read_extract_yaml('/common/extract_datas.yml')['order_id'],
        #     'out_trade_no': 123456
        # }
        RequestsUtil().send_request(testcasename=name, url=url, method=method, headers=headers, data=datas)
        clear_extract_yaml('/common/extract_datas.yml')

