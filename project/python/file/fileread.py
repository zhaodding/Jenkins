# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/26 8:57
# @Function    :

list1 = ["张三","里斯","王五"]
with open("message.txt","w") as file:
    file.writelines(list1)