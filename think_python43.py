import turtle
from math import pi

def square(t, length):
    t.fd(length)
    for _ in range(3):
        t.lt(90)
        t.fd(length)

def polygon(t, length,sides):
    t.fd(length)
    for _ in range(sides-1):
        t.lt(360/sides)
        t.fd(length)


def circle(t,radius,quality = 360):
    length = (2*pi*radius)/quality #2 times pi times radious gives you the circumference that is then divided into the quality rotations
    polygon(t,length,quality)

def arc(t,radius, angle, quality = 360):
    length = (2*pi*radius)/quality
    t.fd(length)
    for _ in range(angle-1):
        t.lt(1)
        t.fd(length)

bob = turtle.Turtle()
#print(bob)

#square(bob, 1000)
#polygon(bob,100,20)
bob.fd(100)
bob.bk(100)
arc(bob,100,180)
turtle.mainloop()
