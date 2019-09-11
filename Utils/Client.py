# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : HTTP请求类
# @File    : Client.py
# @Software: PyCharm

import requests
from Utils.Log import logger

# 接口方法
METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    """当传入的method的参数不是支持的类型时抛出此异常。"""
    pass


class HTTPClient(object):
    def __init__(self, url, method='GET', headers=None, cookies=None):
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持method:{0},请检查传参!'.format(self.method))

    def send(self, data=None):
        '''发送请求方法,目前暂时写死GET,POST,请求方法'''
        if self.method == 'POST':
            response = requests.post(url=self.url, data=data).json()
            logger.info('请求url {}'.format(self.url))
            logger.info('请求响应内容 {}'.format(response))
        else:
            response = requests.get(url=self.url, params=data).json()
            logger.info('请求url {}'.format(self.url))
            logger.info('请求响应内容 {}'.format(response))
        return response


if __name__ == '__main__':
    url = 'http://api.test.by-998.com/user/info'
    data = {
        "api_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjY1MjUzMjAsImV4cCI6MTU2NjU2ODUyMCwiaXNzIjoiYm9uZyIsInN1YiI6ODQ3Mn0.Obo6DPlI6gN4EJ9y2GiuRMDifl8lNB5wCn8zA3cbJtc"}

    # print(url,data.ini)
    h = HTTPClient(url=url, method='get').send(data=data)
    print(h)
