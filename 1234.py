#-*-coding:utf-8 -*-
'''
  正则表达式 确定邮件是否满足正则表达式的要求。
'''
import re
def is_valid_email(addr):
	if re.match('[\w+.-]+@[\w.-]+.\w{3}',addr):
	    print('ok')
	else:
		print('wrong')



