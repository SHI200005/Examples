# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:26:33 2020

@author: slnsi
"""
import numpy as np
import matplotlib.pyplot as pl

n=125
a = np.zeros((2*n+1,n+1))#创建n+1行2n+1列的0二维数组
xlist=[]#用于存储奇数点的列表
ylist=[]

a[n][n]=1#顶端赋值
xl=n#杨辉三角的端点生长设定
xr=n
y=n
xlist.append(n)#顶点坐标存入列表
ylist.append(n)
for i in range(n):
    xl=xl-1
    xr=xr+1
    y=y-1
    a[xl][y]=1#左端赋1
    a[xr][y]=1#右端赋1
    xlist.append(xl)#端点1值都计入列表
    ylist.append(y)
    xlist.append(xr)
    ylist.append(y)
    for j in range(i+1):
        if a[xl+2*j][y]+a[xl+2*j+2][y]==1:#一次计算本行相邻两个数的和，如果和为奇数
            a[xl+2*j+1][y-1]=1#下一行对应元素设为1
            xlist.append(xl+2*j+1)#将下一行那个点计入列表
            ylist.append(y-1)

pl.plot(xlist,ylist,'ro',ms=1.5)
pl.axis("equal")
pl.show()
    
            