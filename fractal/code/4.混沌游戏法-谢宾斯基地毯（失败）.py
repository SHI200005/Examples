# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:05:56 2020

@author: slnsi
"""

import matplotlib.pyplot as pl
import numpy as np
import random
                       
length=1e5
N=50000

#创造3个初始的点坐标,构成一个等边三角形
x0=[40000,80000,80000,40000]
y0=[20000,20000,60000,60000]


#生成N个点
x=[]
y=[]
x1=random.random()*length
y1=random.random()*length
for i in range(N):
    
    m=random.randint(0,3)
    #n=random.randint(0,3)
    #if n<3:
        #xm=2/3*x0[m]+1/3*x1
        #ym=2/3*y0[m]+1/3*y1
    #else:
        #xm=1/3*x0[m]+2/3*x1
        #ym=1/3*y0[m]+2/3*y1

    #xm=2/3*x0[m]+1/3*x1
    #ym=2/3*y0[m]+1/3*y1
    
    xm=1/3*x0[m]+2/3*x1
    ym=1/3*y0[m]+2/3*y1

    x1=xm
    y1=ym
    x.append(xm)
    y.append(ym)

#作图
#fig=pl.figure(10,10)      
pl.plot(x,y,'ro',ms=0.3)
pl.axis("equal")
pl.show()  