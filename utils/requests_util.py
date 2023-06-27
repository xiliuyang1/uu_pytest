import allure
import jsonpath
import pytest
import requests

from utils.log_util import my_logging
from utils.yaml_util import read_yaml


class RequestsUtil:
    session = requests.session()

    def send_request(self, testcasename=None, method=None, url=None, data=None, headers=None, cookies=None, files=None,
                     auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None,
                     cert=None):
        method = str(method).lower()
        base_url = read_yaml("/common/host_config_datas.yml")['host']
        # try:
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
            my_logging.info("【{}】接口请求成功{}".format(testcasename, res.json()))
            RequestsUtil().set_verify_result(res, verify, testcasename=testcasename)
            return res
        elif res.json()['status'] != 200:
            # assert res.json()['status'] == 200
            my_logging.error("【{}】接口请求异常，响应体：{}".format(testcasename, res.json()))
            RequestsUtil().set_verify_result(res, verify, testcasename=testcasename)
            return res
        # except Exception as e:
        #     my_logging.error(e)

    def set_verify_result(self, res=None, verify=None, testcasename=None):
        if verify is None:
            pass
        if verify is not None:
            for validateitem in verify:
                for key in validateitem.keys():
                    # 获取断言的预期结果：
                    validatelist = validateitem[key]
                    if isinstance(validatelist, dict):
                        for verify_key, verify_value in validatelist.items():
                            # 获取响应数据中各字段的实际响应值：（json提取器）
                            result_value = jsonpath.jsonpath(res.json(), verify_key)
                            if not result_value:
                                pytest.assume(False)
                                my_logging.error(
                                    "【" + testcasename + "】接口断言失败，响应数据中未查询到断言对象。响应结果为：" + res.json())
                                allure.dynamic.description(
                                    "【" + testcasename + "】接口断言失败，响应数据中未查询到断言对象。响应结果为：" + res.json())
                                continue
                            if result_value is not None and result_value != "":
                                if key.upper() == "EQ":
                                    if pytest.assume(str(result_value[0]) == str(verify_value)):
                                        my_logging.info("【" + testcasename + "】接口，断言：" + str(verify_key) + "=" + str(
                                            verify_value) + "，断言成功")
                                    else:
                                        my_logging.error("【" + testcasename + "】接口，断言：" + str(verify_key) + "=" + str(
                                            verify_value) + "，断言失败。实际值为：" + str(result_value[0]))
                                        allure.dynamic.description(
                                            "【" + testcasename + "】接口，断言：" + str(verify_key) + "=" + str(
                                                verify_value) + "，断言失败。实际值为：" + str(result_value[0]))
                                        continue
                                elif key.upper() == "CONTAIN":
                                    if str(result_value[0]).find(verify_value) == -1:
                                        pytest.assume(False)
                                        my_logging.error(
                                            "【" + testcasename + "】接口，断言：" + str(verify_key) + "字段中包含" + str(
                                                verify_value) + "，断言失败。实际值为：" + str(result_value[0]))
                                        allure.dynamic.description(
                                            "【" + testcasename + "】接口，断言：" + str(verify_key) + "字段中包含" + str(
                                                verify_value) + "，断言失败。实际值为：" + str(result_value[0]))
                                        continue
                                    else:
                                        pytest.assume(True)
                                        my_logging.info(
                                            "【" + testcasename + "】接口，断言：" + str(verify_key) + "字段中包含" + str(
                                                verify_value) + "，断言成功。实际值为：" + str(result_value[0]))
                                elif key.upper() == "NOT NULL":
                                    if len(str(result_value[0])) > 0:
                                        pytest.assume(True)
                                        my_logging.info("【" + testcasename + "】接口，响应数据中字段【" + str(
                                            verify_key) + "】非空，断言成功。实际值为：" + str(
                                            result_value[0]))
                                    else:
                                        pytest.assume(False)
                                        my_logging.error("【" + testcasename + "】接口，响应数据中字段【" + str(
                                            verify_key) + "】为空，断言失败。实际值为：" + str(
                                            result_value[0]))
                                        allure.dynamic.description("【" + testcasename + "】接口，响应数据中字段【" + str(
                                            verify_key) + "】为空，断言失败。实际值为：" + str(
                                            result_value[0]))
                                        continue
                            else:
                                pytest.assume(False)
                                my_logging.error(
                                    "【" + testcasename + "】接口，断言：" + str(verify_key) + "，断言失败。响应数据为：" + str(
                                        res.json()))
                                allure.dynamic.description(
                                    "【" + testcasename + "】接口，断言：" + str(verify_key) + "，断言失败。响应数据为：" + str(
                                        res.json()))


if __name__ == '__main__':
    print(len('1111111'))
