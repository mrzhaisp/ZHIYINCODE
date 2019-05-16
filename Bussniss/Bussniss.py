#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.Commonlib import Commonlib
from Public.Public import PubLic
from Commonlib.Readxml import Readxml
from Commonlib.Loggin import LoggIn
class Bussniss:

    def __init__(self):
        self.p = PubLic()
        self.r = Readxml()
        self.l = LoggIn()

    def LoadVideo(self):
        #登录上传视频后台系统
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
            self.p.pub.inputKeys(".//body/descendant::input[1]",r"C:\Users\Test\上传视频\人工智能的机器人.mp4")
            self.p.pub.waite(2)
            self.l.Logg("导入视频")
            self.p.pub.activeEvent(".//body/descendant::button[6]")
            # self.p.pub.waite(2)
            # self.l.Logg("输入栏目为内网自编")
            # self.p.pub.activeEvent(".//*[contains(text(),'内网自编')]")
            # self.p.pub.waite(2)
            # self.l.Logg("选择频道分类")
            # self.p.pub.activeEvent(".//*[contains(text(),'频道分类')]/following::div[1]/descendant::input")

        except Exception as e:
            raise e

b = Bussniss()
b.LoadVideo()


