import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_variable_yaml


class TestBoxs:
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/recently_open_record.yml"))
    def test_recently_open_record(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = read_variable_yaml(caseinfo['datas'])
        RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_boxs/box_list.yml"))
    def test_box_list(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        datas = caseinfo['datas']
        rep = RequestsUtil().send_request(testcasename=name, method=method, url=url, data=datas)
        return rep

    def test_box_details(self):
        pass

    # def test_recently_open_record(self):
    #     pass
    #
    # def test_recently_open_record(self):
    #     pass
    #
    # def test_recently_open_record(self):
    #     pass
