from utils.yaml_util import read_yaml


def get_token():
    token = read_yaml('/common/token.yml')['token']
    print(token)
    return token