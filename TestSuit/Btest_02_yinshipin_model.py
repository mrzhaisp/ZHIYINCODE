#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
from Commonlib.Commonlib import Commonlib

class YinShiPin(unittest.TestCase):
    def setUp(self):
        self.bu = Bussniss()
        self.r =  Readxml()
        self.c = Commonlib()
        self.c.solveWaring()

    def tearDown(self):
        u"""退出浏览器"""
        self.bu.pu.pub.quitBrowser()

    def test_001(self):
        u"""登录首页，可直接跳转到音视频库页面"""
        self.assertEqual(
            self.bu.login_audio_video(
                self.r.readxml("yinshipin","username"),
                self.r.readxml("yinshipin","password")),
                self.r.readxml("yinshipin","epxect")

        )

if __name__ == '__main__':
    unittest.main()





























