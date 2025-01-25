# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:15:04 2020

@author: slnsi
"""

#import numpy as np
from math import sin, cos, pi
import matplotlib.pyplot as plt

#the first layer is the sky
#我用不同的alpha表示透明度，画出渐变色的天空
for i in range (10):
    x=[0,30,30,0,0]
    y=[20,20,17.5+0.2*i,17.5+0.2*+i,20]
    plt.fill_between(x, y, facecolor='mediumblue', alpha=i/50,zorder=1)

for i in range (10):
    x=[0,20,20,0,0]
    y=[8,8,14-0.6*i,14-0.6*+i,8]
    plt.fill_between(x, y, facecolor='royalblue', alpha=i/30,zorder=1)
    
for i in range (10):
    x=[20,30,30,20,20]
    y=[10,10,16-0.6*i,16-0.6*+i,10]
    plt.fill_between(x, y, facecolor='royalblue', alpha=i/30,zorder=1)

#the second layer are the clouds
#我用L系统了两个分形龙，按照需要表现出来，就成了浮云的形状
rule = {
"X":"X+YF+", "Y":"-FX-Y", "S":"FX",
"direct":0,
"angle":90,
"iter":13,
"title":"Dragon"
}

d = rule['direct']
a = rule['angle']
p1 = (10.0, 6.0)
p2 = (18.0, 1.0)
l = 0.18
x = []
y = []
stack = []

info = rule['S']
for i in range(rule['iter']):
    ninfo = []
    for c in info:
        if c in rule:
            ninfo.append(rule[c])
        else:
            ninfo.append(c)
    info = "".join(ninfo) #join()就是连接括号里的字符串

for c in info:
    if c in "Ff":#F或f代表着前进，而其他字符只是方向的变化
        r = d * pi / 180
        t = p1[0] + l*cos(r), p1[1] + l*sin(r)#cos与sin变量为弧度制
        x.append(t[0])
        y.append(t[1])
        p1 = t
    elif c == "+":
        d += a
    elif c == "-":
        d -= a
    elif c == "[":
        stack.append((p1,d))
    elif c == "]":
        p1,d = stack[-1]
        del stack[-1]

for c in info:
    if c in "Ff":#F或f代表着前进，而其他字符只是方向的变化
        r = d * pi / 180
        t = p2[0] + l*cos(r), p2[1] + l*sin(r)#cos与sin变量为弧度制
        x.append(t[0])
        y.append(t[1])
        p2 = t
    elif c == "+":
        d += a
    elif c == "-":
        d -= a
    elif c == "[":
        stack.append((p1,d))
    elif c == "]":
        p2,d = stack[-1]
        del stack[-1]

plt.plot(x,y,color='lightsteelblue',linewidth='7',zorder=2)
plt.plot(x,y,'w-',zorder=2)

#the third layer are the remote mountains
#还是用的L系统，自定义规则，尝试生成群山
rule = {
"f":"+f--F", "F":"-f++F", "S":"f",
"direct":45,
"angle":15,
"iter":6,
"title":"Remote Mountain"
}

d = rule['direct']
a = rule['angle']
p1 = (-2.0, 6.0)
p2 = (4.0, 8.0)
l1 = 0.3
l2 = 0.4
x0 = []
y1 = []
y2 = []

info = rule['S']
for i in range(rule['iter']):
    ninfo = []
    for c in info:
        if c in rule:
            ninfo.append(rule[c])
        else:
            ninfo.append(c)
    info = "".join(ninfo) #join()就是连接括号里的字符串

for c in info:
    if c in "Ff":#F或f代表着前进，而其他字符只是方向的变化
        r = d * pi / 180
        t1 = p1[0] + l1*cos(r), p1[1] + l1*sin(r)#cos与sin变量为弧度制
        x0.append(t1[0])
        y1.append(t1[1])
        y2.append(t1[1]-1.5)
        p1 = t1
    elif c == "+":
        d += a
    elif c == "-":
        d -= a

for c in info:
    if c in "Ff":#F或f代表着前进，而其他字符只是方向的变化
        r = d * pi / 180
        t2 = p2[0] + l2*cos(r), p2[1] + l2*sin(r)#cos与sin变量为弧度制
        x0.append(t2[0])
        y1.append(t2[1])
        y2.append(t2[1]-1.5)
        p2 = t2
    elif c == "+":
        d += a
    elif c == "-":
        d -= a

plt.fill_between(x0, y1, facecolor='darkolivegreen',zorder=3)
plt.plot(x0,y1,'k-',linewidth=3)

x2 = x0[32:]
y2 = y2[32:]
plt.plot(x2,y2,'k-',linewidth=10,alpha=0.8,zorder=3)

#the fourth layer is the main mountain
#只是几个简单的几何形状
x = [0,10,14.5,19,21,25,30]
y = [6,10,13.5,18,18,14,11]
plt.fill_between(x, y, facecolor='sienna',zorder=4)

for i in range (10):
    x=[0,30]
    y=[6-0.7*i,11-0.7*i]
    plt.fill_between(x, y, facecolor='black', alpha=i/30,zorder=4)

x = [11,19,23,26,30]
y = [0,4,7,8,6]
plt.plot(x,y,'crimson',linewidth=3,zorder=4)
x = [22,26,28]
y = [0,6,2]
plt.plot(x,y,'crimson',linewidth=5,zorder=4)
x = [23,26]
y = [7,6]
plt.plot(x,y,'crimson',linewidth=2,zorder=4)
x = [28,27]
y = [7,5]
plt.plot(x,y,'crimson',linewidth=3,zorder=4)

#the fifth layer is the snow
#我用递归法做白色分形线条代表雪
x0 = 20.0
y0 = 18.0
L = 0.6

def draw_lines(x,y,L):#以[x,y]为参考点，L为参考边长填充三角形
    if L-0.1 > 0.01:#以三角形边长作为循环结束的标准
        x_1 = [x-L,x-9*L**2]
        y_1 = [y,y-4*L*(1/L)]
        plt.plot(x_1, y_1,'lightgrey',linewidth=20*L,zorder=5,alpha=0.7)
        plt.plot(x_1, y_1,'w-',linewidth=10*L,zorder=6)
        x_2 = [x,x+L**2]
        y_2 = [y+0.2*L,y-3*L*(1/L)]
        plt.plot(x_2, y_2,'lightgrey',linewidth=20*L,zorder=5,alpha=0.7)
        plt.plot(x_2, y_2,'w-',linewidth=10*L,zorder=6)
        x_3 = [x+L,x+6*L**2]
        y_3 = [y,y-2*L*(1/L)]
        plt.plot(x_3, y_3,'lightgrey',linewidth=20*L,zorder=5,alpha=0.7)
        plt.plot(x_3, y_3,'w-',linewidth=10*L,zorder=6)
        x1 = x - 9*L**2
        x2 = x + L**2
        x3 = x + 6*L**2
        y1 = y - 4*L*(1/L)
        y2 = y - 2*L*(1/L)
        y3 = y - 1.5*L*(1/L)
        L = L/2
        draw_lines(x1,y1,L)#绘制下一级，为3个三角形
        draw_lines(x2,y2,L)
        draw_lines(x3,y3,L)
    return None
draw_lines(x0,y0,L0)

plt.axis('off')
plt.xlim(0,30)
plt.ylim(0,20)
plt.show()
