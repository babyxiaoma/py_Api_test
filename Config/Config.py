# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-21 16:01:17
# @File       :Config.py
# @Ide        :PyCharm

from Utils.File_Reader import ExcelReader
import os
import configparser
import datetime
import json


class Config(object):
    def __init__(self):
        '''
        初始化配置
        '''
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.config_path = os.path.join(self.base_path, 'Config')
        self.data_ini_path = os.path.join(self.config_path, 'config.ini')
        self.log_path = os.path.join(self.base_path, 'log')
        self.data_path = os.path.join(self.base_path, 'Data')
        self.report_path = os.path.join(self.base_path, 'Report', 'Api_Report.html')
        self.case_path = os.path.join(self.base_path, 'QP_Case')
        self.data = ExcelReader(self.data_path + '\\Test_Case1.xls').data
        self.Data_ini = os.path.join(self.data_path, 'Data.ini')

        self.config = configparser.ConfigParser()
        self.config.read(self.data_ini_path, encoding='utf-8')
        self.username = self.config.get('Login', 'username')
        self.password = self.config.get('Login', 'password')

        self.test_url = self.config.get('Api', 'test_url')

        self.log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.Log'
        self.log_file_name = self.log_path + '\\' + self.log_file

        self.file_name = self.config.get('Log', 'file_name')
        self.backup = self.config.get('Log', 'backup')
        self.console_level = self.config.get('Log', 'console_level')
        self.file_level = self.config.get('Log', 'file_level')
        self.pattern = self.config.get('Log', 'pattern')
        self.host = self.config.get('TESTDB', 'host')
        self.port = int(self.config.get('TESTDB', 'port'))
        self.user = self.config.get('TESTDB', 'user')
        self.dbpassword = self.config.get('TESTDB', 'passwd')
        self.db = self.config.get('TESTDB', 'db')
        self.server = self.config.get('email', 'server')
        self.sender = self.config.get('email', 'sender')
        self.empassword = self.config.get('email', 'password')
        self.receiver = self.config.get('email', 'receiver')

    # def check_data(self,data.ini):
    #     '''
    #     检查参数,转换成dict
    #     :param data.ini: 参数
    #     :return:
    #     '''
    #     if isinstance(data.ini,str):
    #         return json.loads(data.ini)


if __name__ == '__main__':
    c = Config()
    print(type(c.port))
