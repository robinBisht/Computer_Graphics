from graphics import *
from time import sleep


def plotPoint(x,y,win):
	pt = Point(round(x),round(y))
	pt.setFill("blue")
	pt.draw(win)

def MidPointEllipse(xc,yc,rx,ry):
	win = GraphWin("DDA",600,600)
	win.setBackground(color_rgb(250,250,250))
	win.setCoords(-300,-300,300,300)

	x = 0
	y = ry

	p1 = ( ry**2 - (rx**2 * ry) + (0.25 * rx**2) )
	dx = 2 * ry**2 * x
	dy = 2* rx**2 * y
	while(dx < dy):
		plotPoint(xc+x,yc+y,win)
		plotPoint(xc-x,yc+y,win)
		plotPoint(xc+x,yc-y,win)
		plotPoint(xc-x,yc-y,win)
		sleep(0.05)
		if(p1 < 0):
			x += 1
			dx += 2 * ry**2
			p1 += dx + ry**2
		else:
			x += 1
			y -= 1
			dx += 2*ry**2
			dy -= 2*rx**2
			p1 += dx-dy+(ry**2)

	p2 = (( ry**2 ) * (x+0.5)**2 ) + ( rx**2 * (y-1)**2 ) - rx**2*ry**2
	sleep(1)
	while( 	y >= 0 ):
		plotPoint(xc+x,yc+y,win)
		plotPoint(xc-x,yc+y,win)
		plotPoint(xc+x,yc-y,win)
		plotPoint(xc-x,yc-y,win)
		sleep(0.05)
		if(p2 > 0):
			y -= 1
			dy -= 2*rx**2
			p2 += rx**2 - dy
		else:
			y -= 1
			x += 1
			dx += 2*ry**2
			dy -= 2*rx**2
			p2 += dx-dy+rx**2

	win.getMouse()
	win.close()


if __name__ == "__main__":
	xc = int(input( "Enter x: " ))
	yc = int(input( "Enter y: " ))
	rx = int(input( "Enter radius for x axis: " ))
	ry = int(input( "Enter radius for y axis: " ))
	MidPointEllipse(xc,yc,rx,ry)