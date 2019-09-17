# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-29 15:24:12
# @File       :Api_test_case.py
# @Ide        :PyCharm

import sys
import os

sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
import unittest
from Config.config import Config
from Utils.Client import HTTPClient
from Utils.Log import logger
from Utils.Assertion import Error
from Utils.User_Token import login
from Utils.File_Reader import *
from Utils.Depends import Depend_Data
from Assets.AssetInterface import *
from Utils.Open_Ini import OpenIni


class QP_Api_Test(unittest.TestCase):
    c = Config()
    e = Error()
    datas = _data = ExcelReader(c.data_path + '\\Test_Case1.xls').data

    def test_api_all(self):
        '''主运行函数'''
        for i in self.datas:
            if i['is_run'].upper() == 'YES':
                with self.subTest(case=i['CaseName']):
                    url = self.c.test_url + i['api']
                    data_id = i['data']
                    method = i['method']
                    expect_code = i['expect_code']
                    expect_msg = i['expect_msg']
                    is_token = i['is_token']
                    data = OpenIni().get_data(data_id)
                    depend_id = i['depend_id']
                    query_depend = i['query_depend']
                    field_depend = i['field_depend']
                    sql_value = i['sql_value']
                    expect_data = i['expect_data']
                    is_coin = i['is_coin']
                    # 判断是否需要依赖数据,有则替换依赖数据
                    if depend_id:
                        #判断是否存在逗号,是则是至少有两个key以上,切割组成列表作为keys
                        if ',' in field_depend:
                            field_depend_list = field_depend.split(',')
                            depend = Depend_Data().get_depend_data(depend_id, query_depend, field_depend_list)
                            for key in field_depend_list:
                                #交換兩個字典的值
                                data[key] = depend[key]
                        else:
                            depend = Depend_Data().get_depend_data(depend_id, query_depend, field_depend)
                            data[field_depend] = depend
                    if is_token == 'YES' and data_id != '':
                        api_token = login()
                        data.update({'api_token': api_token})
                        response = HTTPClient(url=url, method=method).send(data=data)
                    elif is_token == 'NO' and data_id != '':
                        response = HTTPClient(url=url, method=method).send(data=data)
                    elif is_token == 'YES' and data_id == '':
                        api_token = login()
                        response = HTTPClient(url=url, method=method).send(data={'api_token': api_token})
                    else:
                        response = HTTPClient(url=url, method=method).send()
                    # 首先进行普通断言
                    self.e.assertHTTPCode(response, expect_code, expect_msg)
                    # 判断是否查询数据库断言
                    if sql_value:
                        if is_coin:
                            expect_data = get_user_coin()
                        self.e.assertMysqldata(sql=get_sql_all(sql_value), expect_data=expect_data)
            else:
                logger.warning('用例: <{}> 不执行!'.format(i['CaseName']))


if __name__ == '__main__':
    unittest.main()
