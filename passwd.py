# -*- coding: UTF-8-*-
#SSH 所用包
import paramiko
# 多线程所用包
import threading

#将ip_list.txt内的ip加入到iplist【】内
iplist=['10.128.157.131','10.128.157.133']
passwd=['123','root','Root1234']
f=open('ip_list.txt','r')
for line in f:
	line=line.strip()
	iplist.append(line)
print(iplist)
print(len(iplist))
f.close

#建立函数
def ssh(ip,passwd,cmd):
	#建立SSH链接
	ssh=paramiko.SSHClient()
	#自动接收公钥
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print "----thread going to try:------",ip,"-------------"
	#密码循环，try成功运行，不成功到except。
	for pwd_try in passwd:
		try:
			ssh.connect(ip,22,username='root',password=pwd_try,timeout=4)
			stdin,stdout,stderr = ssh.exec_command(cmd)
			print "\n"
			print stdout.readline()
			print "IP is: ",ip, "passwd is ", pwd_try, " trying right"
			print "\n"
			break
		except:
			print ip,pwd_try,' trying wrong'
	ssh.close()
if __name__ == '__main__':
	cmd = 'hostname'
	threads = [len(iplist)]
	print threads
	print '****threading start*****'
	for ip in iplist:
		thread = threading.Thread(target=ssh,args=(ip,passwd,cmd))
		thread.start()
