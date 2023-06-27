import allure
import jsonpath
import pytest

from utils.log_util import my_logging
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml, write_extract_yaml, read_extract_yaml


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

    # 钥匙武器箱相关接口
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/weapon_box_list.yml"))
    def test_weapon_box_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/weapon_box_info.yml"))
    def test_weapon_box_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/weapon_box_exchange_key.yml"))
    def test_weapon_box_exchange_key(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_activity/weapon_box_status.yml"))
    def test_weapon_box_status(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                          verify=verify)
        return res

    @pytest.mark.parametrize("caseinfo_1", read_yaml("/test_activity/weapon_box_status.yml"))
    @pytest.mark.parametrize("caseinfo_2", read_yaml("/test_activity/weapon_box_open.yml"))
    def test_weapon_box_open(self, caseinfo_1, caseinfo_2):
        # 先记录开箱前的钥匙数量，命悬一线武器箱：
        before_status_res = TestBoxs().test_weapon_box_status(caseinfo_1)
        if before_status_res.json()['code'] == 200:
            write_extract_yaml({"key_nums": jsonpath.jsonpath(before_status_res.json(), "$..key_nums")[0]})
        # 开启一次武器箱：
        allure.dynamic.title(caseinfo_2['name'])
        name = caseinfo_2['name']
        method = caseinfo_2['method']
        url = caseinfo_2['url']
        headers = read_variable_yaml(caseinfo_2['headers'])
        datas = caseinfo_2['datas']
        verify = caseinfo_2['verify']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)
        # 查询开启后的钥匙数量：
        if res.json()['code'] == 200:
            later_status_res = TestBoxs().test_weapon_box_status(caseinfo_1)
            if later_status_res.json()['code'] == 200:
                my_logging.info(jsonpath.jsonpath(later_status_res.json(), "$..key_nums")[0])
                if pytest.assume(jsonpath.jsonpath(later_status_res.json(), "$..key_nums")[0] == read_extract_yaml()[
                    'key_nums'] - 1):
                    my_logging.info("开启武器箱成功，且钥匙消耗正常。")
                else:
                    my_logging.info("钥匙消耗数量异常，请检查！")
            else:
                pass
