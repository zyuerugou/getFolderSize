# -*- coding: utf-8 -*-
"""
INFO: 获取目录下文件大小并计算文件大小总和

@author: 14001
"""
import os
import os.path


def get_size(path) -> int:
    '''
    INFO: 通过DFS返回该文件夹大小
    '''
    # NOTE: 获取path目录下所有文件
    fileList = os.listdir(path)  
    s = 0
    for fileName in fileList:
        # NOTE: 获取path与filename组合后的路径
        pathTmp = os.path.join(path,fileName)  
        # NOTE: 判断是否为目录
        if os.path.isdir(pathTmp):   
            # NOTE: 是目录就继续递归查找
            s = s + get_size(pathTmp)       
        elif os.path.isfile(pathTmp):  
            # NOTE: 判断是否为文件
            # NOTE: 如果是文件，则获取相应文件的大小
            filesize = os.path.getsize(pathTmp)  
            # NOTE: 将文件的大小累加
            s = s + filesize      
    return s


if __name__ == '__main__':
    # NOTE: 由用户指定文件路径
    path=u'F:/music/'  
    folderSizeList = []
    # NOTE: 遍历目标文件夹下二级目录
    for folderName in os.listdir(path):
        # NOTE: 拼接二级目录路径
        folderPath = os.path.join(path, folderName)
        # NOTE: 如果是文件就continue
        if os.path.isfile(folderPath):
            continue
        # NOTE: 通过DFS返回该文件夹大小
        folderSize = get_size(folderPath)
        # NOTE: 将文件夹大小加入父文件夹大小中
        folderSizeList.append(folderSize)
        # NOTE: 输出 文件夹名 ： 文件夹大小(G)
        print('%s: %.2f G' % (folderName, (folderSize / 1024 / 1024 / 1024)))
    
    # NOTE: 输出一级目录总大小(G)
    print('目录中的文件总大小：%d G' % (sum(folderSizeList) / 1024 / 1024 / 1024))
