# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/27 14:21
# @Function    :

import winrm

# session = winrm.Session('192.168.80.130', auth=('administrator', 'tom@000000'))
# cmd = session.run_cmd('ipconfig')
# cmd.std_out

import winrm
wintest = winrm.Session('192.168.80.130', auth=('administrator', 'tom@000000'))
ret = wintest.run_cmd('ipconfig')
ret.std_out
print(ret.std_out)


# ##windows验证winrm开启情况
# winrm enumerate winrm/config/Listener
#
# ##winrm添加windows本地用户
# New-LocalUser -name "pcpdevops" -Password (ConvertTo-SecureString -String 'zA)00xh+MxNA@h.)T9Ws' -AsPlainText -Force) -AccountNeverExpires -PasswordNeverExpires
# Add-LocalGroupMember -Group "Administrators" -Member "pcpdevops"