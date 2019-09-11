# -*- coding: utf-8 -*-
# !/usr/bin/python

# @Author     :xiao hei ma
# @Time       :2019-08-29 17:07:10
# @File       :main_case.py
# @Ide        :PyCharm

from Support.HTMLTestRunner import HTMLTestRunner
import unittest
from Config.Config import Config
from Utils.Mail import Email


def run(testname):
    '''集合所有用例运行发送报告'''
    c = Config()
    with open(c.report_path, 'wb') as f:
        suite = unittest.defaultTestLoader.discover(start_dir=c.case_path, pattern='Api_*.py')
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='API测试报告',
                                description='接口html测试报告',
                                tester=testname,
                                test_user=str(c.username))
        runner.run(suite)

    e = Email(server=c.server,
              sender=c.sender,
              password=c.empassword,
              receiver=c.receiver,
              title='老马发送的今天的API自动化报告又来了，请注意查看！',
              message='来了来了，你的测试API自动化报告!!，注意如果收不到邮件注意查看垃圾箱还是退信了！',
              path=[c.report_path, c.log_file_name]
              )
    e.send()


run('xiao hei ma')
