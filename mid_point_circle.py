from graphics import *
from time import sleep


def plotPoint(x,y,win):
	pt = Point(round(x),round(y))
	pt.setFill("blue")
	pt.draw(win)

def MidPointCircle(xc,yc,r):
	win = GraphWin("DDA",600,600)
	win.setBackground(color_rgb(250,250,250))
	win.setCoords(-300,-300,300,300)

	x = 0
	y = r

	plotPoint(xc,yc+r,win)
	plotPoint(xc,yc-r,win)
	plotPoint(xc+r,yc,win)
	plotPoint(xc-r,yc,win)

	p = 5/4 - r
	while(x<=y):
		if(p < 0):
			p+=2*x+3
		else:
			p+=2*(x+1)-2*(y-1) + 1
			y-=1
		x+=1

		plotPoint(xc+x,yc+y,win)
		plotPoint(xc+y,yc+x,win)
		plotPoint(xc-x,yc+y,win)
		plotPoint(xc-y,yc+x,win)
		plotPoint(xc-x,yc-y,win)
		plotPoint(xc-y,yc-x,win)
		plotPoint(xc+x,yc-y,win)
		plotPoint(xc+y,yc-x,win)	

		sleep(0.05)
	win.getMouse()
	win.close()


if __name__ == "__main__":
	# MidPointCircle(250,250,10)
	x = int(input( "Enter x: " ))
	y = int(input( "Enter y: " ))
	r = int(input( "Enter radius: " ))
	MidPointCircle(x,y,r)