#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.Public import PubLic
from Commonlib.Commonlib import Commonlib
from Commonlib.Readxml import Readxml
from Commonlib.Loggin import LoggIn
import unittest
c = Commonlib()
lo = LoggIn()
r = Readxml()
class videoLable(unittest.TestCase):
    """拿到所有栏目下的子视频右上角标签，和栏目标签作对比"""
    @classmethod
    def setUpClass(cls):
        c.solveWaring()
        pu = PubLic()
        cls.pu = pu
        cls.pu.login_pub(r.readxml("videoLable","username"),
                         r.readxml("videoLable","password"))
        lo.Logg("打开浏览器")

    @classmethod
    def tearDownClass(cls):
        cls.pu.pub.closeBrowser()
        lo.Logg("关闭浏览器")

    # @unittest.skip("暂时跳过")
    def test_001(self):
        u"""拿到央企标签和该栏目下的视频标签"""
        try:
            lo.Logg("第一个测试案例,拿到央企标签和该栏目下的视频标签")
            self.pu.pub.waite(2)
            textone = self.pu.pub.tryText(".//*[contains(text(),'内网自编')]/ancestor::div[1]/following::li[1]/a")
            # print(textone)
            lo.Logg("输出title为 %s"%textone)
            self.pu.pub.waite(2)
            self.pu.pub.activeEvent(".//*[contains(text(),'内网自编')]/ancestor::div[1]/following::li[1]/a")
            self.pu.pub.waite(2)
            self.pu.pub.jsTopDown("150")
            self.pu.pub.waite(1)
            texttwo = self.pu.pub.tryText(".//*[contains(text(),'综合排序')]/ancestor::div[3]/following-sibling::ul/descendant::div[3]")
            lo.Logg("得到视频标签为%s"%texttwo)
            # print(texttwo)
            self.assertEqual(textone,texttwo)
        except Exception as e:
            lo.Logg(e)
            raise

    def test_002(self):
        u"""拿到国资委标签和该栏目下的视频标签"""
        lo.Logg("第二条测试用例,拿到国资委标签和该栏目下的视频标签")
        try:
            self.pu.pub.moveElement(".//*[contains(text(),'国资委')]")
            self.pu.pub.waite(2)
            textth = self.pu.pub.tryText(".//*[contains(text(),'国资委')]")
            lo.Logg("拿到国资委的标签为%s"%textth)
            self.pu.pub.waite(2)
            self.pu.pub.activeEvent(".//*[contains(text(),'国资委')]")
            self.pu.pub.waite(2)
            textthi = self.pu.pub.tryText(".//*[contains(text(),'综合排序')]/ancestor::div[3]/following-sibling::ul/descendant::div[3]")
            lo.Logg("得到国资委视频标签为%s" %textthi )
            self.assertEqual(textth,textthi)
        except Exception as e:
            lo.Logg(e)
            raise


if __name__ == '__main__':
    unittest.main()

























































