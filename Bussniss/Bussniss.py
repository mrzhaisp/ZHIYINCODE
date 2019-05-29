#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.Commonlib import Commonlib
from Commonlib.Readxml import Readxml
from Commonlib.Loggin import LoggIn
import os
import datetime
import random

# 视频分类列表
videosourse = ["人工智能", "电子对抗", "下一代网络", "智能制造", "区块链", "其他"]

# 视频语言列表
langue = ["中文", "英语", "日语", "俄语", "法语", "德语", "越南语",
          "意大利语", "丹麦语", "汉语", "韩语", "瑞典语", "芬兰语",
          "波兰语", "荷兰语", "泰语", "阿拉伯语", "捷克语", "罗马尼亚语", "匈牙利语", "其他"]


class Bussniss:
    def __init__(self):
        self.c = Commonlib()
        self.r = Readxml()
        self.l = LoggIn()

    def LoadVideoType(self, base_url, username, password, filepath):
        """上传视频格式不符合要求的视频格式"""
        try:
            self.c.loadVideoLogIn(base_url, username, password)
            self.c.waite(2)
            self.c.activeEvent(".//*[contains(text(),'导入视频')]")
            self.c.waite(2)
            # 路径前面加上r处理路径下含U
            self.l.Logg("上传视频文件")
            self.c.activeEvent(".//body/descendant::input[1]")
            self.c.waite(2)
            # ---------:这里是要上传的是视频的路径
            # filepath = self.r.readxml("videofile", "d")
            # 非input标签，第三方工具制作上传文件的路径
            os.system(r"C:\Users\Test\upload.exe %s" % filepath)
            self.c.waite(2)
            t = self.c.tryText(".//body/div[2]/descendant::p")
            # print(t)
            self.l.Logg("拿到警告Alter弹框上文字")
            return t

        except Exception as e:
            self.l.Logg(e)
            raise e

    def LoadVideo(self):
        '''登录上传视频后台系统,并上传视频'''
        self.l.Logg("登录视频上传网站")
        try:
            self.c.loadVideoLogIn(self.r.readxml("baseurl", "loadvideoUrl"),
                                  self.r.readxml("loadvideologin", "username"),
                                  self.r.readxml("loadvideologin", "password"))
            self.c.waite(1)
            self.c.activeEvent(".//*[contains(text(),'导入视频')]")
            self.c.waite(1)
            # 路径前面加上r处理路径下含U
            self.l.Logg("上传视频文件")
            self.c.activeEvent(".//body/descendant::input[1]")
            self.c.waite(1)

            # ---------:这里是要上传的是视频的路径
            filepath = self.r.readxml("videofile", "d")

            # 非input标签，第三方工具制作上传文件的路径
            os.system(r"C:\Users\Test\upload.exe %s" % filepath)
            self.c.waite(2)

            # ---------:这里是要上传的是视频的路径  选择内网自编，还是外网资源<neiwwang>内网自编</neiwwang><waiwang>外网资源</waiwang>
            self.c.activeEvent(".//*[contains(text(),'%s')]" % self.r.readxml("shiplaiyuan", "waiwang"))
            self.c.waite(1)
            self.c.activeEvent(".//*[contains(text(),'频道分类')]/following-sibling::div/descendant::input")
            self.c.waite(1)

            # 随机选取一个栏目
            self.c.activeEvent(".//*[contains(text(),'%s')]" % random.choice(videosourse))
            print(random.choice(videosourse))
            self.c.waite(1)
            self.c.activeEvent(".//*[contains(text(),'语种')]/following-sibling::div/descendant::input")
            self.l.Logg("选择语言")
            self.c.waite(2)

            # ---------选择各种语言
            self.c.activeEvent(".//*[contains(text(),'%s')]" % random.choice(langue))
            print(random.choice(langue))
            self.c.waite(1)
            self.l.Logg("清除制作日期，重新输入当期日期")
            self.c.clearKeys(".//*[contains(text(),'制作日期')]/following-sibling::div/descendant::input")
            self.c.waite(1)
            self.c.inputKeys(".//*[contains(text(),'制作日期')]/following-sibling::div/descendant::input",
                             str(datetime.date.today()))
            self.c.waite(1)
            self.c.activeEvent(".//*[@class='video-import']")
            self.l.Logg("清除上传日期，重新输入当期日期")
            self.c.clearKeys(".//*[contains(text(),'上传日期')]/following-sibling::div/descendant::input")
            self.c.waite(1)
            self.c.inputKeys(".//*[contains(text(),'上传日期')]/following-sibling::div/descendant::input",
                             str(datetime.date.today()))
            self.c.activeEvent(".//*[@class='video-import']")
            self.l.Logg("输入内容摘要")
            self.c.inputKeys(".//*[contains(text(),'内容摘要')]/following-sibling::div/descendant::textarea",
                             "这是一个UI自动化测试的demo")
            self.c.waite(1)
            self.c.activeEvent(".//*[text()='导入']")
            self.c.waite(2)
            self.c.activeEvent(".//*[contains(text(),'查看处理过程')]")

        except Exception as e:
            raise

    def getLoginTitle(self, base_url, username, password):
        # web首页login的title
        try:
            self.c.uiLogIn(base_url, username, password)
            texttwo = self.c.getTitle()
            self.c.waite(2)
            self.l.Logg("web首页登录后Title为--->%s" % texttwo)
            return texttwo
        except Exception as e:
            self.l.Logg(e)
            raise e

    def AudioVideo(self, base_url, username, password):
        """音视频库下"""
        self.l.Logg("This class is AudioVideo")
        try:
            self.c.uiLogIn(base_url, username, password)
            self.c.waite(1)
            self.l.Logg("点击音视频库")
            self.c.activeEvent(".//body/div[1]/descendant::a[2]")
            self.c.waite(1)
            listtext = []

            shishiredian = self.c.tryText(".//body/div[1]/section/descendant::a[4]")
            listtext.append(shishiredian)
            self.l.Logg("拿到音视频下首页的第一个标签为—》%s" % shishiredian)

            neiwangzibian = self.c.tryText(".//body/div[1]/section/descendant::p[1]")
            listtext.append(neiwangzibian)
            self.l.Logg("拿到音视频下首页的第二个标签为—》%s" % neiwangzibian)

            waiwang = self.c.tryText(".//body/div[1]/section/descendant::p[2]")
            listtext.append(waiwang)
            self.l.Logg("拿到音视频下首页的第三个标签为—》%s" % waiwang)

            # print(type(listtext),listtext)
            return listtext
        except Exception as e:
            self.l.Logg(e)


    def ShiShiredian(self,url,username,password):
        try:
            textlist = []
            self.l.Logg("This class is shiShiredian")
            self.c.uiLogIn(url,username,password)
            self.c.waite(1)
            self.c.activeEvent(".//body/div[1]/section/descendant::a[4]")
            self.c.waite(1)
            #拿到第一个视频的标题
            textone = self.c.tryText(".//body/descendant::section/descendant::ul[5]/descendant::div[8]")
            # print("视频页标题为-----> %s"%textone )
            textlist.append(textone)
            self.c.waite(1)
            self.c.jsTopDown("500")
            self.c.waite(1)
            self.l.Logg("拿到时事热点第一条视频")
            self.c.activeEvent(".//body/div[1]/descendant::section/descendant::img[1]")
            self.c.waite(2)
            self.l.Logg("点击播放视频")
            self.c.activeEvent(".//body/descendant::video")
            self.c.waite(5)
            self.l.Logg("停止播放视频")
            self.c.activeEvent(".//body/descendant::video")
            texttwo = self.c.tryText(".//body/descendant::section/descendant::p[4]")
            # print("视频内标题为----->  %s"%texttwo)
            textlist.append(texttwo)
            self.c.waite(2)
            # print(textlist)
            return textlist

        except Exception as e:
            self.l.Logg(e)
            raise e

# b = Bussniss()
# b.ShiShiredian("http://10.168.103.151/web/#/login","admin","111111")
