# -*-coding:utf-8 -*-

'''
根据IP地址列表，统计每个IP及其网段出现的次数，并进行排序。这里使用正则匹配进行计数统计

'''
# datetime 模块为python内置的时间日期模块
import datetime
# re模块为python内置的正则表达式模块
import re

dict4 = {}
dict3 = {}
dict2 = {}

def main():
	print(datetime.datetime.now())
	ifp = open("ip_list.txt","r")
	iplist = ifp.readlines()
	for ip in iplist:
		ip = ip.strip()
		if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",ip):
			check(ip,4)
			check(str(re.match("\d+\.\d+\.\d+",ip).group()),3)





main()

