# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-30 13:19:58
# @File       :Depends.py
# @Ide        :PyCharm

from Config.config import Config
from Utils.Client import HTTPClient
from Utils.User_Token import login
from Utils.Open_Ini import OpenIni
from Utils.Log import logger
from Utils.JMESPath_Extractor import JMESPathExtractor
from Utils.File_Reader import ExcelReader



class Depend_Data(object):
    def __init__(self):
        self.c = Config()
        self.ini = OpenIni()
        self.j = JMESPathExtractor()

    def get_depend_data(self, case_id, query, keys):
        '''
         根据case_id,query获取到被依赖的值的dict
         :param case_id: CaseID   如:A08
         :param query: 被依赖的json查询列表，以‘,’号分开    如:data.id,data
         :param keys: 组装dict的key,如不是列表则传单个字符串
         :return:
        '''
        _data = ExcelReader(self.c.data_path + '\\Test_Case1.xls').data
        value_list = []
        for i in _data:
            if case_id == i['CaseID']:
                logger.info('执行依赖数据CaseID: <{}>'.format(case_id))
                logger.info('被依赖的json查询值: <{}>'.format(query))
                url = self.c.test_url + i['api']
                data_id = i['data']
                method = i['method']
                is_token = i['is_token']
                data = self.ini.get_data(data_id)
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
                # 判断有','存在说明至少有两个查询值,否则只有一个值
                if ',' in query:
                    query_list = query.split(',')
                    # 循环查询值组成list
                    for key in query_list:
                        value = self.j.extract(key, response)
                        value_list.append(value)
                else:
                    return self.j.extract(query, response)
        # 根据keys_list与获取到的依赖值组装成dict并返回
        value_data = dict(zip(keys, value_list))
        return value_data


if __name__ == '__main__':
    test = Depend_Data()
    keys = 'id,rule_id'

    print(test.get_depend_data('A116', 'data[0].id,data[0].rule[0].id', keys))
