#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"
import os
import sys
import logging
import logging.handlers
from Common.Public.System import System
from Common.Public.String import String

def initlog():
    # 配置日志信息
    global mylog
    # 获取mylog实例，如果参数为空则返回root mylog
    mylog = logging.getLogger(String.NEW)
    # 指定日志的最低输出级别，默认为WARN级别
    mylog.setLevel(logging.DEBUG)
    # 指定mylog输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)3s - %(levelname)s - %(message)s')
    # 文件日志
    fh = logging.FileHandler(os.path.join(System().log_path,String.LOG_NAME))
    fh.setFormatter(formatter)
    # 控制台日志
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    # 为mylog添加的日志处理器
    mylog.addHandler(fh)
    mylog.addHandler(console)
    return mylog
mylog = initlog()