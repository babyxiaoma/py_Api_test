# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-30 14:35:25
# @File       :Read_DB.py
# @Ide        :PyCharm

import pymysql
from Config.Config import Config
from decimal import *
from Assets.AssetInterface import *


class DButil(object):
    def __init__(self):
        '''数据库配置'''
        self.c = Config()
        self.host = self.c.host
        self.port = self.c.port
        self.user = self.c.user
        self.passwd = self.c.dbpassword
        self.db = self.c.db
        self.DB = pymysql.connect(
            host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db
        )

    def query(self, sql):
        '''
        获取查询数据的字段
        :param sql: 查询的sql
        :return:
        '''
        try:
            cursor = self.DB.cursor()
            cursor.execute(sql)
            datas = cursor.fetchone()
            cursor.close()
            self.DB.close()
            # 判断类型不是str,int就为Decimal,转换Decimal为str保留4位小数
            if type(datas[0]) not in [str, int]:
                return str(Decimal(datas[0]).quantize(Decimal('0.0000')))
            # 判断不是str,都强转为str
            elif type(datas[0]) not in [str]:
                return str(datas[0])
            else:
                return datas[0]
        except Exception:
            pass


if __name__ == '__main__':
    db_util = DButil()
    sql = get_sql_all('user_info>coin>')
    print(type(db_util.query(sql)))
