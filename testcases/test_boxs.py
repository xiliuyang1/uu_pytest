import allure
import jsonpath
import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml, write_extract_yaml


@allure.feature("饰品盲盒模块")
class TestBoxs:
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/guess_websocket_config.yml"))
    def test_guess_websocket_config(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/box_list.yml"))
    def test_box_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas)
        # 正则表达式提取cases_id：
        write_extract_yaml({'cases_id': jsonpath.jsonpath(res.json(), "$..list[0].cases[0].id")})

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/recently_open_record.yml"))
    def test_recently_open_record(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = read_variable_yaml(caseinfo['datas'])
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/box_item_list.yml"))
    def test_box_item_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = read_variable_yaml(caseinfo['datas'])
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/user_test_open.yml"))
    def test_user_test_open(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)
        allure.dynamic.description(
            "试玩开出的饰品：" + str(jsonpath.jsonpath(res.json(), "$..win_items[*].item.name.zh-CN")))

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/user_open.yml"))
    def test_user_open(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)
        allure.dynamic.description(
            "开出的饰品：" + str(jsonpath.jsonpath(res.json(), "$..win_items[*].item.name.zh-CN")))

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/cherrypick_box_list.yml"))
    def test_cherrypick_box_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas)
        allure.dynamic.description(
            "精选箱子有：" + str(jsonpath.jsonpath(res.json(), "$.data[*].name.zh-CN")))

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/welfare_box_info.yml"))
    def test_welfare_box_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas, verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/get_newbox_list.yml"))
    def test_get_newbox_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas, verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/welfare_box_recently_record.yml"))
    def test_welfare_box_recently_record(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas, verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/welfare_box_user_history.yml"))
    def test_welfare_box_user_history(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = read_variable_yaml(caseinfo['verify'])
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                          verify=verify)
        write_extract_yaml({"record_id": jsonpath.jsonpath(res.json(), "$..data.list[0].id")})

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/receive_luckybox_reward.yml"))
    def test_receive_luckybox_reward(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/open_welfare_box.yml"))
    def test_open_welfare_box(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)
