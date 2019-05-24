#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'test_zhai_sp@126.com'
receiver = ['test_zhai_sp@126.com','2686852189@qq.com',]
smtpserver = 'smtp.126.com'
username = 'test_zhai_sp@126.com'
#注意 这里是授权码 不是密码
password = '2017shixiaoyu'
mail_title = '主题：声像情报融合分析平台UI自动化测试报告'


class SendEmail():
    def sendEmail(self,filepath):

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ','.join(receiver)
        message['Subject'] = Header(mail_title, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('声像情报融合分析平台UI自动化测试报告', 'plain', 'utf-8'))

        # # 构造附件1（附件为TXT格式的文本）
        # att1 = MIMEText(open('../Reporter/151test_UI_report.htm', 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # att1["Content-Disposition"] = 'attachment; filename="151test_UI_report.htm"'
        # message.attach(att1)
        #
        # # 构造附件2（附件为JPG格式的图片）
        # att2 = MIMEText(open('123.jpg', 'rb').read(), 'base64', 'utf-8')
        # att2["Content-Type"] = 'application/octet-stream'
        # att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
        # message.attach(att2)

        # 构造附件3（附件为HTML格式的网页）
        att3 = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="151_selenium_UI_report.htm"'
        message.attach(att3)

        smtpObj = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
        smtpObj.connect(smtpserver)
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功！！！")
        smtpObj.quit()
#
# s = SendEmail()
# s.sendEmail("../Reporter/151_selenium_UI_report.htm")







