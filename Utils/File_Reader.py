# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 读取配置文件类
# @File    : File_Reader.py
# @Software: PyCharm

import os
import xlrd
import configparser
from Config.Config import Config
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


class SheetTypeError(Exception):
    '''自定义一个异常类,接收传入sheettype异常'''
    pass


class ExcelReader(object):
    """
    读取excel文件中的内容。返回list。

    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data.ini)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data.ini)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """

    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileExistsError('文件不存在!')
        self.sheet = sheet
        self.title_line = title_line
        self._data = []
        self.s = self.openexcel()

    def openexcel(self):
        workbook = xlrd.open_workbook(self.excel)
        # 判断self.sheet类型是否为int or str
        if type(self.sheet) not in [int, str]:
            raise SheetTypeError('请输入<type:int>或者<type:str>'.format(type(self.sheet)))
        elif type(self.sheet) == int:
            s = workbook.sheet_by_index(self.sheet)
        else:
            s = workbook.sheet_by_name(self.sheet)
        return s

    @property
    def data(self):
        # 判断没有self._data执行,否则直接返回self._data
        if not self._data:
            # 如果self.title_line为True,则组成dict,否则组成list
            if self.title_line:
                keys = self.s.row_values(0)  # 首行为title
                for col in range(1, self.s.nrows):
                    # 依次遍历其余行,与首行组成dict,拼到self._data中
                    values = self.s.row_values(col)
                    self._data.append(dict(zip(keys, values)))
            else:
                for col in range(0, self.s.nrows):
                    self._data.append(self.s.row_values(col))
        return self._data


if __name__ == '__main__':
    from Config.Config import Config
    import json

    x = ExcelReader(Config().data_path + '\\Test_Case.xls')
    print(x)
