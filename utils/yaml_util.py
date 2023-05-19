# -*- coding: UTF-8 -*-

import os
import yaml
from utils.log_util import LogUtil


def read_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='r', encoding='utf-8') as f:
        params = yaml.load(stream=f, Loader=yaml.FullLoader)
        return params


def read_extract_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='r', encoding='utf-8') as f:
        params = yaml.load(stream=f, Loader=yaml.FullLoader)
        # LogUtil().set_log().info("缓存数据读取成功{}".format(params))
        return params


def write_extract_yaml(data, file_name="/common/token.yml"):
    with open(os.getcwd().split('utils')[0] + "/test_data" + str(file_name), mode='w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=yaml.SafeDumper)
    LogUtil().set_log().info("缓存数据写入成功{}".format(data))


def clear_extract_yaml(file_name="/common/token.yml"):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='w', encoding='utf-8') as f:
        f.truncate()
    # LogUtil().set_log().info("缓存数据清除成功")


def read_variable_yaml(datas):
    if isinstance(datas, list):
        return list_data_set_values(datas)
    if isinstance(datas, dict):
        return dict_data_set_values(datas)
    else:
        return datas


def dict_data_set_values(datas):
    for key in datas.keys():
        value = datas.get(key)
        if isinstance(value, dict):
            new_value = dict_data_set_values(value)
            datas.update(dict({key: new_value}))
        elif isinstance(value, list):
            new_value = list_data_set_values(value)
            datas.update(dict({key: new_value}))
        else:
            if "{{" and "}}" in str(value):  # yaml文件中{{}}格式需要加引号
                start_index = str(value).index("{{")
                end_index = str(value).index("}}")
                fun_name = str(value)[start_index + 2:end_index]
                datas.update(dict({key: eval(fun_name)}))
            else:
                continue
    # print(datas)
    return datas


def list_data_set_values(datas):
    new_list = []
    for item in datas:
        if isinstance(item, dict):
            dict_data_set_values(item)
        elif isinstance(item, list):
            new_list.append(list_data_set_values(item))
        else:
            new_list.append(item)
    new_datas = new_list
    return new_datas


def token():
    token = read_extract_yaml('/common/token.yml')['token']
    return token


if __name__ == '__main__':
    # datas = read_variable_yaml('/test_activity/get_activity_base_datas.yml')
    datas = read_yaml('/test_task/task_datas.yml')
    # datas = read_yaml('/common/token.yml')
    print(datas)
