# getFolderSize

##  需求
类似于linux du -sh *命令
在父目录下将各二级目录占用空间大小展示出来

## 展示：
执行结果如下：

> 
> Death Stranding Soundtrack - Extended Edition: 0.34 G
> 
> gris_ost_flac: 0.55 G
> 
> gris_ost_mp3: 0.32 G
> 
> PERSONA5【女神异闻录5: 1.28 G
> 
> The_Witcher_3_Wild_Hunt_-_Official_Soundtrack_(steam_edition)_flac: 0.49 G
> 
> 尼尔: 7.89 G
> 
> 电台节目: 0.02 G
> 
> 目录中的文件总大小：10 G
> 



## 用法：

1. 修改main函数中这个变量值：
```python
path = u'F:/music/' 
```
2. 如果需要其他级目录，可以修改main函数逻辑，通过调用`def get_size(path) -> int`获取该目录的大小


## 原理：

通过DFS一层层打开文件夹，直到返回文件的大小并累加

