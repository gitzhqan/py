# -*- coding: utf-8 -*-
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip = '172.30.69.250'
ssh.connect(ip, 22, 'NYzhangqian', 'w2e3r4t5y6', timeout=10)
stdin, stdout, stderr = ssh.exec_command('')
stdin = ssh.exec_command('1'+'/n')
print stdout.readlines()
for x in stdout.readlines():
    print x.strip('n')
print '%s/tOK/n' % (ip)
ssh.close()