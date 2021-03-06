#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest
import time

class DownloadVideo(unittest.TestCase):
    """随机下载视频，"""
    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        #暂停20S 下载视频
        self.b.c.closeBrowser()

    def test_001(self):


        """随机下载视频，遍历下载后所有的视频名称,"""
        try:

            self.b.DownloadVideo(self.b.r.readxml("dowmloadvideo","url"),
                                 self.b.r.readxml("dowmloadvideo","usna"),
                                 self.b.r.readxml("dowmloadvideo","paswd"))
        except Exception as e:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            pictfile = "../ErrorPict/"
            pictname = nowTime + 'h_dowmkoadvideo' + '.png'
            self.b.c.getScreenShot(pictfile + pictname)
            self.b.l.Logg(e)

if __name__ == '__main__':
    unittest.main()



































