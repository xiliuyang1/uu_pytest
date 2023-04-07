import os
import time

import yaml


def read_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + file_name, mode='r', encoding='utf-8') as f:
        params = yaml.load(stream=f, Loader=yaml.FullLoader)
        # print(params)
        return params


def write_extract_yaml(file_name, data):
    with open(os.getcwd().split('utils')[0] + file_name, mode='w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=yaml.SafeDumper)


def clear_extract_yaml(file_name):
    with open(os.getcwd().split('utils')[0] + file_name, mode='w', encoding='utf-8') as f:
        f.truncate()


if __name__ == '__main__':
    print(read_yaml('/test_data/test_login_datas.yml')[0]['datas'])
    print(read_yaml("/config/host_config.yml"))
    clear_extract_yaml('/test_data/extract_data.yml')
    print(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())))
