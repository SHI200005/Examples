import numpy as np
import matplotlib.pylab as pl

x0 = 0.0
y0 = 0.0
L0 = 16.0

x_line = [x0,x0+0.5*L0,x0-0.5*L0,x0]#绘制三角形外轮廓
y_line = [y0+np.sqrt(3)/4*L0,
          y0-np.sqrt(3)/4*L0,y0-np.sqrt(3)/4*L0,y0+np.sqrt(3)/4*L0]
pl.plot(x_line, y_line)

def fill_triangles(x,y,L):#以[x,y]为参考点，L为参考边长填充三角形
    x_dot = []
    y_dot = []
    if L-1 > 0.01:#以三角形边长作为循环结束的标准
        x_dot = [x-0.25*L,x+0.25*L,x,x-0.25*L]
        y_dot = [y,y,y-np.sqrt(3)/4*L,y]
        pl.plot(x_dot, y_dot)
        pl.fill_between(x_dot, y_dot, facecolor='black', alpha=0.3)
        x1 = x - 0.25*L
        x2 = x + 0.25*L
        x3 = x
        y1 = y - np.sqrt(3)/8*L
        y2 = y - np.sqrt(3)/8*L
        y3 = y + np.sqrt(3)/8*L
        L = L/2
        fill_triangles(x1,y1,L)#绘制下一级，为3个三角形
        fill_triangles(x2,y2,L)
        fill_triangles(x3,y3,L)
    return None

fill_triangles(x0,y0,L0)
pl.axis("equal")
pl.show()
