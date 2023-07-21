 # !/usr/bin/python
 # -*- coding: UTF-8 -*-
 # author: jing
 # excel的封装

import xlrd
workbook = None

def open_excel(path):
     """
     打开excel
     :param path: 打开excel文件的位置
     """
     global workbook
     if (workbook == None):
        workbook = xlrd.open_workbook(path, on_demand=True)

def get_sheet(sheetName):
     """
     获取页名
     :param sheetName: 页名
     :return: workbook
     """
     global workbook
     return workbook.sheet_by_name(sheetName)


def get_rows(sheet):
    """
    获取行号
    :param sheet: sheet
    :return: 行数
    """
    return sheet.nrows


def get_columns(sheet):
    """
    获取列数
    :param sheet: sheet
    :return: 列数
    """
    return sheet.ncols



def get_content(sheet, row, col):
    """
    获取表格中内容
    :param sheet: sheet
    :param row: 行
    :param col: 列
    :return:
    """
    return sheet.cell(row, col).value



def get_excel_sheet(self, path, module):
    """依据模块名获取sheet"""
    open_excel(path)
    return get_sheet(module)

def release(path):
    """释放excel减少内存"""
    global workbook
    workbook.release_resources()
    del workbook


