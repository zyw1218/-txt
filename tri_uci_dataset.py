# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
#x_train=pd.read_csv(r'UCI HAR Dataset\UCI HAR Dataset\train\X_train.txt')
#y_train=pd.read_csv(r'UCI HAR Dataset\UCI HAR Dataset\train\y_train.txt')
subject_train=pd.read_csv(r'UCI HAR Dataset\UCI HAR Dataset\train\subject_train.txt')#测试者编号
import os
import os.path
import re
import sys
import codecs
#reload(sys)
#sys.setdefaultencoding('utf-8')
 
#这里放着你要操作的文件夹名称
path = r'E:\jys\UCI HAR Dataset\UCI HAR Dataset\train\Inertial Signals'
 
#把e:\get_key\目录下的文件名全部获取保存在files中
#files = os.listdir(path)
##用set可以很好的去重，在数据处理的时候经常会被使用到。这里做初始化
#datas = set()
#for file in files :
#    if not os.path.isdir(file):
#        f=open(path+"/"+file)
#        iter_f = iter(f); #创建迭代器
#data = []
#for line in open("data.txt","r"): #设置文件对象并读取每一行文件
#    data.append(line)               #将每一行文件加入到list中 
def read_tableMethod(filename):
    data=pd.read_table(filename,header=None,delim_whitespace=True)
    return data
def file_name(file_dir): 
    data=[] 
    names=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                File=os.path.join(root,file)#子文件
#                L.append(os.path.join(root, file))
                name=file.split('.')[0]
                names.append(file.split('.')[0])
                a=read_tableMethod(File)
                data.append(a)#                b=a
    return data,names
file_dir=r'E:\jys\UCI HAR Dataset\UCI HAR Dataset\train'
x_train_filename=r'UCI HAR Dataset\UCI HAR Dataset\train\X_train.txt'
#y_train_filename=(r'UCI HAR Dataset\UCI HAR Dataset\train\y_train.txt'
data,names=file_name(file_dir)
L=read_tableMethod(x_train_filename)
#y_train=read_
# =============================================================================
#str = ""
#s=[]
#for line in iter_f: #遍历文件，一行行遍历，读取文本
#    str = str + line
#    s.append(str) #每个文件的文本存到list中
#print(s) #打印结果
# =============================================================================
# #准确获取一个txt的位置，利用字符串的拼接
# txt_path = 'E:\\get_key\\'+file.decode('utf-8')
# #把结果保存了在contents中
# contents = codecs.open(txt_path.decode('utf-8'),'r',encoding='utf-8')
#  
# #datas的数据清空 
# datas.clear()
#  
# #把数据add到datas中，可以去重
# for content in contents:
#  print(content.decode('utf-8'))
#  datas.add(content.decode('utf-8'))
# 
# #去重后新的文件保存的路径
# new_txt_path = 'E:\\get_key3\\' + file.decode('utf-8')
# unique_keywords = codecs.open(new_txt_path.decode('utf-8'), 'w', encoding='utf-8')
# 
# #把datas里的数据输出到新生成的txt中
# for data in datas:
#  unique_keywords.write(data+"\n")
# 
# #释放资源
# unique_keywords.close()</span>

