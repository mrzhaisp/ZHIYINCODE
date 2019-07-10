#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest
import time

class VidevTitle(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        self.b.c.closeBrowser()

    def test_001(self):
        """拿到视频未点击钱的名称和视频点击后的名称"""
        try:
            textlist = self.b.ShiShiredian(
                self.b.r.readxml("videotitle", "url"),
                self.b.r.readxml("videotitle", "usname"),
                self.b.r.readxml("videotitle", "password"))

            textlist[0]
            acop = textlist[1].split("：")

            self.assertEqual(textlist[0], acop[1])
        except Exception as e:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            pictfile = "../ErrorPict/"
            pictname = nowTime + 'f_viderotitle' + '.png'
            self.b.c.getScreenShot(pictfile + pictname)
            self.b.l.Logg(e)


if __name__ == '__main__':
    unittest.main()
