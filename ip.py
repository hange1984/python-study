# -*-coding:utf-8 -*-

"""
根据IP地址列表，统计每个IP及其网段出现的次数，并进行排序。这里使用正则匹配进行计数统计

"""


# datetime 模块为python内置的时间日期模块
import datetime
# re模块为python内置的正则表达式模块
import re

# 建立三个空的字典
dict4 = {}
dict3 = {}
dict2 = {}


def main():
	print(datetime.datetime.now())
	ifp = open("ip_list.txt", "r")
	# 将ip_list文件转为列表，并提取每一行的值
	iplist = ifp.readlines()
	for ip in iplist:
		ip = ip.strip()
		# 正则匹配是否由1-3个数字组成的。
		if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",ip):
			check(ip,4)
			check(str(re.match("\d+\.\d+\.\d+",ip).group()),3)
			check(str(re.match(r"\d+\.\d+",ip).group()),2)
# 将c4排序，根据列表的【1】进行降序，即根据出现的次数进行降序排列
	c4 = sorted(dict4.items(), key=lambda key: key[1], reverse=True)
	c3 = sorted(dict3.items(), key=lambda key: key[1], reverse=True)
	c2 = sorted(dict2.items(), key=lambda key: key[1], reverse=True)



	writeFile("c4_result",c4)
	writeFile("c3_result",c3)
	writeFile("c2_result",c2)

def check(ip,size):
	"""
	根据传入的IP和对应的size数字，去对应字典中检索是否存在，存在即+1，不存在则置为1
	:param ip: 传入单个ip字符串
	:param size: 传入数字，即A\B\C类网段
	:return: 无
	"""

	if size ==4:
		# 检查字典中是否有此IP，如果有取其value+1,如没有取默认值0
		dict4[ip] = dict4.get(ip,0) +1
	elif size == 3 :
		dict3[ip] = dict3.get(ip,0) +1
	elif size == 2 :
		dict2[ip] = dict2.get(ip,0) +1
	else:
		pass

def writeFile(filename,context):
	"""

	:param filename:写入的文件路径
	:param context:要写入的内容
	:return:无
	"""
	ofp = open(filename,'w')
	(k,s) = (context[0])
	print(k)
	# 将list中的（）元祖 取出。
	for (k,s) in context:
		mix = k + ' ' + str(s) + "\n"
		ofp.write(mix)
	ofp.close()

if __name__ == "__main__":
	main()
	print(datetime.datetime.now())

