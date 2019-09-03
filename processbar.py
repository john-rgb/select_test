#!/usr/bin/env/python
# _*_ coding:utf-8 _*_
# @Time   : 2018/7/13 1:08
# @Author : Jingzeng Mo
# @Project: FTP_PROGRAM

import sys
# import math
#
# import subprocess
#
#
# def progress_bar(portion, total):
#     """
#     total 总数据大小，portion 已经传送的数据大小
#     :param portion: 已经接收的数据量
#     :param total: 总数据量
#     :return: 接收数据完成，返回True
#     """
#     part = total / 50  # 1%数据的大小
#     count = math.ceil(portion / part)
#     # print(count)
#     sys.stdout.write('\r')
#     sys.stdout.write(('[%-50s]%.2f%%' % (('>' * count), portion / total * 100)))
#     sys.stdout.flush()
#
#     if portion >= total:
#         sys.stdout.write('\n')
#         return True
#
#
# # 调用方式
# portion = 0
# total = 254820000
# while True:
#     portion += 1024
#     sum = progress_bar(portion, total)
#     if sum:
#         break
# print("ok")
# def dis():
#     diskspace = "df"
#     diskspace_arg = "-h"
#     print("Gathering diskspace information %s command:\n" % diskspace)
#     subprocess.call([diskspace, diskspace_arg])
# dis()
# import os
# data = os.popen("wmic logicaldisk list brief").read()
# # data=data.strip('\\n').split(' ')
# print(type(data))
# print(data)
import ctypes
import os
import platform
import sys


def get_free_space_mb(folder):
    """ Return folder/drive free space (in bytes)
    """
    print(platform.system())
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        total_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
        return free_bytes.value/1024/1024/1024,total_bytes.value/1024/1024/1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize/1024/1024

# print(get_free_space_mb('C:\\'),'GB')
s=get_free_space_mb('h:\\')
print(len(s))
print(s)