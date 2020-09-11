from graphics import *
from time import sleep

def plotPoint(x,y,wi):
	pt = Point(round(x),round(y))
	pt.setFill("blue")
	pt.draw(wi)

def Bresenham(x1,y1,x2,y2):
	win = GraphWin("DDA",600,600)
	win.setBackground(color_rgb(0,0,0))
	win.setCoords(-300,-300,300,300)
	x = x1
	y = y1

	dx = x2-x1
	dy = y2-y1
	p = 2*dx-dy
	while(x <= x2):
		plotPoint(x,y,win)
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