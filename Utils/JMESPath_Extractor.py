# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-30 13:54:17
# @File       :JMESPath_Extractor.py
# @Ide        :PyCharm

import json
import jmespath
from Utils.Log import logger


class JMESPathExtractor(object):
    '''
    用JMESPath实现的抽取器，对于json格式数据实现简单方式的抽取
    '''

    def extract(self, query, body):
        try:
            if isinstance(body, str):
                body = json.loads(body)
            return jmespath.search(expression=query, data=body)
        except Exception as e:
            logger.error('无效查询: {}'.format(query), str(e))
            raise ValueError('无效查询: {}'.format(query), str(e))


if __name__ == '__main__':
    # from Utils.Client import HTTPClient
    # url = 'http://api.test.by-998.com/activity/index'
    # data = {'api_token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjcxNzAyNTEsImV4cCI6MTU2NzIxMzQ1MSwiaXNzIjoiYm9uZyIsInN1YiI6OH0.rud3aFryEI7Z94_3O9Z85-VZ9vUTX2n5ISS85KwK_nc'}
    # res = HTTPClient(url,'get').send(data=data)
    # print(res)

    data = [
        {
            "day": 1,
            "status": 1,
            "is_today": 1,
            "Activity_id": 49,
            "mb_icon": "http://static.cdn.etzg123.com/bankIcon/5c2474943bb9f.png",
            "pc_icon": "http://static.cdn.etzg123.com/bankIcon/5c18e1c0d685f.png"
        },
        {
            "day": 2,
            "status": 0,
            "is_today": 0,
            "Activity_id": 49,
            "mb_icon": "http://static.cdn.etzg123.com/bankIcon/5c2474943bb9f.png",
            "pc_icon": "http://static.cdn.etzg123.com/bankIcon/5c18e1c0d685f.png"
        }
    ]
    j = JMESPathExtractor()
    msg = j.extract('data', data)
    # id = j.extract("data.id",data)
    print(msg)
    # print(type(id))
