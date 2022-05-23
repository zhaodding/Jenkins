# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/22 18:12
# @Function    :

import wmi
import os
import subprocess
import re
import socket, sys


def main():
    # host="remotemachine"
    # username="adminaam"
    # password="passpass!"
    # server =connects(host, username, password)
    # s = socket.socket()
    # s.settimeout(5)
    # print server.run_remote('hostname')

    host = "192.168.80.130"
    username = "administrator"
    password = "tom@000000"
    server = connects(host, username, password)
    s = socket.socket()
    s.settimeout(5)
    aa = server.run_remote('hostname')
    print(aa)


class connects:

    def __init__(self, host, username, password, s=socket.socket()):
        self.host = host
        self.username = username
        self.password = password
        self.s = s

        try:
            self.connection = wmi.WMI(self.host, user=self.username, password=self.password)
            self.s.connect(('192.168.80.130', 3389))
            print("Connection established")
        except:
            print("Could not connect to machine")

    def run_remote(self, cmd, minimized=True):
        call = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)

        return call

    try:
        stdin, stdout, stderr = ssh.exec_command(cmd)
    except Exception as e:
        print(e.message)

    err = ''.join(stderr.readlines())
    out = ''.join(stdout.readlines())
    final_output = str(out) + str(err)
    print(final_output)


# def run_remote(self, cmd,  minimized=True):
#     call=subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT )
#     print call

main()

# async=False,
