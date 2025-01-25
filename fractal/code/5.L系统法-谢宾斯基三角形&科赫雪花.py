# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:25:32 2020

@author: slnsi
"""

from math import sin, cos, pi
import matplotlib.pyplot as pl
from matplotlib import collections #连点成线的一个包
def _init_(rule):
    info = rule['S']
    for i in range(rule['iter']):
        ninfo = []
        for c in info:
            if c in rule:
                ninfo.append(rule[c])
            else:
                ninfo.append(c)
        info = "".join(ninfo)#join()就是连接括号里的字符串
    return info

def Draw_the_lines(rule,info):
    d = rule['direct']
    a = rule['angle']
    p = (0.0, 0.0)
    l = 1.0
    lines = []
    for c in info:
        if c in "Ff":#F或f代表着前进，而其他字符只是方向的变化
            r = d * pi / 180
            t = p[0] + l*cos(r), p[1] + l*sin(r)#cos与sin变量为弧度制
            lines.append(((p[0], p[1]), (t[0], t[1])))
            p = t
        elif c == "+":
            d += a
        elif c == "-":
            d -= a
    return lines

rules = [
{
"f":"F-f-F", "F":"f+F+f", "S":"f",
"direct":0,
"angle":60,
"iter":5,
"title":"Sierpinski Triangle"
},

{
"F":"F-F++F-F", "S":"F++F++F",
"direct":0,
"angle":60,
"iter":8,
"title":"Koch Flake"
},
]

def draw(ax, rule, iter=None):
    if iter!=None:
        rule["iter"] = iter
    lines = Draw_the_lines(rule,_init_(rule))
    linecollections = collections.LineCollection(lines)
    ax.add_collection(linecollections, autolim=True)
    ax.axis("equal")
    ax.set_axis_off()
    ax.set_xlim(ax.dataLim.xmin, ax.dataLim.xmax)#图形摆中间
    #ax.invert_yaxis()

fig = pl.figure(figsize=(7,14))
for i in range(2):
    ax = fig.add_subplot(211+i)
    draw(ax, rules[i])
fig.subplots_adjust(left=0,right=1,bottom=0,top=1,wspace=0,hspace=0)
pl.show()
