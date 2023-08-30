import turtle

def square(t):
    t.fd(100)
    for i in range(3):
        t.lt(90)
        t.fd(100)


bob = turtle.Turtle()
#print(bob)

square(bob)
turtle.mainloop()
