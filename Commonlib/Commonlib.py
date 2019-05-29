#coding=utf-8
# __author__ = 'zgd'
import sys
import os
sys.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t
import warnings
class Commonlib():
    def __init__(self):
        """加载firefox配置文件"""
        # self.dr = webdriver.Firefox(webdriver.FirefoxProfile("C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\glw65f77.default"))
        # self.dr = webdriver.Firefox()
        self.dr = webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')

    def openBrowser(self,myurl):
        """打开浏览器"""
        self.dr.get(myurl)
        self.dr.maximize_window()

    def closeBrowser(self):
        """关闭当前聚焦点所在的浏览器"""
        self.dr.close()

    def solveWaring(self):
        """处理日志提示未关闭"""
        warnings.simplefilter("ignore", ResourceWarning)

    def quitBrowser(self):
        """关闭所有窗口，安全关闭session"""
        self.dr.quit()

    def localElement(self,value):
        """找到元素不做操作"""
        return  self.dr.find_element("xpath",value)

    def activeEvent(self,value):
        """点击事件"""
        self.dr.find_element("xpath",value).click()

    def inputKeys(self,value,sk):
        """输入关键字"""
        self.dr.find_element("xpath",value).send_keys(sk)

    def clearKeys(self,value):
        """清楚输入框内容"""
        self.dr.find_element("xpath",value).clear()

    def waite(self,num):
        """强制等待"""
        t.sleep(num)

    def moveElement(self,value):
        """移动到字符不做操作"""
        gt = self.localElement(value)
        ActionChains(self.dr).move_to_element(gt).perform()

    def tryFindIframe(self,value):
        """循环寻找iframe"""
        for i in range(10):
            try:
                self.dr.switch_to.frame(value)
                break
            except:pass
            t.sleep(1)

    def tryMoveLocation(self,value):
        """循环去找关键字然后"""
        for i in range(10):
            try:
                target = self.dr.find_element("xpath",value)
                self.dr.execute_script("arguments[0].scrollIntoView();", target)
                break
            except:pass
            t.sleep(1)

    def tryFindToclick(self,value):
        """循环去找元素去点击"""
        for i in range(20):
            try:
                self.dr.find_element("xpath",value).click()
                break
            except:pass
            t.sleep(1)
        else:
            print(u"没有找到关键字点击不了")



    def shiFangFrame(self):
        """释放iframe"""
        self.dr.switch_to.default_content()

    def jsTopDown(self,value):
        """处理滚动条上下"""
        js = 'var q=document.documentElement.scrollTop=' + str(value)
        self.dr.execute_script(js)

    def jsLeft(self,value):
        """处理横向滚动条左右"""
        jsleft = 'document.getElementsByClassName("x-scroller-ct")[0].scrollLeft='+ str(value)
        self.dr.execute_script(jsleft)


    def tryTimesleep(self,value):
        """每一秒去寻找切换iframe框"""
        for i in range(10):
            try:
                self.dr.switch_to.frame(value)
            except:pass
            t.sleep(1)

    def trySendKeys(self,value,connect):
        """尝试去输入值"""
        for i in range(10):
            try:
                self.dr.find_element_by_xpath(value).send_keys(connect)
                break
            except:pass
            t.sleep(1)
        else:
            print("Find xpath filed")

    def tryText(self,value):
        """尝试获取文字的函数"""
        for i in range(10):
            try:
                 gt = self.dr.find_element("xpath",value).text
                 return gt
            except:pass
            t.sleep(1)

    def impLicitly(self,value):
        """显式等待"""
        self.dr.implicitly_wait(value)

    def switchOneWindows(self,value):
        """切换到浏览器窗口"""
        all_handers= self.dr.window_handles
        print(all_handers)
        self.dr.switch_to_window(self.dr.window_handles[value])
        # print(self.dr.title)

    def getScreenShot(self,value):
        """截图"""
        self.dr.get_screenshot_as_file(value)

    def reFresh(self):
        """刷新页面"""
        self.dr.refresh()

    def dissMissAlter(self):
        """处理弹框"""
        alsm = self.dr.switch_to.alert()
        # alsk = self.dr.switch_to_alert()
        alsm.dismiss()

    def getAlterText(self):
        """拿到弹框的txt文字"""
        t = self.dr.switch_to_alert()
        # print(t.text)

    def getTitle(self):
        text = self.dr.title
        return text

    def uiLogIn(self,myurl,username,password):
        """前端UI显示"""
        self.openBrowser(myurl)
        self.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input")
        self.waite(1)
        self.inputKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input",username)
        self.waite(1)
        self.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input")
        self.waite(1)
        self.inputKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input",password)
        self.waite(1)
        self.activeEvent(".//*[contains(text(),'立即登录')]")

    def loadVideoLogIn(self,myurl,username,password):
        """后台上传视频"""
        self.openBrowser(myurl)
        self.waite(1)
        self.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input")
        self.waite(1)
        self.inputKeys((".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input"),username)
        self.waite(1)
        self.clearKeys(".//body/descendant::input[2]")
        self.waite(1)
        self.inputKeys(".//body/descendant::input[2]",password)
        self.waite(1)
        self.activeEvent(".//*[contains(text(),'立即登录')]")
