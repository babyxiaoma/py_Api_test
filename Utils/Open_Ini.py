# -*- coding: utf-8 -*-
#!/usr/bin/python

#@Author     :xiao hei ma
#@Time       :2019-09-17 15:22:40
#@File       :Open_Ini.py
#@Ide        :PyCharm

import configparser
from Config.config import Config
from Utils.Log import logger
import json

class OpenIni(object):
    def __init__(self):
        self.c = Config()

    def get_data(self, option):
        try:
            if option != '':
                c = configparser.ConfigParser()
                c.read(self.c.Data_ini, encoding='utf-8')
                data = c.get('data', option=option)
                return json.loads(data)
        except Exception:
            logger.error('节点id值: <{}> 错误,请检查!'.format(option))


if __name__ == '__main__':
    x = OpenIni()
    print(x.get_data('login_1'))
    print(type(x.get_data('login_1')))