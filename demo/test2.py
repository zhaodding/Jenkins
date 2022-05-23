# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/22 17:54
# @Function    :
import os

import winrm


def winCMD(hostname, username, password, cmd):
    '''
    在 windows 下执行命令
    '''
    try:
        wintest = winrm.Session(hostname + ':3389/wsman', auth=(username, password))
        ret = wintest.run_cmd(cmd)
        print(ret.std_out.decode())
        print(ret.std_err)
    except Exception as e:
        print(e)

winCMD(hostname='192.168.80.130', username='administrator', password='tom@000000', cmd='dir')






# import paramiko
#
# client = paramiko.SSHClient()
# client.load_system_host_keys()
# try:
#     client.connect("192.168.80.130", username="administrator", password="tom@000000")
#     _, stdout, _ = client.exec_command("[ -f /opt/ad/bin/email_tidyup.sh ] && echo OK")
#     os.path.exists('aa.txt')
#     print(stdout.read())
# except Exception as e:
#     print(e)
#
# client.close()
