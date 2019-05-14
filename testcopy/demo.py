#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.Public import PubLic
from selenium import webdriver
import unittest
import time as t
from Commonlib.Loggin import LoggIn

class Testdemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pu = PubLic()
        lo = LoggIn()
        cls.lo = lo
        cls.pu = pu
        pu.login_pub("admin","111111")
        lo.Logg("打开浏览器，输入了账户名密码进入主页")

    @classmethod
    def tearDownClass(cls):
        #退出浏览器
        cls.pu.pub.closeBrowser()
        cls.lo.Logg("关闭浏览器")

    def test001_get_text_001(self):
        try:
            #拿到具体栏目下的视频的title
            self.pu.pub.activeEvent(".//body/descendant::a[12]")
            self.pu.pub.waite(2)
            self.pu.pub.jsTopDown(300)
            self.pu.pub.waite(2)
            textone = self.pu.pub.tryText(".//body/descendant::a[1]/ancestor::div[4]/following-sibling::section/div/ul/descendant::div[@class='title-box'][1]")
            self.lo.Logg("获取第一个视频下的name")
            self.pu.pub.waite(2)
            # 重新点击音视频库存
            self.pu.pub.activeEvent(".//body/descendant::a[2]")
            self.lo.Logg("拿到第一条视频的title----> %s"  %(textone))
            return textone
        except Exception as e:
            self.lo.Logg(e)
            raise


    def test002_video_text(self):
        pass


if __name__ == '__main__':
    unittest.main()
















