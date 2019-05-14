#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
from Commonlib.Commonlib import Commonlib
class LoginTatle(unittest.TestCase):
    """root登录首页"""

    def setUp(self):
        self.bu = Bussniss()
        self.r = Readxml()
        self.c = Commonlib()
        self.c.solveWaring()

    def tearDown(self):
        """退出浏览器"""
        self.bu.pu.pub.quitBrowser()

    def test_001(self):
        u"""不同权限分配不同首页"""
        self.assertEqual(
            self.bu.login_action_header(
                self.r.readxml("login","username"),
                self.r.readxml("login","password")),
                self.r.readxml("login","epxect"))

if __name__ == '__main__':
    unittest.main()



















