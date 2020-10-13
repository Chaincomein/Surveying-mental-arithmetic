from graphics import *
from random import randrange
import sys
def main():
    win=GraphWin("心算",600,400)
    y=0
    z=1
    while True:
        while True:
            a=randrange(1,2000)
            b=randrange(1,2000)
            c=randrange(1,2000)
            d=randrange(1,2000)
            if a<b:
                x=a
                a=b
                b=x
            if c<d:
                x=c
                c=d
                d=x    
            dist1=a-b
            dist2=c-d
            dist3=dist1-dist2
            h1=int((a+b)/2)
            h2=int((c+d)/2)
            rh1=int(h1+4787+randrange(-2,3))
            rh2=int(h2+4687+randrange(-2,3))
            if 30<dist1<1000 and 30<dist2<1000 and dist3*dist3<=900 and z==1:
                rh1=int(h1+4787+randrange(-2,3))
                rh2=int(h2+4687+randrange(-2,3))
                z=0
                break
            if 30<dist1<1000 and 30<dist2<1000 and dist3*dist3<=900 and z==0:
                rh1=int(h1+4687+randrange(-2,3))
                rh2=int(h2+4787+randrange(-2,3))
                z=1
                break
        if y==1:
            no1.setText(str(a).zfill(4))
            no2.setText(str(b).zfill(4))
            no3.setText(str(c).zfill(4))
            no4.setText(str(d).zfill(4))
            no5.setText(str(h1).zfill(4))
            no6.setText(str(h2).zfill(4))
            no7.setText(str(int(h1+4687+randrange(-2,3))).zfill(4))
            no8.setText(str(int(h1+4787+randrange(-2,3))).zfill(4))
        if y==0:
            no1=Text(Point(100,100),str(a).zfill(4))
            no2=Text(Point(100,200),str(b).zfill(4))
            no1.draw(win)
            no2.draw(win)
            no3=Text(Point(200,100),str(c).zfill(4))
            no4=Text(Point(200,200),str(d).zfill(4))
            no3.draw(win)
            no4.draw(win)
            no5=Text(Point(300,100),str(h1).zfill(4))
            no6=Text(Point(300,200),str(h2).zfill(4))
            no5.draw(win)
            no6.draw(win)
            no7=Text(Point(400,100),str(rh1).zfill(4))
            no8=Text(Point(400,200),str(rh2).zfill(4))
            no7.draw(win)
            no8.draw(win)
            y=1
        key=win.getKey()
        if key=="Escape":
            win.close()
            sys.exit()
        
main()

    
    
