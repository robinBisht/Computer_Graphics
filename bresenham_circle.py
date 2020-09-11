from graphics import *
from time import sleep


def plotPoint(x,y,win):
	pt = Point(round(x),round(y))
	pt.setFill("blue")
	pt.draw(win)

def drawCircle(xc,yc,x,y,win):
	plotPoint(xc+x,yc+y,win)
	plotPoint(xc+x,yc-y,win)
	plotPoint(xc-x,yc+y,win)
	plotPoint(xc-x,yc-y,win)
	plotPoint(xc+y,yc+x,win)
	plotPoint(xc+y,yc-x,win)
	plotPoint(xc-y,yc+x,win)
	plotPoint(xc-y,yc-x,win)

def BresenhamCircle(xc,yc,r):
	win = GraphWin("DDA",600,600)
	win.setBackground(color_rgb(250,250,250))
	win.setCoords(-300,-300,300,300)

	x = 0
	y = r

	drawCircle(xc,yc,x,y,win);
	sleep(0.05)
	p = 3 - 2*r
	
	while(x<=y):
		x+=1
		if(p > 0):
			y-=1
			p += 4*(x-y)+10
		else:
			p += 4*x +6
		drawCircle(xc,yc,x,y,win)
		sleep(0.05)

	win.getMouse()
	win.close()


if __name__ == "__main__":
	BresenhamCircle(0,0,100)
	# x = int(input( "Enter x: " ))
	# y = int(input( "Enter y: " ))
	# r = int(input( "Enter radius: " ))
	# BresenhamCircle(x,y,r)