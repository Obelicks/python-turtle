import turtle
from math import pi

def square(t, length):
    polygon(t,length,4)

def polygon(t, length,sides):
    polyline(t,sides,360/sides,length)
   
def circle(t,radius,quality = 360):
    arc(t,radius,quality)

def arc(t,radius, angle, quality = 360):
    length = (2*pi*radius)/quality
    polyline(t,angle,1,length)

def polyline(t,angle,curve,length):
    t.fd(length)
    for _ in range(angle-1):
        t.lt(curve)
        t.fd(length)
        
bob = turtle.Turtle()
#square(bob, 100)
#polygon(bob,100,5)
#arc(bob,100,180)
circle(bob,100)
turtle.mainloop()
