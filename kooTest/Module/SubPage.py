#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"

from appium import webdriver
from Module import HomePage
from Common.Logger import mylog
from Common.ReadData import Data
from Common.Public.String import String
from Common.Public.Keycode import KeyCode

class SubPage(HomePage.Home):
    desired_caps = Data().getXml(String.DRIVER_XML,String.NODE_CAP)
    driver = webdriver.Remote(String.DRIVER_ADDRESS, desired_caps)

    def handleCase(self,table_sheet=None):
        case_list = Data().excelRead(table_sheet)
        for case in case_list:
            mylog.info("%s : %s : %s" % (case[String.TESTCASE_ID],case[String.TEST_STEP],case[String.TEST_OBJECT]))
            # 列表case_list中取excel中一行的用例case,字典类型
            if case[String.POSITION_METHOD] == String.ID:
                # 元素查找方式
                if case[String.OPERATION_METHOD] == String.CLICK:
                    self.clickButton(self.byId,case[String.TEST_OBJECT])
                elif case[String.OPERATION_METHOD] == String.SEND_KEYS:
                    self.sendKeys(self.byId,case[String.TEST_OBJECT],case[String.TEST_DATA])
            elif case[String.POSITION_METHOD] == String.ACCESSIBILITY_ID:
                if case[String.OPERATION_METHOD] == String.CLICK:
                    self.clickButton(self.byID,case[String.TEST_OBJECT])
                elif case[String.OPERATION_METHOD] == String.SEND_KEYS:
                    self.sendKeys(self.byID,case[String.TEST_OBJECT],case[String.TEST_DATA])
            elif case[String.POSITION_METHOD] == String.CLASS_NAME:
                if case[String.OPERATION_METHOD] == String.CLICK:
                    self.clickButton(self.byClassName,case[String.TEST_OBJECT])
                elif case[String.OPERATION_METHOD] == String.SEND_KEYS:
                    self.sendKeys(self.byClassName,case[String.TEST_OBJECT],case[String.TEST_DATA])
            elif case[String.POSITION_METHOD] == String.XPATH:
                if case[String.OPERATION_METHOD] == String.CLICK:
                    self.clickButton(self.byXpath,case[String.TEST_OBJECT])
                elif case[String.OPERATION_METHOD] == String.SEND_KEYS:
                    self.sendKeys(self.byXpath,case[String.TEST_OBJECT],case[String.TEST_DATA])
            elif case[String.POSITION_METHOD] == String.KEY:
                for name,value in vars(KeyCode).items():
                    if case[String.TEST_OBJECT].upper() == name:
                        if case[String.OPERATION_METHOD] == String.NONE:
                            self.pressKeycode(value)
                        # 按键事件遍历
                        elif case[String.OPERATION_METHOD] == String.TRAVERSE:
                            for traverse_num in range(10):
                                self.pressKeycode(value)