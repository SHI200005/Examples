# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:07:13 2020
你做分形的随机法，就是混沌游戏那个
具体图形做谢宾斯基三角形和谢宾斯基地毯
@author: Daisy
"""
import matplotlib.pyplot as pl
import numpy as np
import random
                       
length=1e5
N=50000

#创造3个初始的点坐标,构成一个等边三角形
x0=[40000,80000,60000]
y0=[20000,20000,54641]


#生成N个点
x=[]
y=[]
x1=random.random()*length
y1=random.random()*length
for i in range(N):
    
    m=random.randint(0,2)
    xm=0.5*(x0[m]+x1)
    ym=0.5*(y0[m]+y1)
    x1=xm
    y1=ym
    x.append(xm)
    y.append(ym)

#作图
#fig=pl.figure(10,10)      
pl.plot(x,y,'ro',ms=0.3)
pl.axis("equal")
pl.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          