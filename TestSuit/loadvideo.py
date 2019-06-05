#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest

class loadvideo(unittest.TestCase):
    """上传视频"""
    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        self.b.c.waite(20)
        self.b.c.closeBrowser()

    def test_001(self):
        """上传符合格式的视频"""
        self.assertEqual(
            self.b.LoadVideo(),
            self.b.r.readxml("loadvideo","text")
        )


if __name__ == '__main__':
    unittest.main()

