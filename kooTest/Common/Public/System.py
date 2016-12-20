#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"

import os
import time

class System:
    def __init__(self):
        self.result_path = self.filePath("Result")
        self.data_path = self.filePath("Data")
        self.log_path = self.creatDir()
        self.sysTime = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime(time.time()))

    def removeFile(self,targetDir):
        """
	    批量删除空文件
	    """
        for __file in os.listdir(targetDir):
            __targetFile = os.path.join(targetDir,__file)
            if os.path.isfile(__targetFile):
                if not os.path.getsize(__targetFile):
                    os.remove(__targetFile)

    def filePath(self,_path):
        #父目录
        __fpath = os.path.pardir
        #当前目录 返回:\workspace\kooTest\Common\Public
        __spath = os.path.split(os.path.realpath(__file__))[0]
        #当前目录的上级目录 返回:\workspace\kooTest\Common\
        __cpath = os.path.abspath(os.path.join(__spath,__fpath))
        #当前目录的父级目录 返回:\workspace\kooTest
        __rpath = os.path.abspath(os.path.join(__cpath,__fpath))
        return __rpath + "\\" + _path

    def creatDir(self):
        """
        生成路径\Result\2016-xx-xx
        """
        result = self.result_path
        # 返回:\workspace\kooTest\Result
        if not os.path.exists(result):
            os.mkdir(result)
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        __resultpath = result + "\\" + day
        if not os.path.exists(__resultpath):
            os.mkdir(__resultpath)
        return __resultpath

    def listFile(self, path):
        """
        遍历目录,返回：
        ['G:\\workspace\\kooTest\\Data\\cap.xml',  'G:\\workspace\\kooTest\\Data\\testcase.xlsx']
        """
        if os.path.isdir(path):
            list_file = []
            for __file in os.listdir(path):
                __file_path = os.path.join(path,__file)
                if os.path.isfile(__file_path):
                    if os.path.splitext(__file_path)[-1] == ".apk":
                        list_file.append(__file_path)
                    elif os.path.splitext(__file_path)[-1] == ".xml":
                        list_file.append(__file_path)
                    elif os.path.splitext(__file_path)[-1] == ".xls":
                        list_file.append(__file_path)
                    elif os.path.splitext(__file_path)[-1] == ".xlsx":
                        list_file.append(__file_path)
            return list_file