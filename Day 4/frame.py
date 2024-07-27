import turtle,random

def make_cloumn(height):
    for i in range(height):
        r=random.random()
        g=random.random()
        b=random.random()
        p.color(r,g,b)
        p.stamp()
        p.forward(15)
p=turtle.Pen()
p.setheading(90)
p.speed(1)
p.color("green")
p.shape("square")
p.shapesize(0.5)
p.up()
x=-150
y=-100
p.goto(x,y)
for i in range(1):
    make_cloumn(10)
    p.right(90)
    make_cloumn(20)
    p.right(90)
    make_cloumn(10)
    p.right(90)
    make_cloumn(20)
    
turtle.mainloop()