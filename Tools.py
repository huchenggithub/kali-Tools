# -*- coding: UTF-8 -*-  
#!/usr/bin/python3

import os
import time
import install

from termcolor import *

os.system('reset')
print (colored('##################################################\n制作者：极客之眼团队_{"text":"json"}\n极客之眼团队群号：659155551\n本工具只适用与kali linux中\n如有错误请联系QQ：1945649519\ngitub仓库:https://github.com/nios34/kali-Tools\n###########最后祝您使用愉快#######################',"green"))
XX= input(colored('请写出您要执行的命令:',"yellow"))
if XX == "help":
    print ("         install 安装程序")
    print ("          exit 退出")
    print ("          deb 修改安装源")
    XX= input(colored('请写出您要执行的命令:',"yellow"))
if XX == "exit":
    exit()
if XX == "deb":
    install.deb()
if XX == "install":
    install.install()
