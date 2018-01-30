#-*-coding:utf-8 -*-
# SSH 所用包
import paramiko
# 时间模块
import time


def ssh_su_root(ip, username, password, root_pwd, cmd):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(ip, 22, username=username, password=password, timeout=4)
	except Exception as e:
		print(e)
		return

	if username != 'root':
		print("I'm not root!")
		ssh2 = ssh.invoke_shell()
		time.sleep(0.4)
		ssh2.send('su - \n')
		buff = ''
        #当ssh链接上后，判断不是root的话，输入“su -”。如果返回值末尾是Password：或者是“密码：”则发送root_pwd
		#如果不是的话写入buff，继续循环。直到变为password或者密码
		while not (buff.endswith('Password: ') or buff.endswith('密码： ')):
			resp = ssh2.recv(999)
			buff += resp

		ssh2.send(root_pwd)
		ssh2.send('\n')
		buff = ''
		# 当root密码输入后，如果正确，endwith返回直为#，不正确返回$
		while not (buff.endswith('# ') or buff.endswith('$ ')):
			resp = ssh2.recv(9999)
			buff += resp

		result = buff
		#将结果的第一行打印出来，判断是否root登录成功。
		print("su root result --->", result.split('\r\n')[1])
		stdin, stdout, stderr = ssh.exec_command(cmd)
		print("CMD----->" + '\n' + stdout.read())

		ssh.close()
	else:
		print("I am root!")
		stdin, stdout, stderr = ssh.exec_command(cmd)
		stdin.write("Y")
		print("stdout.readlines() --->" + stdout.readline())
		ssh.close


if __name__ == "__main__":
	cmd = 'df -h'
	ip = '10.128.157.133'
	username = 'root'
	password = 'Root1234'
	ssh_su_root(ip, username, password, 'Root1234', cmd)
	username='root'
	password = 'Root1234'
	cmd = 'date'
	ssh_su_root(ip,username,password,'Root1234',cmd)