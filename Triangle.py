import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.shape("turtle")

color =["pink","orange","green","red","yellow","blue","cyan","navy"]

def shape(side,a):
    for x in range(a):
        t.fd(side)
        t.lt(360/a)
for i in range(3,11):
    t.pencolor(color[i-3])    
    shape(100,i)

s.mainloop()