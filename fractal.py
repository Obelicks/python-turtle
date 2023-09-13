import turtle

def invisible_move(t,length):
    t.penup()
    t.fd(length)
    t.pendown()

def snowflake(t,length):
    length = 3**length
    koch(t,length)
    t.rt(120)
    koch(t,length)
    t.rt(120)
    koch(t,length)

def koch(t,x):
    if x < 3:
        t.fd(x*1)
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

def all_together_now(t):
    t.pencolor("red")

    invisible_move(t,-750)

    triangle(t,200,7)

    invisible_move(t,450)

    t.lt(90)
    t.pencolor("green")
    Tree(t,100,12)
    t.rt(90)

    invisible_move(t,250)

    t.pencolor("blue")
    t.lt(60)
    snowflake(t,5)
    invisible_move(t,250)
    crazy(t)

def crazy(t):
    for i in range(360):
        for colors in ['red', 'yellow', 'green', 'purple', 'orange', 'blue']:
            t.pencolor(colors)
            t.forward(i)
            t.left(124)

bob = turtle.Turtle()
screen = turtle.Screen() 
screen.bgcolor("black") #Background color set to black
bob.hideturtle() #Hide the turtle spite
bob.speed(0)
bob.pencolor("white")
#turtle.tracer(0,0)

all_together_now(bob)
#turtle.update()
turtle.mainloop()

