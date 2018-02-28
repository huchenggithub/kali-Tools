# -*- coding: UTF-8 -*-  

import os
import time

from termcolor import *


def install():
    print (colored('输入help以查询支持安装的软件',"yellow"))
    AZXX = input(colored('请写出您要安装的程序：',"yellow"))
    if AZXX == "help":
        print (colored('可安装的软件列表:',"blue"))
        print (colored('          名称          支持状态',"blue"))
        print (colored('          网易云音乐          未知',"blue"))
        print (colored('          输入法/PINYIN          OK',"blue"))
        print (colored('          补全系统          ok',"blue"))
        print (colored('          w3af          ok',"blue"))
        print (colored('          sublime_text          ok',"blue"))
        AZXX = input(colored('请写出您要安装的程序：',"yellow"))
    if AZXX ==  "网易云音乐":
        os.system('wget -o music.deb http://d1.music.126.net/dmusic/netease-cloud-music_1.1.0_amd64_ubuntu.deb')
        os.system('dpkg -i music.deb')
        os.system('apt-get -y install -f')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
    if AZXX == "输入法":
        os.system('apt-get -y install fcitx-googlepinyin')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
    if AZXX == "PINYIN":
        os.system('apt-get -y install fcitx-googlepinyin')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
    if AZXX == "补全系统":
        os.system('apt-get -y install kali-linux-all')
        print (colored("操作完成，3秒后重启脚本","blue"))
        os.system('reset')
        time.sleep(3)
        os.system('python3 Tools.py')
    if AZXX  == "w3af":
        os.system('wget -P /home https://raw.githubusercontent.com/nios34/kali-Tools/%E5%B7%A5%E5%85%B7%E4%BE%9D%E8%B5%96/SSL%20for%20W3AF.py')
        os.system('wget -P /home https://raw.githubusercontent.com/nios34/kali-Tools/%E5%B7%A5%E5%85%B7%E4%BE%9D%E8%B5%96/w3af%E8%87%AA%E5%8A%A8%E5%AE%89%E8%A3%85.sh')
        os.system('sh /home/w3af自动安装.sh')
        os.system('rm -rf /home/w3af自动安装.sh')
        os.system('rm -rf /home/SSL\ for\ W3AF.py')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
    if AZXX == "sublime_text":
        global AZXXX
        AZXXX = input(colored('请写出您要安装的位数:',"yellow"))
    if AZXXX ==  "32":
        os.system('wget -P home https://download.sublimetext.com/sublime_text_3_build_3143_x32.tar.bz2')
        os.system('tar -xf /home/sublime_text_3_build_3143_x32.tar.bz2')
        os.system('ln -s /home/sublime_text/sublime_text /root/桌面/sublime')
        os.system('ln -s /home/sublime_text/sublime_text /bin/sublime')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        print (colored("现在您可以在终端输入sublime，或在桌面开启","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
    if AZXXX == "64":
        os.system('wget -P /home https://download.sublimetext.com/sublime_text_3_build_3143_x64.tar.bz2')
        os.system('tar -xf /home/sublime_text_3_build_3143_x64.tar.bz2')
        os.system('ln -s /home/sublime_text/sublime_text /root/桌面/sublime')
        os.system('ln -s /home/sublime_text/sublime_text /bin/sublime')
        print (colored("操作完成，3秒后重启脚本","blue"))
        print (colored("现在您可以在终端输入sublime，或在桌面开启","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
def deb():
    print (colored('输入help以查询支持安装的软件',"yellow"))
    debX = input(colored('请写出您要变为的软件源：',"yellow"))
    if debX == "help":
        print (colored('可使用的软件列表:',"blue"))
        print (colored('          名称          支持状态',"blue"))
        print (colored('          中科大          ok',"blue"))
        print (colored('          官方源          OK',"blue"))
        debX = input(colored('请写出您要变为的软件源：',"yellow"))
    if debX == "中科大":
        os.system('rm -rf /etc/apt/sources.list')
        os.system('echo "deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib\ndeb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib" >/etc/apt/sources.list')
        os.system('apt-get update --fix-missing')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
    if debX == "官方源":
        os.system('rm -rf /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib" >/etc/apt/sources.list')
        os.system('apt-get update --fix-missing')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        os.system('python3 Tools.py')
def gpg():
    os.system('wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add')
    os.system('apt-get update')
    print (colored("操作完成，3秒后重启脚本","blue"))
    time.sleep(3)
    os.system('python3 Tools.py')