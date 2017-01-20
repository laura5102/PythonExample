#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 脚本功能：实现每日上线计划、明日上线计划、以及当天完成上线需求.

#from jira import JIRA
import base64
import datetime,time
from jira import JIRA
from pprint import pprint


class SearchClass(object):

    # base64.b64encode("xxx")
    _number = 0
    _jira_server = "http://jira.secoo.com/"
    _user = "bGl1bGVp"
    _passwd = "IVFBWmNkZTNA"

    def __init__(self):
        self._key = ""
        self._summary = ""
        self._reporter = ""
        self._duedate = ""
        self._description = ""
        self._search_results = ""
        self._search_command = ""
        self._issue_info = ""
        self._type = ""
        self._authed_jira = JIRA(server=(self._jira_server), basic_auth=(base64.b64decode(self._user), base64.b64decode(self._passwd)))

    def _jira_status(self):
        return self._authed_jira

    def _search_issues(self, command):
        self._search_command = command
        self._search_results = self._authed_jira.search_issues(self._search_command)
        return self._search_results

    def _get_issue_info(self, issueid):
        self._key = issueid
        self._issue_info = self._authed_jira.issue(self._key)
        self._summary = self._issue_info.fields.summary
        self._reporter = self._issue_info.fields.reporter
        self._duedate = self._issue_info.fields.duedate
        self._description = self._issue_info.fields.description
        self._type = self._issue_info.fields.issuetype.name
        self._number +=1
        print  (u" %d、[%s] (%s) %s  @%s  %s  " % (self._number, self._type, self._key, self._summary, self._reporter, self._duedate))

    def _print_search_resluts(self):
        # 如
        if len(self._search_results) != 0 :
            for index in range(len(self._search_results)):
                self._key = self._search_results[index].key
                self._get_issue_info(self._key)
        else:
            print u"暂无"


# 主程序
today = datetime.date.today() 
tomorrow = today + datetime.timedelta(days=1) 

today_plan_bak = "issuetype in (线上问题, 项目上线, 上线任务) AND status in \
(开放, 正在处理, 上线申请, 测试中, 测试确认, 需求方确认, 测试通过, 问题确认, 问题创建人确认, 开发负责人确认, 开发处理) \
AND assignee in (currentUser(), yanglili, membersOf(运维组)) AND due = " + str(today)
today_plan = "issuetype in (线上问题, 项目上线, 上线任务) AND due =" + str(today)
today_finish = "issuetype in (线上问题, 项目上线, 上线任务) AND status = 上线完成 AND due = " + str(today) 
tomorrow_plan = "issuetype in (线上问题, 项目上线, 上线任务)  AND due = " + str(tomorrow)

print u"【生产环境】今日计划上线:"
search1 = SearchClass()
search1._search_issues(today_plan)
search1._print_search_resluts()
print 

print u"[明日计划]："
search2 = SearchClass()
search2._search_issues(tomorrow_plan)
search2._print_search_resluts()
print
print "小贴示: 请各位小伙伴在上线前，完成上线内容说明和各环节审批。\n"

print u"[今日已完成]："
search3 = SearchClass()
search3._search_issues(today_finish)
search3._print_search_resluts()





