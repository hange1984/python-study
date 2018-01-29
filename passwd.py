# -*- coding: UTF-8-*-
#SSH 专用包
import paramiko
# 多线程专用包
import threading

#将IP_LIST文件内容加入到iplist()里。
iplist=['10.128.157.131','10.128.157.133']
passwd=['123','root','Root1234']
f=open('ip_list.txt','r')
for line in f:
    line=line.strip()
    iplist.append(line)
print(iplist)
print(len(iplist))
f.close

#设置SSH函数，
def ssh(ip,passwd,cmd):
    #建立ssh链接
    ssh=paramiko.SSHClient()
    #设置ssh自动接收公钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("----thread going to try:------",ip,"-------------")
    #使用root进行链接，如果正确执行命令。错误跳到except
    for pwd_try in passwd:
        try:
            ssh.connect(ip,22,username='root',password=pwd_try,timeout=4)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            print("\n")
            print(stdout.readline())
            print("IP is: ",ip, "passwd is ", pwd_try, " trying right")
            print("\n")
            break
        except:
            print(ip,pwd_try,' trying wrong')
    ssh.close()
if __name__ == '__main__':
    cmd = 'hostname'
    #这个应该没什么用。
    threads = [len(iplist)]
    print(threads)
    print('****threading start*****')
    #多线程调用ssh函数。
    for ip in iplist:
        thread = threading.Thread(target=ssh,args=(ip,passwd,cmd))
        thread.start()
