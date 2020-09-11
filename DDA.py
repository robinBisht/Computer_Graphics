from graphics import *
from time import sleep

def plotPoint(x,y,wi):
	pt = Point(round(x),round(y))
	pt.setFill("blue")
	pt.draw(wi)

def DDA(x1,y1,x2,y2):
	win = GraphWin("DDA",600,600)
	win.setBackground(color_rgb(0,0,0))
	win.setCoords(-300,-300,300,300)
	dx = x2-x1
	dy = y2-y1

	n = max(abs(dx),abs(dy))

	dt = n
	dxdt = dx/dt
	dydt = dy/dt

	x = x1
	y = y1

	while(n):
		plotPoint(x,y,win)
		x += dxdt
		y += dydt
		n = n-1
		sleep(.02)
	win.getMouse()
	win.close()


if __name__ == '__main__':
	x1 = int(input( "Enter x1: " ))
	y1 = int(input( "Enter y1: " ))
	x2 = int(input( "Enter x2: " ))
	y2 = int(input( "Enter y2: " ))
	DDA(x1,y1,x2,y2)