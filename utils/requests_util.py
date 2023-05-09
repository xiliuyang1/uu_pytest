import json

import requests

from utils.yaml_util import read_yaml


class RequestsUtil:
    session = requests.session()

    def send_request(self, method, url, data="", **kwargs):
        method = str(method).lower()
        base_url = read_yaml("/common/host_config_datas.yml")['host']
        if method == 'get':
            res = RequestsUtil.session.request(method=method, url=base_url + url, params=data, **kwargs)
            return res
        elif method == 'post':
            if type(data) == 'dict':
                res = RequestsUtil.session.request(method=method, url=base_url + url, json=data, **kwargs)
                return res
            else:
                res = RequestsUtil.session.request(method=method, url=base_url + url, data=data, **kwargs)
                return res
