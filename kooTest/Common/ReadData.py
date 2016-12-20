#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"
import os
import xlrd
from Common.Logger import mylog
from Common.Public.System import System
from Common.Public.String import String
from xml.etree import ElementTree as ET

class Data:
    def __init__(self):
        self.__path = System().data_path

    def getXml(self,xml,node):
        _xml_path = ""
        # xml argment : 提供xml配置文件名称
        for __file in os.listdir(self.__path):
            if __file.endswith(String.XML):
                _xml_path = self.__path + "\\" + xml
                break

        if not _xml_path:
            mylog.error("XML文件不存在")
        else:
            #打开xml文档
            root = ET.parse(_xml_path)
            #查找当前目录下的capabilities的子节点
            books  = root.findall(node)
            k = []
            v = []
            for book_list in books:
                for book in book_list:
                    # 当要获取属性值时，用attrib方法
                    # 当要获取节点名时，用tag方法
                    k.append(book.tag)
                    # 当要获取节点值时，用text方法
                    v.append(book.text)
            # 以字典返回xml文件中信息
            return dict(zip(k,v))

    def __excelPath(self):
        for __xls in System().listFile(self.__path):
            if __xls.split(".")[-1] == String.XLSX:
                # 返回测试用例路径，:\workspace\koo\data\koocan测试用例.xlsx
                return __xls
            elif __xls.split(".")[-1] == String.XLS:
                return __xls

    def excelRead(self,table_sheet):
        # table_sheet 表格sheet的数值，如0,1,2
        file_path = self.__excelPath()
        if not os.path.exists(file_path):
            mylog.error("目录" + self.__path + "下不存在用例文件")
            # read excel
        else:
            mylog.info("测试用例路径：" + file_path)
            __xls = xlrd.open_workbook(file_path)
            # 按表格名称，返回当前sheet，每个sheet只编写某个模块用例
            __table = __xls.sheet_by_index(table_sheet)
            __rows = __table.nrows  #行
            __cols = __table.ncols  #列
            __colnames = __table.row_values(0) #以列表形式返回第一行的所有值
            #mylog.info(__colnames)
            #将每一行数据以字典返回，将每一行字段组成的字典添加生成一个list
            data = []
            for r in range(1,__rows):
                xls_row = {}
                for c in range(__cols):
                    __cell_value = __table.cell(r,c).value
                    # 判断表格值是否为空
                    if __cell_value == "":
                        __cell = []
                        for __r in range(1,r):
                            if __table.cell(__r,c).value != "":
                                __cell.append(__table.cell(__r,c).value)
                        if len(__cell) == 0:
                            __cell_value = ""
                        else:
                            # 表格值为空，使用该列中最后显示的数值
                            __cell_value = __cell[-1]
                    xls_row.setdefault(__colnames[c],__cell_value)
                # 判断定位方式是否小写
                if xls_row[String.POSITION_METHOD].isupper():
                    xls_row[String.POSITION_METHOD] = xls_row[String.POSITION_METHOD].lower()
                data.append(xls_row)

            return data