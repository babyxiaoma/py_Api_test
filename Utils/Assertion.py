# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-22 16:31:15
# @File       :Assertion.py
# @Ide        :PyCharm

from Utils.Log import logger
from Utils.Read_DB import DButil


class Error(object):
    '''
    断言类
    '''

    def assertHTTPCode(self, response, expect_code, expect_msg=None):
        '''
        判断返回的code与预期code一致
        :param res_code:返回响应code
        :param code_list:预期codelist
        :return:
        '''
        if isinstance(expect_code, str):
            expect_code = int(expect_code)
        # 判断code
        if expect_code != response['code']:
            logger.error(
                '预期结果不在实际结果中!,预期结果: <{}>,实际响应code: <{}>,实际响应结果: <{}>'.format(expect_code, response['code'], response))
            raise AssertionError(
                '预期结果不在实际结果中!,预期结果: <{}>,实际响应code: <{}>,实际响应结果: <{}>'.format(expect_code, response['code'], response))
        # 判断msg
        if expect_msg != None:
            if expect_msg not in response['msg']:
                logger.error(
                    '预期结果不在实际结果中!,预期结果: <{}>,实际响应msg: <{}>,实际响应结果: <{}>'.format(expect_msg, response['msg'], response))
                raise AssertionError(
                    '预期结果不在实际结果中!,预期结果: <{}>,实际响应msg: <{}>,实际响应结果: <{}>'.format(expect_msg, response['msg'], response))
        # 判断data
        if 'data' in response:
            if response['data'] == '':
                logger.error(
                    '实际结果数据为空!,实际响应结果: <{}>'.format(response))
                raise AssertionError(
                    '实际结果数据为空!,实际响应结果: <{}>'.format(response))


    def assertMysqldata(self, sql, expect_data):
        '''
        对比sql结果和预期结果
        :param sql: sql语句
        :param expect_data: 预期结果
        :return:
        '''
        sql_data = DButil().query(sql)
        if sql_data != expect_data:
            logger.error(
                '数据库查询数据与预期结果不一致!数据库结果: <{}> type: {},预期结果: <{}> type: {}'.format(sql_data, type(sql_data), expect_data,
                                                                                  type(expect_data)))
            raise ValueError(
                '数据库查询数据与预期结果不一致!数据库结果: <{}> type: {},预期结果: <{}> type: {}'.format(sql_data, type(sql_data), expect_data,
                                                                                  type(expect_data)))
