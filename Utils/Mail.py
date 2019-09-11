# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 邮件类
# @File    : Mail.py
# @Software: PyCharm

import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from Utils.Log import logger


class Email(object):
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        '''
        初始化Email
        :param server:smtp服务器,必填
        :param sender:发件人,必填
        :param password:发件人密码,必填
        :param receiver:收件人,多收件人以";"隔开,必填
        :param title:邮件标题,必填
        :param message:邮件正文,非必填
        :param path:附件路径，可传入list（多附件）或str（单个附件），非必填.
        '''
        self.server = server
        self.sender = sender
        self.password = password

        self.receiver = receiver
        self.title = title
        self.message = message
        self.path = path
        self.msg = MIMEMultipart('related')

    def _attach_file(self, att_file):
        att = MIMEText(open(att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title  # 标题
        self.msg['From'] = self.server  #发送服务
        self.msg['To'] = self.receiver  # 收件人

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.path:
            if isinstance(self.path, list):
                for f in self.path:
                    self._attach_file(f)
            elif isinstance(self.path, str):
                self._attach_file(self.path)

        # 连接服务器发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接服务器
        except (gaierror and error) as e:
            logger.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s' % e)
        else:
            try:
                smtp_server.login(self.sender, self.password)  # 登录
            except smtplib.SMTPAuthenticationError as e:
                logger.exception('用户名密码验证失败.%s' % e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
            finally:
                smtp_server.quit()  # 断开连接
                logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))


'''
执行完成之后可以看到receiver收到了我们的报告。当然，在这块你有可能遇到很多问题，可以根据错误号去网上查询[如网易帮助](http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html)。一般有几种常见的错误：

1. 账户密码出错
2. 服务器sever出错，这个可以根据你的发送人的邮箱去网站或邮箱设置中查看到
3. 邮箱没有开通smtp服务，一般在邮箱设置中
4. 邮件被拦截，在title、message以及发送的文件中不要带明显乱码、广告倾向的字符
5. sender跟loginuser不一致的问题，发送人必须是登录用户
'''
