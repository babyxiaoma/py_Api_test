# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-21 18:34:32
# @File       :User_Token.py
# @Ide        :PyCharm

from Utils.Client import HTTPClient
from Config.Config import Config
from Utils.Log import logger


def login():
    c = Config()
    username = c.username
    password = c.password
    try:
        url = c.test_url + 'pub/login'
        response = HTTPClient(url, 'post').send(data={'username': username, 'password': password})
        api_token = response['data']
        return api_token
    except Exception as e:
        logger.error('获取api_token失败!  {}'.format(e))
