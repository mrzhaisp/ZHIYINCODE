#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.Commonlib import Commonlib
from Public.Public import PubLic
import sys
class Bussniss:
    u"""所有的测试业务都在这里"""
    def __init__(self):
        self.pu = PubLic()

    def login_action_header(self,username,password):
        u"""登录首页拿到页眉'--  声像情报融合分析平台'"""
        self.pu.lo.Logg("This classname is login_action_header")
        try:
            self.pu.login_pub(username,password)
            text_login = self.pu.pub.tryText(".//head/following-sibling::body/descendant::a[1]")
            self.pu.lo.Logg('测试案例admin登录首页为%s'%(text_login))
            return text_login
        except Exception as e:
            self.pu.lo.Logg(e)
            raise

    def login_audio_video(self,username,password):
        u"""拿到音视频库模块 -----  音视频库"""
        self.pu.lo.Logg("This classname is login_audio_video")
        try:
            self.pu.login_pub(username,password)
            # self.pu.pub.activeEvent(u".//*[@id='app']/descendant::a[2]")
            text_audio_video = self.pu.pub.tryText(".//body/descendant::p[5]")
            self.pu.lo.Logg("测试案例为点击到音视频库后页面含有%s"%(text_audio_video))
            return text_audio_video
        except Exception as e:
            self.pu.lo.Logg(e)
            raise

    def login_people_lib(self,username,password):
            u"""拿到人物库----  人物库"""
            self.pu.lo.Logg("This classname is login_people_lib")
            try:
                self.pu.login_pub(username,password)
                self.pu.pub.waite(2)
                self.pu.pub.activeEvent(".//*[text()='人物库']")
                self.pu.pub.waite(2)
                text_people_lib = self.pu.pub.tryText(".//*[contains(text(),'知名人物')]")
                print("点击人物库后转向页面包含",text_people_lib)
                return text_people_lib
            except Exception as e:
                self.pu.lo.Logg(e)
                raise

    def video_label_yangqi(self,username,password):
            u"""拿到央企的视频列表里的其中两个视频的标签"""
            self.pu.lo("This classname is video_label_yangqi")
            try:
                self.pu.login_pub(username,password)
                self.pu.pub.waite(2)
                self.pu.pub.activeEvent(".//body/descendant::a[12]")
                self.pu.pub.waite(2)
                qiye_text = self.pu.pub.tryText(".//*[contains(text(),'综合排序')]/ancestor::div[3]/following-sibling::ul/descendant::div[3]")
                print("企业--视频右上角的标签为 " ,qiye_text)

                #拿到第一个视频的名字
                video_title_name = self.pu.pub.tryText(".//body/descendant::a[1]/ancestor::div[4]/following-sibling::section/div/ul/descendant::div[@class='title-box'][1]")
                print("第一个视频的标题为 " ,video_title_name)
                return qiye_text,video_title_name
            except Exception as e:
                self.pu.lo.Logg(e)
                raise

    def video_yangqi_fir_title(self,username,password):
        """拿到音视频栏目央企第一条视频信息的title"""
        self.pu.lo.Logg("This classname is video_yangqi_fir_title ")
        try:
            self.pu.login_pub(username,password)
            self.pu.lo.Logg("登录进系统")
            self.pu.pub.waite(2)
            self.pu.pub.waite(2)
            self.pu.lo.Logg("准备点击央企视频栏目")
            self.pu.pub.activeEvent(".//body/descendant::a[12]")
            self.pu.pub.waite(2)
            self.pu.pub.jsTopDown("300")
            self.pu.pub.waite(2)
            textone = self.pu.pub.tryText(".//body/descendant::a[1]/ancestor::div[4]/following-sibling::section/div/ul/descendant::div[@class='title-box'][1]")
            self.pu.lo.Logg("拿到央企下第一条视频信息的title %s"%textone)
            return textone
        except Exception as e:
            self.pu.lo.Logg(e)
            raise

    def video_yangqi_fir_in_title(self,username,password):
        """拿到音视频栏目央企第一条视频信息点击进去后的title"""
        self.pu.lo.Logg("This classname is video_yangqi_fir_title ")
        try:
            self.pu.login_pub(username,password)
            self.pu.pub.waite(1)
            texttwo = self.video_yangqi_fir_title(username,password)
            self.pu.lo.Logg("进入系统，根据第一条视频的title去点击第一条视频")
            self.pu.pub.tryMoveLocation(".//*[text()='%s']"%texttwo)
            self.pu.pub.waite(2)
            self.pu.lo.Logg("点击视频详情")
            self.pu.pub.activeEvent(".//*[text()='%s']"%texttwo)
            textthr = (self.pu.pub.tryText(".//body/descendant::h2")).split('丨')
            textfor = textthr[1]
            self.pu.lo.Logg("拿到视频详情的title----》%s"%textfor)
            return textfor
        except Exception as e:
            self.pu.lo.Logg(e)
            raise
#
# b = Bussniss()
# b.video_yangqi_fir_in_title("admin","111111")
#






















