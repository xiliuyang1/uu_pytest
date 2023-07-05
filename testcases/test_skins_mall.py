import allure
import jsonpath
import pytest
from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml, write_extract_yaml


@allure.feature("饰品商城模块")
class TestSkinsMall:
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_skins_mall/get_steam_list.yml"))
    def test_get_steam_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = caseinfo['datas']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)
        write_extract_yaml({"steam_id": jsonpath.jsonpath(res.json(), "$.data[0].steam_id")[0]})

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_skins_mall/get_steam_status.yml"))
    def test_get_steam_status(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_skins_mall/skins_list.yml"))
    def test_skins_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        verify = caseinfo['verify']
        res = RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas, verify=verify)
        write_extract_yaml({"item_id": jsonpath.jsonpath(res.json(), "$.data.list[0].id")[0]})

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_skins_mall/get_item_sell_price.yml"))
    def test_get_item_sell_price(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas, verify=verify)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_skins_mall/steam_check_health.yml"))
    def test_steam_check_health(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = read_variable_yaml(caseinfo['headers'])
        datas = read_variable_yaml(caseinfo['datas'])
        verify = caseinfo['verify']
        RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=datas, verify=verify)

