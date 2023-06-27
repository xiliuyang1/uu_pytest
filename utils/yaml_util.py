# -*- coding: UTF-8 -*-

import os
import random

import yaml
from utils.log_util import LogUtil


def read_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='r', encoding='utf-8') as f:
        params = yaml.load(stream=f, Loader=yaml.FullLoader)
        return params


def read_image_file(image_name):
    file = open(os.getcwd().split('utils')[0] + "/test_data/test_pictures/" + image_name, 'rb')
    return file


def read_extract_yaml(file_name="/common/extract_datas.yml"):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='r', encoding='utf-8') as f:
        params = yaml.load(stream=f, Loader=yaml.FullLoader)
        LogUtil().set_log().info("缓存数据读取成功{}".format(params))
        return params


def write_extract_yaml(data, file_name="/common/extract_datas.yml"):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, 'r', encoding='utf-8') as f:
        get_data = yaml.safe_load(f)
    if str(get_data) == 'None':
        with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, 'w',
                  encoding='utf-8') as f:
            yaml.safe_dump(data, f)
    else:
        for key, value in data.items():
            get_data[key] = value
            print(get_data)
        with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, 'w',
                  encoding='utf-8') as f:
            yaml.safe_dump(get_data, f)
    LogUtil().set_log().info("缓存数据写入成功{}".format(data))


def clear_extract_yaml(file_name="/common/token.yml"):
    with open(os.getcwd().split('utils')[0] + "/test_data" + file_name, mode='w', encoding='utf-8') as f:
        f.truncate()
    LogUtil().set_log().info("{}文件中的缓存数据清除成功".format(file_name))


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
    return datas


def list_data_set_values(datas):
    new_list = []
    for item in datas:
        if isinstance(item, dict):
            new_list.append(dict_data_set_values(item))
        elif isinstance(item, list):
            new_list.append(list_data_set_values(item))
        else:
            new_list.append(item)
    new_datas = new_list
    return new_datas


def token():
    token = read_extract_yaml('/common/token.yml')['token']
    return token


"""
random.randint(a,b) 方法，生成一个 a 与 b 之间的随机整数，也就是 (a,b)
random.randrange(a,b) 方法, 生成一个 a 与 b 之间的不包含 b 的随机整数， [a, b) ，
random.uniform(a, b) 方法， 生成 [a, b] 之间的随机浮点数

"""


def get_random_mobile():
    random_num = str(random.randint(1000, 9999))
    random_mobile = str(1883803) + random_num
    return random_mobile


def get_random_email():
    random_num = str(random.randint(1000, 9999))
    random_email = str(1883803) + random_num + "@163.com"
    return random_email


def get_random_int():
    return str(random.randint(10, 99))


if __name__ == '__main__':
    print(os.path.join(os.getcwd().split('utils')[0], "test_data", "/common/extract_datas.yml"))
