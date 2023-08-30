import turtle

def square(t, length):
    t.fd(length)
    for i in range(3):
        t.lt(90)
        t.fd(length)

def polygon(t, length,sides):
    t.fd(length)
    for i in range(sides-1):
        t.lt(360/sides)
        t.fd(length)

bob = turtle.Turtle()
#print(bob)

#square(bob, 1000)
polygon(bob,100,20)
turtle.mainloop()
