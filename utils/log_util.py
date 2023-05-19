import json
import logging
import os
import time
import colorlog

"""
ColoredFormatter类带着一些参数：

 format：用于输出日志的格式化字符串（必需）
 datefmt：一个传递给基类的可选的日期格式。见logging.Formatter
 reset：隐性的添加一个颜色重置代码到消息输出，除非输出已经结束。默认为True
 log_colors：记录级别名称到颜色名称的一个映射。可以在colorlog.default_log_colors或下面的例子中找到默认值
 secondary_log_colors：颜色名称到log_colors样式映射的映射，可以在格式化字符串中使用其定义的其他颜色。 请参考下面的示例
 style：可以向格式化字符串中添加参数，给不同的日志信息显示不同的颜色
 
 log_color：返回与日志级别关联的颜色
 <name>_log_color：如果格式化中配置了辅助颜色，则根据日志级别返回另一种颜色（请参考下面的secondary_log_colors）
 在为日志级别配置颜色时，可以使用逗号连接多个转义码（但不能直接在格式字符串中使用）。 例如，black，bg_white将在白色背景上使用转义码表示黑色文本

下面是格式化字符串中可用的：

 {color}，fg_ {color}，bg_ {color}：前景色和背景色
 bold，bold_{color}，fg_bold_{color}，bg_bold_{color}：粗体/明亮的颜色
 reset：清除所有的格式（包括前景色和背景色）
可用的颜色名字是： black, red, green, yellow, blue, purple, cyan and white
"""


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
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
        console_fmt = colorlog.ColoredFormatter(
            fmt="%(log_color)s%(asctime)s [%(filename)s:%(lineno)d] [%(funcName)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d-%H:%M:%S", log_colors=log_colors_config, secondary_log_colors={},
            style='%')
        # 控制台不同的日志等级显示不同的日志颜色

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


my_logging = LogUtil().set_log()
if __name__ == '__main__':
    print(111)
