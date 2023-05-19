import jsonpath
import requests

from utils.log_util import my_logging
from utils.yaml_util import read_yaml, list_data_set_values, dict_data_set_values


class RequestsUtil:
    session = requests.session()

    def send_request(self, testcasename=None, method=None, url=None, data=None, headers=None, cookies=None, files=None,
                     auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None,
                     cert=None):
        method = str(method).lower()
        base_url = read_yaml("/common/host_config_datas.yml")['host']
        try:
            if method == 'get':
                res = RequestsUtil.session.request(method="get", url=base_url + url, params=data, headers=headers,
                                                   cookies=cookies, files=files, auth=auth, timeout=timeout,
                                                   allow_redirects=allow_redirects, proxies=proxies, hooks=hooks,
                                                   stream=stream, verify=verify, cert=cert)
            elif method == 'post':
                res = RequestsUtil.session.request(method="post", url=base_url + url, data=data, headers=headers,
                                                   cookies=cookies, files=files, auth=auth, timeout=timeout,
                                                   allow_redirects=allow_redirects, proxies=proxies, hooks=hooks,
                                                   stream=stream, verify=verify, cert=cert)
            if res.json()['status'] == 200:
                RequestsUtil().getresponsevalue(res, verify)
                my_logging.info("{}接口请求成功".format(testcasename))
                return res
            elif res.json()['status'] != 200:
                my_logging.warning("{}接口请求异常，响应体：{}".format(testcasename, res.json()))
                return res
        except Exception as e:
            print(e)

    def getresponsevalue(self, response, verify):
        if verify is not None:
            for key, value in verify:
                check_value = jsonpath.jsonpath(response.json(), key)
                if check_value == value:
                    my_logging.info("{}={}的断言成功".format(key, value))
        else:
            pass
