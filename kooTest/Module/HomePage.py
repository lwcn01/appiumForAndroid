#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"

from Module import BasePage
from Common.Logger import mylog
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

class Home(BasePage.Base):

    def byId(self, id_):
        """Finds an element by id.元组

        :Args:
         - id\_ - The id of the element to be found.

        :Usage:
            driver.find_element_by_id('foo')
        """
        return self.find_element((By.ID, id_))

    def byID(self,id):
        """
        usage: byID("ll_fav")
        """
        return self.find_element((MobileBy.ACCESSIBILITY_ID,id))

    def byXpath(self, xpath):
        """
        Finds an element by xpath.

        :Args:
         - xpath - The xpath locator of the element to find.

        :Usage:
            driver.find_element_by_xpath('//div/td[1]')
        """
        return self.find_element((By.XPATH, xpath))

    def byClassName(self, name):
        """
        Finds an element by class name.

        :Args:
         - name: The class name of the element to find.

        :Usage:
            driver.find_element_by_class_name('foo')
        """
        return self.find_element((By.CLASS_NAME, name))

    def androidUiautomator(self, uia_string):
        """Finds element by uiautomator in Android.

        :Args:
         - uia_string - The element name in the Android UIAutomator library

        :Usage:
            driver.find_element_by_android_uiautomator('.elements()[1].cells()[2]')
        """
        return self.find_element((MobileBy.ANDROID_UIAUTOMATOR, uia_string))

    def androidUiautomatorList(self, uia_string):
        """Finds elements by uiautomator in Android.

        :Args:
         - uia_string - The element name in the Android UIAutomator library

        :Usage:
            driver.find_elements_by_android_uiautomator('.elements()[1].cells()[2]')
        """
        return self.find_elements((MobileBy.ANDROID_UIAUTOMATOR, uia_string))

    def clickButton(self,by = byId,value = None):
        """
        :Usage:

        """
        try:
            __method = by(value)
            TouchAction(self.driver).tap(__method).perform()
        except:
            mylog.warn("%s 页面中 %s 元素未能找到按钮" %(self,value))

    def sendKeys(self,by = byId,element=None,value = None):
        """sendKeys
        :Usage:

        """
        try:
            __method = by(element)
            TouchAction(self.driver).tap(__method).perform()
        except:
            mylog.warn("%s 页面中 %s 元素未能找到按钮" %(self,element))
        else:
            __method.clear()
            __method.send_keys(value)

    def getGrid(self,loc):
        """find postions of the element
        :Usage:

        """
        __element = self.find_element(loc)
        __startX = int(__element.location['x'])
        __startY = int(__element.location['y'])
        __endX = int(__element.size['width']) + __startX
        __endY = int(__element.size['height']) + __startY

        centerX = (__startX + __endX) / 2
        centerY = (__startY + __endY) / 2

        return centerX,centerY

    def currentWindowSize(self):
        """
        get current windows size mnn
        :return:windowSize 返回字典
        """
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        return width,height

    def swipeToLeft(self,during=None):
        """from right swipe to left
        :Usage:
        :during: continus time
        """
        #width = self.driver.manage().window().getSize().width
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        return self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2, during)

    def swipeToRight(self,during=None):
        """
        swipe right
        :param during:
        :return:
        """
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        return self.driver.swipe(width/5, height/2, width*4/5, height/2, during)

    def swipeToUp(self,during=None):
        """
        swipe UP
        :param during:
        :return:
        """
        width = self.currentWindowSize()[0]
        height = self.currentWindowSize()[1]
        return self.driver.swipe(width/2, height/4, width/2, height*3/4, during)

    def swipeToDown(self,during=None):
        """
        swipe down
        :param during:
        :return:
        """
        width = self.currentWindowSize()[0]
        height = self.currentWindowSize()[1]
        return self.driver.swipe(width/2, height*3/4, width/2, height/4, during)