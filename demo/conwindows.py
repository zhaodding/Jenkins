# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/22 17:39
# @Function    :


import paramiko
import re
#创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 连接服务器
ssh.connect(hostname='192.168.80.130',port=3389,username='administrator',password='tom@000000')
# 执行命令
stdin,stdout,stderr = ssh.exec_command('ipconfig')

# 获取命令结果
result = stdout.read().decode('gbk')

print(result)