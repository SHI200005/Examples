
import matplotlib.pylab as pl

x0 = 0.0
y0 = 0.0
L0 = 81.0

x_line = [x0-1/2*L0,x0+1/2*L0,x0+1/2*L0,x0-1/2*L0,x0-1/2*L0]#绘制正方形外轮廓
y_line = [y0+1/2*L0,y0+1/2*L0,y0-1/2*L0,y0-1/2*L0,y0+1/2*L0]
pl.plot(x_line, y_line)

def fill_rectangles(x,y,L):#以[x,y]为参考点，L为参考边长填充三角形
    x_dot = []
    y_dot = []
    if L-1 > 0.01:#以正方形边长作为循环结束的标准
        x_dot = [x-1/6*L,x+1/6*L,x+1/6*L,x-1/6*L,x-1/6*L]
        y_dot = [y+1/6*L,y+1/6*L,y-1/6*L,y-1/6*L,y+1/6*L]
        pl.plot(x_dot, y_dot)
        pl.fill_between(x_dot, y_dot, facecolor='black', alpha=0.3)
        x1 = x - 2/6*L
        x2 = x 
        x3 = x + 2/6*L
        x4 = x + 2/6*L
        x5 = x + 2/6*L
        x6 = x
        x7 = x - 2/6*L
        x8 = x - 2/6*L
        y1 = y + 2/6*L
        y2 = y + 2/6*L
        y3 = y + 2/6*L
        y4 = y
        y5 = y - 2/6*L
        y6 = y - 2/6*L
        y7 = y - 2/6*L
        y8 = y 
        L = L/3
        fill_rectangles(x1,y1,L)#绘制下一级，为八个正方形
        fill_rectangles(x2,y2,L)
        fill_rectangles(x3,y3,L)
        fill_rectangles(x4,y4,L)
        fill_rectangles(x5,y5,L)
        fill_rectangles(x6,y6,L)
        fill_rectangles(x7,y7,L)
        fill_rectangles(x8,y8,L)
    return None

fill_rectangles(x0,y0,L0)
pl.axis("equal")
pl.show()