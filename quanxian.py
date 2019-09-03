#-*-coding:utf-8-*-
import os,sys

#假定f1.txt文件存在，并具有读写权限

file_mode =['os.F_OK','os.R_OK','os.W_OK','os.X_OK']

#通过序列索引迭代
for index in range(len(file_mode)):
    results =os.access("C:\\python27",eval(file_mode[index]))
    print(type(results))
    print(str(file_mode[index]) + " - 返回值: %s"% results)