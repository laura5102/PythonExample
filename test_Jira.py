#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from jira import JIRA
from jira import JIRA
from pprint import pprint
authed_jira = JIRA(server=('http://jira.secoo.com/'),basic_auth=('liulei','!QAZcde3@'))

class SearchIssue:
    # 定义成员变量
    key = ""
    summary = ""
    reporter = ""
    duedate = ""
    description = ""

    def __init__(self, key):
        key = key

    def get_issue_info(self):
    	issue = authed_jira.issue(self.key)
    	self.summary = issue.fields.summary
    	self.reporter = issue.fields.reporter
    	self.duedate = issue.fields.duedate
    	self.description = issue.fields.description
    
        return ("[JIRA] (%s) %s  @%s  %s " % (self.key, self.summary, self.reporter, self.duedate))


# 主程序
print "今日计划上线"
search_issue = authed_jira.search_issues('issuetype in (线上问题, 项目上线, 上线任务) AND status in (开放, 正在处理, 测试中, 测试确认, 需求方确认, 测试通过, 问题确认, 问题创建人确认, 开发负责人确认, 开发处理) AND assignee in (currentUser(), yanglili, membersOf(运维组)) ORDER BY status DESC')
#pprint(search_issue)      # print search_issue , 树形结构
for index in range(len(search_issue)):
	search2 = SearchIssue(search_issue[index].key)
	print search2.get_issue_info()

print "今日上线完成"
search_issue = authed_jira.search_issues('issuetype in (线上问题, 项目上线, 上线任务) AND status = 上线完成 AND due >= -1d AND due <= 1d ORDER BY status DESC')
#pprint(search_issue)      # print search_issue , 树形结构
for index in range(len(search_issue)):
	search1 = SearchIssue(search_issue[index].key)
	print search1.get_issue_info()

print "Good bye!"





