#-*- coding:utf-8 -*-
import os
import time

# 时间输出格式化函数
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y/%m/%d  %H:%M', timeStruct)

# 绝对路径absPath
absPath = 'c:\\'
for fileName in os.listdir(absPath):
    fileAbsPath = os.path.join(absPath, fileName)
    # >>> os.path.join('a','b') >>> 'a\\b'
    dirModifyTime = TimeStampToTime(os.path.getmtime(fileAbsPath))

    isDir = None
    dirSize = None
    if os.path.isdir(fileAbsPath):
        isDir = '<DIR>'
        dirSize = ''
    if os.path.isfile(fileAbsPath):
            isDir = ''
            dirSize = str(format(os.path.getsize(fileAbsPath), ',') )
            print(int(dirSize)/1024)
    print(dirModifyTime, isDir.center(11, ' '), dirSize.rjust(8, ' '), fileName)
