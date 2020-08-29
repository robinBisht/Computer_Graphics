from graphics import *
from time import sleep



def Bresenham(x1,y1,x2,y2):
	win = GraphWin("DDA",500,500)
	win.setBackground(color_rgb(0,0,0))
	dx = x2-x1
	dy = y2-y1

	n = max(abs(dx),abs(dy))

	dt = n
	dxdt = dx/dt
	dydt = dy/dt

	x = x1
	y = y1

	while(n):
		pt = Point(round(x),round(y))
		pt.setFill("blue")
		pt.draw(win)
		x += dxdt
		y += dydt
		n = n-1
		sleep(.02)
	win.getMouse()
	win.close()

Bresenham(10,10,120,120)