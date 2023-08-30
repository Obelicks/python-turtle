import turtle

def square(t, length):
    t.fd(length)
    for i in range(3):
        t.lt(90)
        t.fd(length)


bob = turtle.Turtle()
#print(bob)

square(bob, 1000)
turtle.mainloop()
