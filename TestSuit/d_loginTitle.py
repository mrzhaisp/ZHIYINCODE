#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest
import time


class LogTitle(unittest.TestCase):
    """首页登录title"""

    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        self.b.c.quitBrowser()

    def test_001(self):
        """首页登录title"""
        try:
            self.assertEqual(self.b.getLoginTitle(
                self.b.r.readxml("baseurl", "uiUrl"),
                self.b.r.readxml("login", "username"),
                self.b.r.readxml("login", "password"))
                , self.b.r.readxml("loginTitle", "epxect"))
        except Exception as e:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            pictfile = "../ErrorPict/"
            pictname = nowTime + 'd_loginTitle' + '.png'
            self.b.c.getScreenShot(pictfile+pictname)
            self.b.l.Logg(e)

if __name__ == '__main__':
    unittest.main()
