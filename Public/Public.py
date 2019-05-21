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

    def login_ui_pub(self,base_url,username,password):
        """前端UI登录模块"""
        self.pub.openBrowser(base_url)
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

    def login_load_video(self,base_url,username,password):
        """后台上传视频登录"""
        self.pub.openBrowser(base_url)
        self.pub.waite(1)
        self.pub.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input")
        self.pub.waite(1)
        self.pub.inputKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input",username)
        self.pub.waite(1)
        self.pub.clearKeys(".//body/descendant::input[2]")
        self.pub.waite(1)
        self.pub.inputKeys(".//body/descendant::input[2]",password)
        self.pub.waite(1)
        self.pub.activeEvent(".//*[contains(text(),'立即登录')]")
# b = PubLic()
# b.login_load_video("http://10.168.103.151/admin/#/","admin","111111")












