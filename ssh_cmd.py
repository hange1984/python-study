# -*- coding: UTF-8-*-
# SSH 专用包
import paramiko


def ssh(iplist, passwd, cmd, cmd2):
    # 建立ssh链接
    ssh = paramiko.SSHClient()
    # 设置ssh自动接收公钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 使用root进行链接
    for ip in iplist:
        for password in passwd:
            try:
                print("----thread going to try:------", ip, password, "-------------")
                ssh.connect(ip, username='root', port='22', password=password)
                stdin, stdout, stderr = ssh.exec_command(cmd)
                result = stderr.readlines()
                if len(result) > 0 :
                    print 'ERROR:' + result[0]
                    exit()
                for item in stdout.readlines():
                    print item
                stdin, stdout, stderr = ssh.exec_command(cmd2)
                result2 = stderr.readlines()
                if len(result2) > 0:
                    print 'ERROR:' + result2[0]
                    exit()
                for item in stdout.readlines():
                    print item
                ipsuccess.append(ip)
                break
            except:
                print 'IP:' + ip + ' User:root Password:' + password + ' authentication faile'

    ssh.close()


def saltMaster(iplist):
    # 建立ssh链接
    ssh = paramiko.SSHClient()
    # 设置ssh自动接收公钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    master_ip = '10.128.158.15'
    for ip in iplist:
        master_cmd = 'salt-key -d '+ip+' -y'
        ssh.connect(master_ip, username='root', port='22', password='Root1234')
        stdin, stdout, stderr = ssh.exec_command(master_cmd)
        result = stderr.readlines()

        if len(result) > 0:
            print 'ERROR:' + result[0]

            exit()
        for item in stdout.readlines():
            print item

    ssh.close()



if __name__ == '__main__':
    iplist = []
    username = 'root'
    port = '22'
    passwd = ['654321', 'Root1234']
    ipsuccess = []
    ipfalse = []
    f = open('ip.txt', 'r')
    for line in f:
        line2 = line.replace(':', '').strip()
        iplist.append(line2)
    print(iplist)
    print(len(iplist))
    f.close
    saltMaster(iplist)


    cmd = "rm -rf /var/run/salt-minion.pid /etc/salt/pki/minion/minion*"
    cmd2 = "service salt-minion restart"
    ssh(iplist, passwd, cmd, cmd2)
    print '成功的IP地址:'
    print ipsuccess
    for i in iplist:
        if i not in ipsuccess:
            ipfalse.append(i)
    print '失败的IP地址：'
    print list(set(ipfalse))