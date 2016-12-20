#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"
import time
import unittest
from Module.SubPage import SubPage
from Common.Public.String import String

class Headlines(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = SubPage.driver

    def test_headlines(cls):
        time.sleep(String.WAIT_TIME)
        SubPage(appium_driver=cls.driver).handleCase(0)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()

