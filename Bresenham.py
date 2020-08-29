from graphics import *
from time import sleep



def Bresenham(x1,y1,x2,y2):
	win = GraphWin("DDA",500,500)
	win.setBackground(color_rgb(0,0,0))

	x = x1
	y = y1

	dx = x2-x1
	dy = y2-y1
	p = 2*dx-dy
	while(x <= x2):
		pt = Point(x,y)
		pt.setFill("blue")
		pt.draw(win)
		x+=1
		if(p<0):
			p = p+2*dy
		else:
			p = p+2*dy-2*dx
			y+=1
		sleep(0.02)

	win.getMouse()
	win.close()

Bresenham(10,10,150,150)