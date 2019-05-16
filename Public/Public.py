#coding=utf-8
# __author__ = 'zgd'
from Commonlib.Commonlib import Commonlib
from Commonlib.Loggin import LoggIn
from Commonlib.Readxml import Readxml

lo = LoggIn()
r = Readxml()

class PubLic:

    def __init__(self):
        self.pub = Commonlib()

    def login_pub(self,username,password):
        """封装登录模块"""
        self.pub.openBrowser(r.readxml("baseurl","testurl"))
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
