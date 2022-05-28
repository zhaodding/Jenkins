# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/27 14:21
# @Function    :

import winrm

session = winrm.Session('192.168.80.130', auth=('administrator', 'tom@000000'))
cmd = session.run_cmd('ipconfig')
t = cmd.std_out
print(t)

# import winrm
# wintest = winrm.Session('192.168.80.130', auth=('administrator', 'tom@000000'))
# ret = wintest.run_cmd('cd C:')
#
# ret.std_out
# print(ret.std_out)





# -*- coding:utf8 -*-
# import winrm
#
# IP_LOCAL = '192.168.80.130'
# username = 'administrator'
# password = 'tom@000000'
# shells = {'ifconfig'}
#
# CMD = [
#     'mkdir win_test_file',
#     'mkdir win_test_file1',
#     'ipconfig'
# ]
#
#
# s = winrm.Session(IP_LOCAL, auth=(username, password), transport='ntlm')  # 远程连接windows
# r = s.run_ps(shells)  # 执行脚本
# print(r.status_code)
# print(str(r.std_out))

# def run_cmd(ip, user, pwd, cmd_list):
#     try:
#         win = winrm.Session(ip, auth=(username, password), transport='ntlm')
#         for cmd in cmd_list:
#             ret = win.run_ps(cmd)
#             if ret.status_code == 0:  # 调用成功
#                 print(str(ret.std_out))
#             else:
#                 return False
#         return True
#     except Exception as e:
#         print(e)
# # 测试命令执行
#
# run_cmd(IP_LOCAL, 'administrator', password, CMD)


# s = str(r.std_out)
# b5 = s.encode('big5')
# print(b5)
















# ##windows验证winrm开启情况
# winrm enumerate winrm/config/Listener
#
# ##winrm添加windows本地用户
# New-LocalUser -name "pcpdevops" -Password (ConvertTo-SecureString -String 'zA)00xh+MxNA@h.)T9Ws' -AsPlainText -Force) -AccountNeverExpires -PasswordNeverExpires
# Add-LocalGroupMember -Group "Administrators" -Member "pcpdevops"