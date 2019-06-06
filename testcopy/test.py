#coding=utf-8
from Commonlib.Commonlib import Commonlib
from selenium import webdriver
# import time as t
# import random
# options = webdriver.ChromeOptions()
# prefs = {
#     "download.prompt_for_download": False,
#     'download.default_directory': r'C:\Users\Test\loadvideofile\seleniundownload',#下载目录
#     "plugins.always_open_pdf_externally": True,
#     'profile.default_content_settings.popups': 0,#设置为0，禁止弹出窗口
#     # 'profile.default_content_setting_values.images': 2,#禁止图片加载
#     }
# options.add_experimental_option('prefs',prefs)
#
# executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
#
# dr = webdriver.Chrome(executable_path=executable_path,chrome_options=options)
#
# dr.get("http://10.168.103.151/web/#/login")
#
# dr.maximize_window()
#
# dr.find_element("xpath",".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input").send_keys("admin")
# t.sleep(1)
# dr.find_element("xpath",".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input").send_keys("111111")
# t.sleep(1)
# dr.find_element("xpath",".//*[contains(text(),'立即登录')]").click()
# t.sleep(2)
# #点击事实热点
# listnum = ["5","6","7","8","9","10","11","12","13","14"]
# filexpath = ".//section/div/descendant::a[%s]"%random.choice(listnum)
# # xpaths = [".//section/div/descendant::a[13]",".//section/div/descendant::a[14]"]
# print(filexpath)
# dr.find_element("xpath","%s"%filexpath).click()
# t.sleep(2)
# dr.find_element("xpath",".//section/div/descendant::img[1]").click()
# t.sleep(2)
# dr.find_element("xpath",".//*[contains(text(),'下载视频')]").click()
#
#
import os

def file_name(file_dir):
    for root ,dirs,files in os.walk(file_dir):
        print(files)
        for i in files:
            print(i)

file_name(r"C:\Users\Test\loadvideofile\seleniundownload")








