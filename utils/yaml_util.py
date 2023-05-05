# -*- coding: UTF-8 -*-
import json
import os
import time

import pytest
import yaml

from common.data_handler import list_data_set_values, dict_data_set_values
from utils.log_util import LogUtil


def read_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='r', encoding='utf-8') as f:
        params = yaml.load(stream=f, Loader=yaml.FullLoader)  # 把数据转化为json格式
        # f = open(os.getcwd().split('utils')[0] + file_name, mode='r', encoding='utf-8')
        # params = yaml.safe_load(f)
        return params


def write_extract_yaml(data, file_name="/common/token.yml"):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=yaml.SafeDumper)
        LogUtil().set_log().info("缓存数据写入成功")


def clear_extract_yaml(file_name="/common/token.yml"):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='w', encoding='utf-8') as f:
        f.truncate()
        LogUtil().set_log().info("缓存数据清除成功")


# def read_variable_yaml(file_name):
#     datas = read_yaml(file_name)
#     if isinstance(datas, list):
#         datas = read_yaml(file_name)[0]
#     if isinstance(datas, dict):
#         for key, value in datas.items():
#             if isinstance(value, dict):
#                 dict_data_set_values(value)
#             elif isinstance(value, list):
#                 value = list_data_set_values(value)
#                 datas = datas.update(dict({key: value}))
#             else:
#                 datas = datas
#             if "{{" and "}}" in str(value):  # yaml文件中{{}}格式需要加引号
#                 start_index = str(value).index("{{")
#                 end_index = str(value).index("}}")
#                 fun_name = str(value)[start_index + 2:end_index]
#                 datas[key] = eval(fun_name)
#         return datas


def read_variable_yaml(file_name):
    datas = read_yaml(file_name)
    if isinstance(datas, list):
        datas = read_yaml(file_name)[0]
    if isinstance(datas, dict):
        for key, value in datas.items():
            if isinstance(value, dict):
                value = dict_data_set_values(value)
            elif isinstance(value, list):
                value = list_data_set_values(value)
            else:
                datas = datas
            if "{{" and "}}" in str(value):  # yaml文件中{{}}格式需要加引号
                start_index = str(value).index("{{")
                end_index = str(value).index("}}")
                fun_name = str(value)[start_index + 2:end_index]
                datas[key] = eval(fun_name)
        return datas


def get_token():
    token = read_yaml('/common/token.yml')['token']
    print(token)
    return token


if __name__ == '__main__':
    datas = read_variable_yaml('/test_activity/get_activity_datas.yml')
    print(type(datas))
