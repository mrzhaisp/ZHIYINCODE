#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import time
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
#
# class SendEmail:
#
#     def sendmail(self,file_new):
#         mail_from = "test_zhai_sp@126.com"
#         main_to = "2686852189@qq.com"
#         f = open(file_new,'rb')
#         mail_body = f.read()
#         f.close()
#         msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
#         msg['Subject'] = u'151Test声像情报融合分析平台UI自动化测试报告'
#         msg['data'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
#         smtp = smtplib.SMTP()
#         smtp.connect("smtp.126.com")
#         smtp.login("test_zhai_sp@126.com","2017shixiaoyu")
#         smtp.sendmail(mail_from,main_to,msg.as_string())
#         smtp.quit()
#         print("邮件发送完毕")
#
# if __name__ == '__main__':
#     s = SendEmail()
#     s.sendmail("../Reporter/151test_UI_report.htm")
#
# test_zhai_sp@126.com
# shixiaoyu2017
# 授权码  2017shixiaoyu


import os ,time,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def sentmail(file_new):
    #发信邮箱
    mail_from='test_zhai_sp@126.com'
    #收信邮箱
    mail_to='2686852189@qq.com'
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"私有云测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.126.com')
    #这里是授权码 不是密码  不是密码。。。
    smtp.login('test_zhai_sp@126.com','2017shixiaoyu')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print ('email has send out !')

sentmail("../Reporter/151test_UI_report.htm")

