import json
import logging
import os
import time


class LogUtil:

    def __init__(self, level="DEBUG"):
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(level)

    def console_handler(self, level='DEBUG'):
        con_handler = logging.StreamHandler()
        # 给日志器设置等级：
        con_handler.setLevel(level)
        # 给处理器添加格式器:
        con_handler.setFormatter(self.set_formatter()[0])
        return con_handler
        # 给到一个控制台处理器

    def file_handler(self, level='DEBUG'):
        file_handler = logging.FileHandler(
            os.getcwd().split("utils")[0] + "/logger/{}.txt".format(
                time.strftime('%Y-%m-%d', time.localtime(time.time()))),
            mode='a', encoding="utf-8")
        # 给文件处理器设置等级：
        file_handler.setLevel(level)
        # 给文件处理器添加格式器：
        file_handler.setFormatter(self.set_formatter()[1])
        # return出文件处理器：
        return file_handler

    def set_formatter(self):
        console_fmt = logging.Formatter(
            fmt="%(asctime)s [%(filename)s:%(lineno)d] [%(funcName)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d-%H:%M:%S")
        file_fmt = logging.Formatter(
            fmt="%(asctime)s [%(filename)s:%(lineno)d] [%(funcName)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d-%H:%M:%S")
        return console_fmt, file_fmt
        # 给到两个日志的格式器

    def set_log(self):
        # 给日志器添加处理器：
        self.logger.addHandler(self.file_handler())
        self.logger.addHandler(self.console_handler())
        return self.logger
