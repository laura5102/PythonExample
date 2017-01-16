#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('demo1.xlsx')   # 创建一个EXCEL文件
worksheet = workbook.add_worksheet()   # 创建一个工作表对象

worksheet.set_column('A:A',20)    # 设定第一列（A）宽度为20像素
bold = workbook.add_format({'bold': True})   # 定义一个加粗的格式对象

worksheet.write('A1','Hello')   # A1单元格写入'Hello'
worksheet.write('A2','world',bold)   # A2单元格写入'world'并引用加粗格式对象bold
worksheet.write('B2',u'中文测试',bold)   # B2单元格写入中文并引用加粗格式对象bold

worksheet.write(2, 0, 32)  # 用行列表示法写入数字‘32’与‘35.5’
worksheet.write(3, 0, 35.5)  # 行列表示法的单元格下标以0作为起始值，‘3,0’等价于‘A3’
worksheet.write(4, 0, '=SUM(A3:A4)') 

workbook.close()