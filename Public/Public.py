#coding=utf-8
# __author__ = 'zgd'
import sys
import os
sys.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Commonlib.Commonlib import Commonlib
from Commonlib.Loggin import LoggIn
from Commonlib.Readxml import Readxml
class PubLic:
    def __init__(self):
        self.pub = Commonlib()
        self.r  = Readxml()
        self.lo = LoggIn()

    def login_pub(self,username,password):
        """封装登录模块"""
        self.pub.openBrowser(self.r.readxml("baseurl","testurl"))
        self.pub.waite(1)
        self.pub.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input")
        self.pub.waite(1)
        self.pub.inputKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input",username)
        self.pub.waite(1)
        self.pub.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input")
        self.pub.waite(1)
        self.pub.inputKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input",password)
        self.pub.waite(1)
        self.pub.activeEvent(".//*[contains(text(),'立即登录')]")
        self.pub.waite(2)
# if __name__ == '__main__':
#     mop = PubLic()
#     mop.login_pub("loginusername","loginpwd")






































