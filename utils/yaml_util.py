# -*- coding: UTF-8 -*-
import os
import time

import pytest
import yaml


def read_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + file_name, mode='r', encoding='utf-8') as f:
        params = yaml.load(stream=f, Loader=yaml.FullLoader)  # 把数据转化为json格式
        # print(params)
        return params


def write_extract_yaml(file_name, data):
    with open(os.getcwd().split('utils')[0] + file_name, mode='w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=yaml.SafeDumper)


def clear_extract_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + file_name, mode='w', encoding='utf-8') as f:
        f.truncate()


if __name__ == '__main__':
    pytest.main(['-vs'])
