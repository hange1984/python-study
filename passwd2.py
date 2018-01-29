# -*- coding:utf-8 -*-

# SSH 所用包
import paramiko
# 时间模块
import time

def ssh_su_root(ip,username,password,root_pwd,cmd)
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(ip,22,username=username,password=password,timeout=4)
	excpet Exception,e:
		print str(e)
		return
	
	if username != 'root':
		print "I'm not root!"
		ssh2 = ssh.invoke_shell()
		time.sleep(0.2)
		ssh2.send('su - \n')
		buff=''
		#这里用while循环是因为有延迟。第一次buff是空，while not false。第二次有可能命令没有执行完成。buff.endswitch都是False。
		#全部执行完成后，buff.endswith命令才变成了True。跳出循环。继续执行下面的命令。如果知道延迟的时间可以用time.sleep(4)
		while not (buff.endswith('Password: ') or buff.endswith('密码： ')):
			resp=ssh2.recv(999)
			buff += resp
		ssh2.send(root_pwd)
		ssh2.send('\n')
		buff = ''
		
		while not buff.endswith('# '):
			resp =ssh2.recv(9999)
			buff += resp
		ssh.close()
		result = buff
		print "su root result --->", result
		
		ssh.close()
	else:
		print "I am root!"
		stdin,stdout,stderr = ssh.exec_command(cmd)
		stdin.Write("Y")
		print "stdout.readlines() --->"stdout.readlines()
		ssh.close
		
		
if __name__=="__main__"
	cmd='date'
	ip='10.128.157.133'
	username='odin'
	password='odin'
	ssh_su_root(ip,username,password,'odin',cmd)
	username='root'
	ssh_su_root(ip,username,password,'Root1234',cmd)
	