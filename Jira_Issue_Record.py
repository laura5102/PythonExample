#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import xlsxwriter
from xlutils.copy import copy
import xlrd
import base64
import datetime,time
from jira import JIRA
from pprint import pprint
import xlrd as ExcelRead

global _file_name

_file_name = "/Users/lei/Documents/工作/寺库/SVN/opdoc/上线文档/03_寺库上线记录表.xls"
_jira_server = "http://jira.secoo.com/"
_user = "bGl1bGVp"
_passwd = "IVFBWmNkZTNA"
_authed_jira = JIRA(server=(_jira_server),basic_auth=(base64.b64decode(_user), base64.b64decode(_passwd)))
_number = 0
# 将数据写入文件
def write_append(file_name,input_data):
    _values = input_data
    print "input_data:\n", _values
    _r_xls = ExcelRead.open_workbook(file_name)
    _r_sheet = _r_xls.sheet_by_index(0)
    rows = _r_sheet.nrows
    _w_xls = copy(_r_xls)
    sheet_write = _w_xls.get_sheet(0)

    for i in range(0, 8):
        sheet_write.write(rows, i, _values[i])
        #w_xls.save(file_name + '.out' + os.path.splitext(file_name)[-1]);
        _w_xls.save(_file_name)

def _get_issue_info(issueid):
    _key = issueid
    _issue_info = _authed_jira.issue(_key)
    _summary = _issue_info.fields.summary
    _reporter = _issue_info.fields.reporter
    _duedate = _issue_info.fields.duedate
    _description = _issue_info.fields.description
    _description = _description.replace(' ','')
    _type = _issue_info.fields.issuetype.name
    _data = (u"%d %s [JIRA](%s)%s %s  B %s %s" % (_number, _description, _key, _summary, _reporter, _type, _duedate))
    _data = _data.split(' ')
    write_append(_file_name, _data)


today = datetime.date.today()
today_finish = "issuetype in (线上问题, 项目上线, 上线任务) AND status = 上线完成 AND due = " + str(today)
_search_results = _authed_jira.search_issues(today_finish)

if len(_search_results) != 0:
    for index in range(len(_search_results)):
        _number += 1
        _key = _search_results[index].key
        _get_issue_info(_key)