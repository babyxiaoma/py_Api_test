# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 日志类
# @File    : Log.py
# @Software: PyCharm

import logging
from Config.config import Config
from logging.handlers import TimedRotatingFileHandler


class Logger(object):
    def __init__(self, logger_name='Auto_frame'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        # 引入配置文件log
        c = Config()
        # 日志文件名
        self.log_file_name = c.log_file_name  # 日志名
        self.backup_count = c.backup  # 保留日志数量
        # 日志输出级别
        self.console_output_level = c.console_level
        self.file_output_level = c.file_level
        # 日志输出格式
        self.formatter = c.pattern if c and c.pattern else logging.Formatter(
            '%(asctime)s -- %(name)s -- %(filename)s -- %(lineno)d -- %(levelname)s -- %(message)s')

    def get_logger(self):
        '''在logger添加日志句柄并返回,如果logger已有句柄,则直接返回'''
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志,最多保留self.backup_count 份
            file_handler = TimedRotatingFileHandler(filename=self.log_file_name,
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

    '''
    日志等级（level）	描述
    DEBUG	最详细的日志信息，典型应用场景是 问题诊断
    INFO	信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
    WARNING	当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
    ERROR	由于一个更严重的问题导致某些功能不能正常运行时记录的信息
    CRITICAL	当发生严重错误，导致应用程序不能继续运行时记录的信息
    '''


# 调用logger即可写入日志
logger = Logger().get_logger()

if __name__ == '__main__':
    log = Logger()
    print(log.logger.info('thi is a info!'))
