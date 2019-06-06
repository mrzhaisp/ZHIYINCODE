#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# 判断文件是否存在
file = r"C:\Users\admin\Downloads"
videoname = "20190530--700MCSCI262---Intrusion-Detection-Systems-(IDS)"
path_name = file + '\\' + videoname
mt = os.path.exists(path_name)
print(mt)













