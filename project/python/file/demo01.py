# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/25 22:04
# @Function    :




# print("\n","="*10,"蚂蚁庄园动态","="*10)
# file = open('status.txt','w',encoding='utf-8')
# print("\n即将显示。。。\n")
# file.write("上海")
# # file.close()
# file.flush()


# print("\n","="*10,"蚂蚁庄园动态","="*10)
# with open('status.txt','r',encoding='utf-8') as file:
#     pass
# print("\n即将展示。。。\n")
# #

#  查看文件内容
print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('status.txt','r',encoding='utf-8')
print("\n即将展示。。。\n")
print(file.read())
print("关闭前",file.closed)
file.close()
print("关闭后",file.closed)

'''
print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('aa.jpg','rb')
print("\n即将展示。。。\n")
print(file)
'''


