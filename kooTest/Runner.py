#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"
import time
import unittest
from Common.MyLog import myLog
from Common.SendEmail import sendEmail
from Common.Public import HTMLTestRunner
from Common.Public.System import System
from Common.Public.String import String
from Common.Command import Initialize,Command

def creatSuite():
    case_path = ".\\Testcase"
    # 定义单元测试容器
    testsuite = unittest.TestSuite()
    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)
    # 将测试用例加入测试容器中
    for test_script in discover:
        for test_case in test_script:
            testsuite.addTest(test_case)
    return testsuite

@myLog
def AutoRunner():
    try:
        Initialize().adbEnv()
        Initialize().checkEnv()
    except:
        raise EnvironmentError
    else:
        Command().installApp(app_dir=System().data_path)
        time.sleep(String.WAIT_TIME)
        suite = creatSuite()
        #报告存放路径，支持相对路径
        filename = System().log_path + "\\Report_" + System().sysTime + "." + String.HTML
        fp = open(filename, 'wb')
        #定义测试报告
        #runner=unittest.TextTestRunner(verbosity=2,resultclass=HTMLTestRunner._TestResult)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=String.TEST_TITLE,description=String.TEST_DETAILS)
        #运行测试用例
        runner.run(suite)
        fp.close()  #关闭报告文件
        sendEmail(filename)

if __name__ == '__main__':
    AutoRunner()