# -*- coding: UTF-8-*-
#SSH ���ð�
import paramiko
# ���߳����ð�
import threading

#��ip_list.txt�ڵ�ip���뵽iplist������
iplist=['10.128.157.131','10.128.157.133']
passwd=['123','root','Root1234']
f=open('ip_list.txt','r')
for line in f:
	line=line.strip()
	iplist.append(line)
print(iplist)
print(len(iplist))
f.close

#��������
def ssh(ip,passwd,cmd):
	#����SSH����
	ssh=paramiko.SSHClient()
	#�Զ����չ�Կ
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print "----thread going to try:------",ip,"-------------"
	#����ѭ����try�ɹ����У����ɹ���except��
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