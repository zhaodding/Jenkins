# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/27 14:36
# @Function    :


import winrm
# 虚机服务器server 2019
IP_LOCAL = '192.168.80.130'        # 服务器IP
PWD_LOCAL = 'tom@000000'              # 服务器管理员密码

# 测试的命令
CMD = [
    'mkdir win_test_file',
    'mkdir win_test_file1',
    'ipconfig'
]
def run_cmd(ip, user, pwd, cmd_list):
    try:
        win = winrm.Session('http://' + ip + ':5985/wsman', auth=(user, pwd))
        for cmd in cmd_list:
            ret = win.run_ps(cmd)
            if ret.status_code == 0:  # 调用成功
                print(cmd)
            else:
                return False
        return True
    except Exception as e:
        print(e)
# 测试命令执行
run_cmd(IP_LOCAL, 'administrator', PWD_LOCAL, CMD)
