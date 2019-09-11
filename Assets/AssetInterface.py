# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-30 15:52:32
# @File       :AssetInterface.py
# @Ide        :PyCharm

from Utils.Client import HTTPClient
from Config.Config import Config
import time
from Common.User_Token import login


def get_user_coin():
    '''
    获取用户信息余额
    :return:
    '''
    api_token = login()
    response = HTTPClient(Config().test_url + 'user/balance', 'get').send(data={'api_token': api_token})
    return response['data']['coin']


def get_sql_all(sql_value):
    '''
    根据传入的方法和字段数据返回出sql
    :param sql_value: excel上获取的value
    :return:
    '''
    # 格式化当前时间
    _time = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))

    id_name = sql_value.split('>')[0]
    field = sql_value.split('>')[1]
    id_value = sql_value.split('>')[2]
    if id_name == 'user_info':
        return '''select {} from gygy_members WHERE username = '{}';'''.format(field, Config().username)
    elif id_name == 'activity':
        return '''select {} from gygy_activity_apply WHERE apply_date = '{}' and activity_id = {}'''.format(field,
                                                                                                            _time,
                                                                                                            id_value)
    else:
        return None

# print(get_sql_all('activity>activity_id>49'))
# print('获取余额类型:',type(get_user_coin()))
