import allure
import jsonpath
import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, write_extract_yaml, read_variable_yaml


@allure.feature("福利roll房模块")
class TestRollRoom:
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_roll_room/room_list.yml"))
    def test_room_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas, verify=verify)
        room_id = jsonpath.jsonpath(res.json(), "$..list[0].id")
        write_extract_yaml({"room_id": room_id[0]})

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_roll_room/my_join_list.yml"))
    def test_my_join_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_roll_room/room_detail.yml"))
    def test_room_detail(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas, verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_roll_room/roll_reward_list.yml"))
    def test_roll_reward_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas,
                                    verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_roll_room/join_room.yml"))
    def test_join_room(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, headers=headers, url=url, data=datas,
                                    verify=verify)
