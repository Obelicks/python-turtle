import turtle
def snowflake(t,length):
    length = 3**length
    koch(t,length)
    t.rt(120)
    koch(t,length)
    t.rt(120)
    koch(t,length)

def koch(t,x):
    if x < 3:
        t.fd(x*33)
        return
    koch(t,x/3)
    t.lt(60) 
    koch(t,x/3)
    t.rt(120)
    koch(t,x/3)
    t.lt(60)
    koch(t,x/3)

def Tree(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length)
    t.lt(angle)
    Tree(t, length*0.66, n-1)
    t.rt(2*angle)
    Tree(t, length*0.66, n-1)
    t.lt(angle)
    t.bk(length)

def triangle(t, length, n):
    if n == 0:
        return
    triangle(t,length/2,n-1)
    t.fd(length)
    t.lt(120)
    triangle(t,length/2,n-1)
    t.fd(length)
    t.lt(120)
    triangle(t,length/2,n-1)
    t.fd(length)
    t.lt(120)


bob = turtle.Turtle()
bob.hideturtle()
triangle(bob,150, 10)
#snowflake(bob,3)
turtle.mainloop()

