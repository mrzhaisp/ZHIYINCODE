#coding=utf-8
from Commonlib.Commonlib import Commonlib
import time as t
from selenium import webdriver
options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,
    'download.default_directory': r'C:\Users\Test\loadvideofile\seleniundownload',#下载目录
    "plugins.always_open_pdf_externally": True,
    'profile.default_content_settings.popups': 0,#设置为0，禁止弹出窗口
    # 'profile.default_content_setting_values.images': 2,#禁止图片加载
    }
options.add_experimental_option('prefs',prefs)

executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"

dr = webdriver.Chrome(executable_path=executable_path,chrome_options=options)

dr.get("http://10.168.103.151/web/#/login")

dr.maximize_window()

dr.find_element("xpath",".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input").send_keys("admin")
t.sleep(1)
dr.find_element("xpath",".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input").send_keys("111111")
t.sleep(1)
dr.find_element("xpath",".//*[contains(text(),'立即登录')]").click()
t.sleep(1)
#点击事实热点
dr.find_element("xpath",".//section/div/descendant::a[5]").click()
t.sleep(1)
dr.find_element("xpath",".//section/div/descendant::img[1]").click()
t.sleep(2)
dr.find_element("xpath",".//*[contains(text(),'下载视频')]").click()
















