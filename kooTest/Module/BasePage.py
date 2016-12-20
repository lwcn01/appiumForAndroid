#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"

import time
from Common.ReadData import *
from Common.Logger import mylog
from Common.Public.System import System
from selenium.webdriver.support.ui import WebDriverWait

class Base:
    driver = None
    def __init__(self, appium_driver):
        self.driver = appium_driver

    #单个元素定位方法
    def find_element(self,element):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*element).is_displayed())
            return self.driver.find_element(*element)
        except:
            mylog.warn("%s 页面中未能找到 %s 元素" %(self,element))

    #一组元素定位方法
    def find_elements(self,element):
        try:
            if len(self.driver.find_elements(*element)):
                return self.driver.find_elements(*element)
        except:
            mylog.warn("%s 页面中未能找到 %s 元素" %(self,element))

    # 自定义图片的名称
    def __savePicture(self, name):
        __image = System().log_path + "\\Image"
        if not os.path.exists(__image):
            os.mkdir(__image)
        return  __image + "\\" + name + "_" + System().sysTime + ".png"

     # 截图
    def screenShot(self,name):
        """
		name:图片名称
		"""
        time.sleep(String.WAIT_TIME)
        mylog.info("当前截图存储路径：%s" % self.__savePicture(name))
        return self.driver.get_screenshot_as_file(self.__savePicture(name))

    def pressKeycode(self,key):
        mylog.info("按键事件：keycode %s" % key)
        return self.driver.press_keycode(key)

    def isAppInstall(self, bundle_id):
        """Checks whether the application specified by `bundle_id` is installed
        on the device.
        :Args:
         - bundle_id - the id of the application to query
         :Usage:
         - isAppInstall“com.xxxx”
        """
        try:
            self.driver.is_app_installed(bundle_id)
        except Exception as e:
            mylog.warn("%s 未安装：%s" %(bundle_id,e))
            return False
        else:
            return True

    def InstallApp(self, app_path):
        """Install the application found at `app_path` on the device.

        :Args:
         - app_path - the local or remote path to the application to install
        """
        try:
            self.driver.install_app(self, app_path)
        except Exception as e:
            mylog.warn("%s 安装失败：%s" %(app_path,e))