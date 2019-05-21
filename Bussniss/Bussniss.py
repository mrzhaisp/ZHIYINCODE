#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.Commonlib import Commonlib
from Public.Public import PubLic
from Commonlib.Readxml import Readxml
from Commonlib.Loggin import LoggIn
import os
import datetime

class Bussniss:

    def __init__(self):
        self.p = PubLic()
        self.r = Readxml()
        self.l = LoggIn()

    def LoadVideo(self):
        '''登录上传视频后台系统,并上传视频'''
        self.l.Logg("登录视频上传网站")
        try:
            self.p.login_load_video( self.r.readxml("baseurl","loadvideoUrl"),
                                     self.r.readxml("loadvideologin","username"),
                                     self.r.readxml("loadvideologin","password"))
            self.p.pub.waite(1)
            self.p.pub.activeEvent(".//*[contains(text(),'导入视频')]")
            self.p.pub.waite(2)
            #路径前面加上r处理路径下含U
            self.l.Logg("上传视频文件")
            self.p.pub.activeEvent(".//body/descendant::input[1]")
            self.p.pub.waite(2)
            filepath = self.r.readxml("videofile","a")
            # filepath = r"C:\Users\Test\上传视频\2019--0521--Autoit-selenium-test.mp4"
            #非input标签，第三方工具制作上传文件的路径
            os.system(r"C:\Users\Test\upload.exe %s"%filepath)
            self.p.pub.waite(2)
            self.p.pub.activeEvent(".//*[contains(text(),'外网资源')]")
            self.p.pub.waite(1)
            self.p.pub.activeEvent(".//*[contains(text(),'频道分类')]/following-sibling::div/descendant::input")
            self.p.pub.waite(1)
            self.p.pub.activeEvent(".//*[contains(text(),'电子对抗')]")
            self.l.Logg("选择自编网站的央企")
            self.p.pub.activeEvent(".//*[contains(text(),'语种')]/following-sibling::div/descendant::input")
            self.l.Logg("选择语言")
            self.p.pub.waite(1)
            self.p.pub.activeEvent(".//*[contains(text(),'英语')]")
            self.p.pub.waite(1)
            self.l.Logg("清除制作日期，重新输入当期日期")
            self.p.pub.clearKeys(".//*[contains(text(),'制作日期')]/following-sibling::div/descendant::input")
            self.p.pub.waite(1)
            self.p.pub.inputKeys(".//*[contains(text(),'制作日期')]/following-sibling::div/descendant::input",str(datetime.date.today()))
            self.p.pub.waite(1)
            self.p.pub.activeEvent(".//*[@class='video-import']")
            self.l.Logg("清除上传日期，重新输入当期日期")
            self.p.pub.clearKeys(".//*[contains(text(),'上传日期')]/following-sibling::div/descendant::input")
            self.p.pub.waite(1)
            self.p.pub.inputKeys(".//*[contains(text(),'上传日期')]/following-sibling::div/descendant::input",str(datetime.date.today()))
            self.p.pub.activeEvent(".//*[@class='video-import']")
            self.l.Logg("输入内容摘要")
            self.p.pub.inputKeys(".//*[contains(text(),'内容摘要')]/following-sibling::div/descendant::textarea","这是一个测试自动化的demo")
            self.p.pub.waite(1)
            self.p.pub.activeEvent(".//*[text()='导入']")
            self.p.pub.waite(2)
            #刷新页面，取出弹窗
            self.p.pub.reFresh()

        except Exception as e:
            raise e



b = Bussniss()
b.LoadVideo()



























