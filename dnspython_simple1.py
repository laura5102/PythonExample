#!/usr/bin/python
# -*- coding: UTF-8 -*-

import dns.resolver

domain = raw_input('Please input an domain: ')  # 输入域名地址
A = dns.resolver.query(domain, 'A')   # 指定查询类型为A的记录
for i in A.response.answer:
	for j in i.items:     # 遍历回应信息
		print j.address