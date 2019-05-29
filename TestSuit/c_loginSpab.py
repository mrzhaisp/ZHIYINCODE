#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest
import operator

class LoginSpan(unittest.TestCase):
    """登录主页后显示三个span栏目'时事热点','内网自编','外网资源',"""

    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        self.b.c.closeBrowser()

    def test_001(self):
        """获取到页面上登录首页的三个标题，组成列表，对比"""
        listone = self.b.AudioVideo(
            self.b.r.readxml("loginspan", "url"),
            self.b.r.readxml("loginspan", "username"),
            self.b.r.readxml("loginspan", "password"))

        # 这里顺序必须的一样  否则就返回False
        listtwo = ['时事热点', '内网自编', '外网资源']

        t = operator.eq(listone, listtwo)

        self.assertEqual(t, True)


if __name__ == '__main__':
    unittest.main()
